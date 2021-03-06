from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required


from .forms import SearchForm
from .models import Food
from .algorythms import Algorythm


# Create your views here.
def home(request):

    form = SearchForm()

    context = {
        'form': form,
    }

    return render(request, 'foodfinder/home.html.django', context)


@login_required(login_url='/auth/login/')
def search(request):

    if request.method == 'POST':

        form = SearchForm(request.POST)
        search_term = form.get_search_term()

        if search_term is not None:

            algorythm = Algorythm.get_algorythm_by_classname('ByCategory')
            food = Food.objects.get_food_by_search_term(search_term)

            if food is None:
                return redirect('home')

            substitutes = algorythm.search_substitutes(food, request.user)

        else:

            substitutes = []
            food = None

    else:

        form = SearchForm()


    context = {
        'form': form,
        'food': food,
        'original_food': food,
        'substitutes': substitutes,
    }

    # results : 2x3
    return render(request, 'foodfinder/results_page.html.django', context)


@login_required(login_url='/auth/login/')
def food_page(request, code):

    form = SearchForm()

    food = Food.objects.get(code=code)

    context = {
        'form': form,
        'food': food,
    }

    return render(request, 'foodfinder/food_page.html.django', context)


@login_required(login_url='/auth/login/')
def account_page(request):

    form = SearchForm()

    context = {
        'form': form,
        'account': request.user,
    }

    return render(request, 'foodfinder/account_page.html.django', context)


def legacy(request):

    form = SearchForm()

    context = {
        'form': form,
        'account': request.user,
    }

    return render(request, 'foodfinder/legacy.html.django', context)

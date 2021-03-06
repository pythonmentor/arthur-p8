from django import forms


class SearchForm(forms.Form):

    search_term = forms.CharField(
        max_length=127,
        widget=forms.TextInput(attrs={'placeholder': 'Ex : Tomates farcies'}))

    def get_search_term(self):

        if self.is_valid():
            cd = self.cleaned_data

            return cd['search_term']

        else:
            return None

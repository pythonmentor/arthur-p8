from django.test import TestCase


from foodfinder.models import Food, Category, Nutriment, FoodNutriment
from favor.models import Favor
from mugauth.models import Account


class ModelsTestCase(TestCase):

    USERNAME = 'TestUser'
    EMAIL = 'test@email.com'
    PASSWORD = 'password'

    FOOD = {
        'code': '1024',
        'name': 'TestFood',
        'img_front_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'img_back_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'nutriscore': 'A',
        'nutriments': {'fat': 1.2, 'salt': 2.4},
        'categories': ['Chocolat', 'Sugar'],
    }

    def setUp(self):

        account = Account.objects.create_user(username=self.USERNAME, email=self.EMAIL, password=self.PASSWORD)

        food = Food.objects.create(
            name=self.FOOD['name'],
            code=self.FOOD['code'],
            img_front_url=self.FOOD['img_front_url'],
            img_back_url=self.FOOD['img_back_url'],
            nutriscore=self.FOOD['nutriscore'])

        for category_name in self.FOOD['categories']:
            category = Category.objects.create(name=category_name)
            food.category_set.add(category)

        for nutriment_name, nutriment_quantity in self.FOOD['nutriments'].items():
            nutriment = Nutriment.objects.create(name=nutriment_name)

            food_nutriment = FoodNutriment.objects.create(
                food=food, nutriment=nutriment,
                quantity=nutriment_quantity)

        favor = Favor.objects.create(account=account, food=food, substitute_of=food)

    def test_models_relations(self):

        account = Account.objects.get(username=self.USERNAME)

        favors = Favor.objects.filter(account=account)

        self.assertEqual(favors.first().food.name, self.FOOD['name'])
        self.assertEqual(favors.first().substitute_of.name, self.FOOD['name'])

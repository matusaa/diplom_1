import allure
import pytest
from praktikum.ingredient import Ingredient
from data import IngredientConstants as IC


@pytest.mark.parametrize('type_ingredient,name,price', [[IC.SAUCE_TYPE, IC.SAUCE_NAME, IC.SAUCE_PRICE],
                                                        [IC.FILLING_TYPE, IC.FILLING_NAME, IC.FILLING_PRICE]])
class TestIngredient:
    @allure.title('Проверка поля type у ингредиента')
    def test_ingredient_type_true(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.type == type_ingredient

    @allure.title('Проверка поля name у ингредиента')
    def test_name_of_ingredient_true(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.name == name

    @allure.title('Проверка поля price у ингредиента')
    def test_price_of_ingredient_true(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.price == price

    @allure.title('Проверка работы метода get_type')
    def test_get_type(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_type() == type_ingredient

    @allure.title('Проверка работы метода get_name')
    def test_get_name_ingredient(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_name() == name

    @allure.title('Проверка работы метода get_price')
    def test_get_price_ingredient(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_price() == price

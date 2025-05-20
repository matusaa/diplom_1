import pytest
import allure
from praktikum.burger import Burger
from data import Receipt


@allure.feature("Тестирование класса Burger")
@pytest.mark.usefixtures("mock_bun", "mock_sauce", "mock_filling")
class TestBurger:

    @allure.title("Начальный состав бургера: булочка отсутствует, ингредиентов нет")
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    @allure.title("Выбор булочки через set_buns")
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title("Добавление ингредиента через add_ingredient")
    def test_add_ingredient(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients == [mock_sauce]

    @allure.title("Удаление ингредиента через remove_ingredient")
    def test_remove_ingredient(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_filling]

    @allure.title("Перемещение ингредиента через move_ingredient")
    def test_move_ingredient(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    @allure.title("Корректный расчет цены бургера get_price")
    def test_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_price = mock_bun.get_price() * 2 + mock_sauce.get_price() + mock_filling.get_price()
        assert burger.get_price() == expected_price

    @allure.title("Корректное формирование чека get_receipt")
    def test_get_receipt(self, mock_bun, mock_filling, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        assert receipt == Receipt.BURGER_RECEIPT
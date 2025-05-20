import allure
from praktikum.bun import Bun
from data import BunConstants as BN

@allure.feature("Тестирование класса Bun")
class TestBun:

     @allure.title("Успешное получение названия булочки")
     def test_bun_name(self):
          bun = Bun(BN.BUN_NAME, BN.BUN_PRICE)
          assert bun.get_name() == BN.BUN_NAME

     @allure.title("Успешное получение цены булочки")
     def test_bun_price(self):
          bun = Bun(BN.BUN_NAME, BN.BUN_PRICE)
          assert bun.get_price() == BN.BUN_PRICE
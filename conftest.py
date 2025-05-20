import pytest
from unittest.mock import Mock
from data import BunConstants as BC, IngredientConstants as IC


class Utils:
    @staticmethod
    def mock_bun(bun):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun[0]
        mock_bun.get_price.return_value = bun[1]
        return mock_bun

    @staticmethod
    def mock_ingredient(ingredient):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient[0]
        mock_ingredient.get_name.return_value = ingredient[1]
        mock_ingredient.get_price.return_value = ingredient[2]
        return mock_ingredient


@pytest.fixture
def mock_bun():
    return Utils.mock_bun([BC.BUN_NAME, BC.BUN_PRICE])


@pytest.fixture
def mock_sauce():
    return Utils.mock_ingredient([IC.SAUCE_TYPE, IC.SAUCE_NAME, IC.SAUCE_PRICE])


@pytest.fixture
def mock_filling():
    return Utils.mock_ingredient([IC.FILLING_TYPE, IC.FILLING_NAME, IC.FILLING_PRICE])
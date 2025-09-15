import pytest
import requests
import allure
from data import Data
import order_helper as OH


class TestOrderCreation:

    @allure.title("Тест создания заказа с разными цветами самоката")
    @pytest.mark.parametrize('color', Data.COLOR_VARIANTS)
    def test_order_creation(self, color):
        payload = OH.get_order_payload(color)
        response = requests.post(Data.BASE_URL + Data.ORDER_ENDPOINT, json=payload)
        assert response.status_code == 201
        assert "track" in response.json()

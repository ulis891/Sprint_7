import pytest
import allure
from data import Data
import order_helper as OH


class TestOrderCreation:

    @allure.title("Тест создания заказа с разными цветами самоката")
    @pytest.mark.parametrize('color', Data.COLOR_VARIANTS)
    def test_order_creation(self, samokat_api, color):
        payload = OH.get_order_payload(color)
        response = samokat_api.create_order(json=payload)
        assert response.status_code == 201
        assert "track" in response.json()


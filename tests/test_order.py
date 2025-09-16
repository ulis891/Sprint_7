import pytest
import allure
from data import Data
import order_helper as OH


@allure.epic("API Яндекс Самокат")
@allure.feature("Создание закакза")
@allure.story("Ручка /api/v1/orders")
class TestOrderCreation:

    @allure.title("Тест создания заказа с разными цветами самоката")
    @pytest.mark.parametrize('color', Data.COLOR_VARIANTS)
    def test_order_creation(self, samokat_api, color):
        payload = OH.get_order_payload(color)
        response = samokat_api.create_order(json=payload)
        assert response.status_code == 201
        assert "track" in response.json()


@allure.epic("API Яндекс Самокат")
@allure.feature("Создание закакза")
@allure.story("Ручка /api/v1/orders")
class TestOrderList:

    @allure.title("Тест получения списка заказов")
    def test_order_list(self, samokat_api):
        response = samokat_api.get_orders()
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)

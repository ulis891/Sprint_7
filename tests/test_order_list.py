import allure


class TestOrderList:

    @allure.title("Тест получения списка заказов")
    def test_order_list(self, samokat_api):
        response = samokat_api.get_orders()
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)

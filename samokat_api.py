import requests
import allure
from data import Data as D


class SamokatApi:
    @allure.step("Удаление курьера")
    def delete_courier(self, **kwargs):
        response_id = requests.post(D.BASE_URL + D.LOGIN_COURIER, **kwargs)
        courier_id = response_id.json()
        response = requests.delete(D.BASE_URL + D.DELETE_COURIER, data=courier_id)
        return response

    @allure.step(f"Создание курьера")
    def create_courier(self, *args, **kwargs):
        response = requests.post(D.BASE_URL + D.CREATE_COURIER, **kwargs)
        if response.status_code == 201:
            self.delete_courier(**kwargs)
        return response

    @allure.step("Логин курьера")
    def login_courier(self, **kwargs):
        response = requests.post(D.BASE_URL + D.LOGIN_COURIER, **kwargs)
        return response

    @allure.step("Создание заказа")
    def create_order(self, **kwargs):
        response = requests.post(D.BASE_URL + D.CREATE_ORDER, **kwargs)
        return response

    @allure.step("Получение списка заказов")
    def get_orders(self):
        response = requests.get(D.BASE_URL + D.CREATE_ORDER)
        return response

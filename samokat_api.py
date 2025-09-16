import requests
import allure
from data import Data as D


class SamokatApi:
    @allure.step("Удаление курьера")
    def delete_courier(self, **kwargs):
        if kwargs:
            if "id" not in kwargs:
                response_id = self.login_courier(**kwargs)
                if response_id.status_code == 200:
                    courier_id = str(response_id.json()["id"])
                    response = requests.delete(D.BASE_URL + D.DELETE_COURIER + courier_id)
                    return response
            courier_id = kwargs["id"]
            response = requests.delete(D.BASE_URL + D.DELETE_COURIER + courier_id)
            return response
        response = requests.delete(D.BASE_URL + D.DELETE_COURIER)
        return response

    @allure.step(f"Создание курьера")
    def create_courier(self, **kwargs):
        response = requests.post(D.BASE_URL + D.CREATE_COURIER, **kwargs)
        return response

    @allure.step("Логин курьера")
    def login_courier(self, **kwargs):
        response = requests.post(D.BASE_URL + D.LOGIN_COURIER, **kwargs)
        return response

    @allure.step("Создание заказа")
    def create_order(self, **kwargs):
        response = requests.post(D.BASE_URL + D.CREATE_ORDER, **kwargs)
        if response.status_code == 201:
            self.cancel_order(data=response.json())
        return response

    @allure.step("Получение списка заказов")
    def get_orders(self):
        response = requests.get(D.BASE_URL + D.CREATE_ORDER)
        return response

    @allure.step("Отмена заказа")
    def cancel_order(self, **kwargs):
        response = requests.put(D.BASE_URL + D.CANCEL_ORDER, **kwargs)
        return response

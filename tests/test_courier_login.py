import requests
import allure
import json
import pytest
import courier_helper
from data import Data


class TestCourierLogin:

    @allure.title("Успешный логин курьера")
    def test_courier_login(self, create_courier):
        login = create_courier[0]
        password = create_courier[1]
        payload = {"login": login, "password": password}
        response = requests.post(Data.BASE_URL + Data.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Тест логина без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_missing_field(self, create_courier, missing_field):
        login, password, firstname = create_courier
        payload = {"login": login, "password": password}
        del payload[missing_field]
        response = requests.post(Data.BASE_URL + Data.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 400, "Неверный код ответа"
        assert response.json()["message"] == "Недостаточно данных для входа", "Неверное сообщение об ошибке"

    @allure.title("Тест логина с неверным паролем")
    def test_login_wrong_password(self, create_courier):
        login, password, firstname = create_courier
        payload = {"login": login, "password": password + "wrong"}
        response = requests.post(Data.BASE_URL + Data.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 404, "Неверный код ответа"
        assert response.json()["message"] == "Учетная запись не найдена", "Неверное сообщение об ошибке"

    @allure.title("Тест логина с несуществующим пользователем")
    def test_login_nonexistent_user(self, create_courier):
        login, password, firstname = create_courier
        payload = {"login": login + "wrong", "password": password}
        response = requests.post(Data.BASE_URL + Data.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 404, "Неверный код ответа"
        assert response.json()["message"] == "Учетная запись не найдена", "Неверное сообщение об ошибке"



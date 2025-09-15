import requests
import allure
import json
import pytest
import courier_helper
from data import Data


class TestCourierCreation:

    @allure.title("Тест успешного создания курьера")
    def test_create_courier(self, create_login_password_firstname):
        payload = create_login_password_firstname
        response = requests.post(Data.BASE_URL + Data.CREATE_COURIER_ENDPOINT, json=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Тест создания дубликата курьера")
    def test_create_duplicate_courier(self, create_courier):
        login, password, firstname = create_courier
        payload = {"login": login, "password": password, "firstname": firstname}
        response = requests.post(Data.BASE_URL + Data.CREATE_COURIER_ENDPOINT, json=payload)

        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Тест создания курьера с пустым полем логина")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, create_login_password_firstname, missing_field):
        payload = create_login_password_firstname
        del payload[missing_field]
        response = requests.post(Data.BASE_URL + Data.CREATE_COURIER_ENDPOINT, json=payload)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

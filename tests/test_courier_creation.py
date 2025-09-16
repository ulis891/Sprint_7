import allure
import pytest


class TestCourierCreation:

    @allure.title("Тест успешного создания курьера")
    def test_create_courier(self, samokat_api, create_login_password_firstname):
        payload = create_login_password_firstname
        response = samokat_api.create_courier(data=payload)
        assert response.status_code == 201, "Неверный код ответа"
        assert response.json() == {"ok": True}, "Неверный ответ"

    @allure.title("Тест создания дубликата курьера")
    def test_create_duplicate_courier(self, samokat_api, create_courier):
        login, password, firstname = create_courier
        payload = {"login": login, "password": password, "firstname": firstname}
        response = samokat_api.create_courier(data=payload)
        assert response.status_code == 409, "Неверный код ответа"
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой.", "Неверный ответ"

    @allure.title("Тест создания курьера с пустым полем логина")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, samokat_api, create_login_password_firstname, missing_field):
        payload = create_login_password_firstname
        del payload[missing_field]
        response = samokat_api.create_courier(data=payload)
        assert response.status_code == 400, "Неверный код ответа"
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи", "Неверный ответ"

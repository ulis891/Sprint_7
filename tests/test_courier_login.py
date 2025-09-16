import allure
import pytest


class TestCourierLogin:

    @allure.title("Успешный логин курьера")
    def test_courier_login(self, samokat_api, create_courier):
        login = create_courier[0]
        password = create_courier[1]
        payload = {"login": login, "password": password}
        response = samokat_api.login_courier(data=payload)
        assert response.status_code == 200, "Неверный код ответа"
        assert "id" in response.json(), "Отсутствует поле id"

    @allure.title("Тест логина без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_missing_field(self, samokat_api, create_courier, missing_field):
        login, password, firstname = create_courier
        payload = {"login": login, "password": password}
        del payload[missing_field]
        response = samokat_api.login_courier(data=payload)
        assert response.status_code == 400, "Неверный код ответа"
        assert response.json()["message"] == "Недостаточно данных для входа", "Неверное сообщение об ошибке"

    @allure.title("Тест логина с неверным паролем")
    def test_login_wrong_password(self, samokat_api, create_courier):
        login, password, firstname = create_courier
        payload = {"login": login, "password": password + "wrong"}
        response = samokat_api.login_courier(data=payload)
        assert response.status_code == 404, "Неверный код ответа"
        assert response.json()["message"] == "Учетная запись не найдена", "Неверное сообщение об ошибке"

    @allure.title("Тест логина с несуществующим пользователем")
    def test_login_nonexistent_user(self, samokat_api, create_courier):
        login, password, firstname = create_courier
        payload = {"login": login + "wrong", "password": password}
        response = samokat_api.login_courier(data=payload)
        assert response.status_code == 404, "Неверный код ответа"
        assert response.json()["message"] == "Учетная запись не найдена", "Неверное сообщение об ошибке"

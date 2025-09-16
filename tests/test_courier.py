import allure
import pytest


@allure.epic("API Яндекс Самокат")
@allure.feature("Создание курьера")
class TestCourierCreation:

    @allure.title("Тест успешного создания курьера")
    def test_create_courier(self, samokat_api, create_login_password_firstname):
        payload = create_login_password_firstname
        response = samokat_api.create_courier(data=payload)
        assert response.status_code == 201, "Неверный код ответа"
        assert response.json() == {"ok": True}, "Неверный ответ"

    @allure.title("Тест создания дубликата курьера")
    def test_create_duplicate_courier(self, samokat_api, create_and_delete_courier):
        login, password, firstname = create_and_delete_courier
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


@allure.epic("API Яндекс Самокат")
@allure.feature("Логин курьера")
class TestCourierLogin:

    @allure.title("Успешный логин курьера")
    def test_courier_login(self, samokat_api, create_and_delete_courier):
        login = create_and_delete_courier[0]
        password = create_and_delete_courier[1]
        payload = {"login": login, "password": password}
        response = samokat_api.login_courier(data=payload)
        assert response.status_code == 200, "Неверный код ответа"
        assert "id" in response.json(), "Отсутствует поле id"

    @allure.title("Тест логина без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_missing_field(self, samokat_api, create_and_delete_courier, missing_field):
        login, password, firstname = create_and_delete_courier
        payload = {"login": login, "password": password}
        del payload[missing_field]
        response = samokat_api.login_courier(data=payload)
        assert response.status_code == 400, "Неверный код ответа"
        assert response.json()["message"] == "Недостаточно данных для входа", "Неверное сообщение об ошибке"

    @allure.title("Тест логина с неверным паролем")
    def test_login_wrong_password(self, samokat_api, create_and_delete_courier):
        login, password, firstname = create_and_delete_courier
        payload = {"login": login, "password": password + "wrong"}
        response = samokat_api.login_courier(data=payload)
        assert response.status_code == 404, "Неверный код ответа"
        assert response.json()["message"] == "Учетная запись не найдена", "Неверное сообщение об ошибке"

    @allure.title("Тест логина с несуществующим пользователем")
    def test_login_nonexistent_user(self, samokat_api, create_and_delete_courier):
        login, password, firstname = create_and_delete_courier
        payload = {"login": login + "wrong", "password": password}
        response = samokat_api.login_courier(data=payload)
        assert response.status_code == 404, "Неверный код ответа"
        assert response.json()["message"] == "Учетная запись не найдена", "Неверное сообщение об ошибке"


@allure.epic("API Яндекс Самокат")
@allure.feature("Удаление курьера")
class TestCourierDelete:

    @allure.title("Тест успешного удаления курьера")
    def test_delete_courier(self, samokat_api, create_courier):
        login, password, firstname = create_courier
        payload = {"login": login, "password": password}
        response = samokat_api.delete_courier(data=payload)
        assert response.status_code == 200, "Неверный код ответа"
        assert response.json() == {"ok": True}, "Неверный ответ"





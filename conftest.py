import pytest
import string
import random
import requests
from samokat_api import SamokatApi as API


@pytest.fixture
def samokat_api():
    return API()


@pytest.fixture
def delete_courier(samokat_api):
    def _delete_courier(data):
        response = samokat_api.delete_courier(data=data)
        return response
    return _delete_courier



@pytest.fixture
def create_login_password_firstname(delete_courier):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    yield payload
    if "firstName" in payload:
        del payload["firstName"]
    if "login" and "password" in payload:
        delete_courier(payload)



@pytest.fixture
def create_courier(samokat_api, create_login_password_firstname):
    response = samokat_api.create_courier(data=create_login_password_firstname)
    login_pass = []
    if response.status_code == 201:
        login_pass.append(create_login_password_firstname["login"])
        login_pass.append(create_login_password_firstname["password"])
        login_pass.append(create_login_password_firstname["firstName"])
    return login_pass


@pytest.fixture
def create_and_delete_courier(samokat_api, create_courier, delete_courier):
    login_pass = create_courier
    yield login_pass
    login, password = create_courier[:2]
    payload = {
        "login": login,
        "password": password
    }
    delete_courier(payload)

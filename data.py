class BaseData:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    # ENDPOINTS
    LOGIN_COURIER = "/api/v1/courier/login"
    CREATE_COURIER = "/api/v1/courier"
    DELETE_COURIER = "/api/v1/courier/"
    CREATE_ORDER = "/api/v1/orders"
    CANCEL_ORDER = "/api/v1/orders/cancel"


class OrderData:
    COLOR_VARIANTS = [
        ["BLACK"],
        ["GREY"],

        ["BLACK", "GREY"],
        []
    ]


class TestData:
    CREATE_DUPLICATE_COURIER_MESSAGE = "Этот логин уже используется. Попробуйте другой."
    MISSING_FIELDS_CREATE_MESSAGE = "Недостаточно данных для создания учетной записи"
    MISSING_FIELDS_LOGIN_MESSAGE = "Недостаточно данных для входа"
    WRONG_FIELDS_LOGIN_MESSAGE = "Учетная запись не найдена"

class Data:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    # ENDPOINTS
    LOGIN_COURIER = "/api/v1/courier/login"
    CREATE_COURIER = "/api/v1/courier"
    DELETE_COURIER = "/api/v1/courier/"
    CREATE_ORDER = "/api/v1/orders"
    CANCEL_ORDER = "/api/v1/orders/cancel"

    COLOR_VARIANTS = [
        ["BLACK"],
        ["GREY"],

        ["BLACK", "GREY"],
        []
    ]

from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker('ru_RU')


def get_order_payload(color=None):
    days_ahead = random.randint(1, 14)
    delivery_date = (datetime.now() + timedelta(days=days_ahead)).strftime("%Y-%m-%d")
    firstName = fake.first_name()
    lastName = fake.last_name()
    address = fake.address()
    metroStation = random.randint(1, 10)
    phone = fake.phone_number()
    rentTime = random.randint(1, 7)
    comment = fake.text(max_nb_chars=20)

    payload = {
        "firstName": firstName,
        "lastName": lastName,
        "address": address,
        "metroStation": metroStation,
        "phone": phone,
        "rentTime": rentTime,
        "deliveryDate": delivery_date,
        "comment": comment
    }

    if color:
        payload["color"] = color

    return payload




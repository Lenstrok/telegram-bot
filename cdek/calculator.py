import requests

from cdek.auth import get_headers
from cdek.schemas import LocationInfo, DeliveryInfo

STORE_TO_DOOR_TARIFF = 11  # todo уточнить про тарифы, добавить методы доставки

TEST_POST_STORE_TO_DOOR_PRICE = 'https://api.edu.cdek.ru/v2/calculator/tariff'


def get_store_to_door_price(from_location: LocationInfo, to_location: LocationInfo) -> DeliveryInfo:
    """todo"""
    return _get_price(from_location=from_location, to_location=to_location, tariff_code=STORE_TO_DOOR_TARIFF)


def _get_price(from_location: LocationInfo, to_location: LocationInfo, tariff_code: int) -> DeliveryInfo:
    """todo"""
    r = requests.post(TEST_POST_STORE_TO_DOOR_PRICE, json={
        'tariff_code': tariff_code,
        'from_location': from_location.__dict__,
        'to_location': to_location.__dict__,
        'code': '',  # todo добавить доп. услуги параметром
        'packages': [{
            "height": 10,
            "length": 10,
            "weight": 10,
            "width": 10
        }],  # todo добавить упаковки параметром
        'weight': '',  # добавить общий вес параметром (в граммах)
    }, headers=get_headers())

    if r.status_code != 200:
        raise Exception(f'Get price info: code={r.status_code}, error={r.json()}')  # todo

    return DeliveryInfo(**r.json())

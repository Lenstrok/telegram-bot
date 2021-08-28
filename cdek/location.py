from typing import List

import requests

from cdek.auth import *

TEST_GET_OFFICE_LIST = 'https://api.edu.cdek.ru/v2/deliverypoints'
TEST_GET_CITY_LIST = 'https://api.edu.cdek.ru/v2/location/cities'
TEST_GET_REGION_LIST = 'https://api.edu.cdek.ru/v2/location/regions'

RU_COUNTRY_CODE = 'RU'


def get_region_info_list() -> List[dict]:
    """todo"""

    r = requests.get(TEST_GET_REGION_LIST, params={'country_codes': RU_COUNTRY_CODE}, headers=HEADERS)

    if r.status_code != 200:
        raise Exception(f'Get regions info: code={r.status_code}, error={r.json()}')  # todo

    return [{'region': info['region'], 'region_code': info['region_code']} for info in r.json()]  # todo работать с классом, а не с dict


def get_city_info_list(region_code: int) -> List[dict]:
    """todo"""

    r = requests.get(TEST_GET_CITY_LIST, params={
        'country_codes': RU_COUNTRY_CODE,
        'region_code': region_code,
    }, headers=HEADERS)

    if r.status_code != 200:
        raise Exception(f'Get city info: code={r.status_code}, error={r.json()}')  # todo

    return [{'city': info['city'],  'code': info['code']} for info in r.json()]  # todo работать с классом, а не с dict


def get_office_info_list(city_code: int) -> List[str]:
    """todo"""

    r = requests.get(TEST_GET_OFFICE_LIST, params={
        'country_codes': RU_COUNTRY_CODE,
        'city_code': city_code,
    }, headers=HEADERS)

    if r.status_code != 200:
        raise Exception(f'Get office info: code={r.status_code}, error={r.json()}')  # todo

    return r.json()  # todo работать с классом, а не с dict

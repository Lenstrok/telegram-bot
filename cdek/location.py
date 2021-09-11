from typing import List

import requests

from cdek.errors import CdekLocationError
from cdek.auth import get_headers
from cdek.schemas.location import RegionInfo, CityInfo, OfficeInfo

TEST_GET_OFFICE_LIST = 'https://api.edu.cdek.ru/v2/deliverypoints'
TEST_GET_CITY_LIST = 'https://api.edu.cdek.ru/v2/location/cities'
TEST_GET_REGION_LIST = 'https://api.edu.cdek.ru/v2/location/regions'

RU_COUNTRY_CODE = 'RU'


def get_region_info_list() -> List[RegionInfo]:
    """Получить список информации о регионах cdek."""

    r = requests.get(TEST_GET_REGION_LIST, params={'country_codes': RU_COUNTRY_CODE}, headers=get_headers())

    if r.status_code != 200:
        raise CdekLocationError(f'Get regions info: code={r.status_code}, error={r.json()}')

    return [RegionInfo(region=info['region'], region_code=info['region_code']) for info in r.json()]


def get_city_info_list(region_code: int) -> List[CityInfo]:
    """Получить список информации о городах cdek."""

    r = requests.get(TEST_GET_CITY_LIST, params={
        'country_codes': RU_COUNTRY_CODE,
        'region_code': region_code,
    }, headers=get_headers())

    if r.status_code != 200:
        raise CdekLocationError(f'Get city info: code={r.status_code}, error={r.json()}')

    return [CityInfo(city=info['city'], code=info['code']) for info in r.json()]


def get_office_info_list(city_code: int) -> List[OfficeInfo]:
    """Получить список информации об офисах cdek."""

    r = requests.get(TEST_GET_OFFICE_LIST, params={
        'country_codes': RU_COUNTRY_CODE,
        'city_code': city_code,
    }, headers=get_headers())

    if r.status_code != 200:
        raise CdekLocationError(f'Get office info: code={r.status_code}, error={r.json()}')

    return [OfficeInfo(address_full=info['location']['address_full'], code=info['code']) for info in r.json()]

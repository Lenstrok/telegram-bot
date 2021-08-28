# todo собрать аналогично конфигу что-то
# todo и добавить адеватоное кеширование (3600 сек - жизнь токена)
# todo hardcode
# todo logging, error handling

import requests
from requests.structures import CaseInsensitiveDict


TEST_USER = 'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI'
TEST_PASS = 'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'

TEST_POST_AUTH = 'https://api.edu.cdek.ru/v2/oauth/token?parameters'


def _get_token() -> CaseInsensitiveDict:
    """todo"""
    r = requests.post(TEST_POST_AUTH, params={'grant_type': 'client_credentials',
                                              'client_id': TEST_USER,
                                              'client_secret': TEST_PASS})

    if r.status_code != 200:
        raise Exception(f'Auth: code={r.status_code}, error={r.json()}')  # todo

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {r.json()['access_token']}"

    return headers


HEADERS = _get_token()

# Клиент CDEK

### Пример:

```buildoutcfg
from cdek import get_region_info_list, get_city_info_list, get_office_info_list


if __name__ == '__main__':

    region_info_list = get_region_info_list()

    print(len(region_info_list))
    print(region_info_list)

    city_info_list = get_city_info_list(region_info_list[0].region_code)

    print(len(city_info_list))
    print(city_info_list)

    office_info_list = get_office_info_list(city_info_list[2].code)

    print(len(office_info_list))
    print(office_info_list)
```
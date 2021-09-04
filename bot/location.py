import logging

from geopy.geocoders import Nominatim
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def get_location(update: Update, context: CallbackContext) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_location = update.message.location

    geolocator = Nominatim(user_agent="lenstrok_tg_bot")
    location = geolocator.reverse(f"{user_location.latitude}, {user_location.longitude}")
    print(location.address)
    print(location.raw)

    ######################################  todo
    from cdek import get_store_to_door_price, LocationInfo, get_region_info_list, get_city_info_list

    region_info_list = get_region_info_list()
    from_location = None
    to_location = None

    for region_info in region_info_list:
        if region_info.region == 'Москва':
            for city_info in get_city_info_list(region_code=region_info.region_code):
                if city_info.city == 'Москва':
                    from_location = LocationInfo(city=city_info.city, code=city_info.code)

    print(123123123, location.raw)  # todo rm
    for region_info in region_info_list:
        print(region_info.region)  # todo rm
        # if region_info.region == 'Ростовская обл.':  # == location.raw['address']['state']:
        #     print(region_info)  # todo rm
        #     for city_info in get_city_info_list(region_code=region_info.region_code):
        #         print(city_info.city)  # todo rm  Самарское сельское поселение, Азовский район, Ростовская область, Южный федеральный округ, Россия
        #         # if city_info.city == location.raw['address']['city']:
        #         #     print(city_info)  # todo rm
        #         #     to_location = LocationInfo(city=city_info.city, code=city_info.code)

    if from_location is None or to_location is None:
        raise Exception('123123123')

    price = get_store_to_door_price(
        from_location=from_location,  # todo уточнить у Лёни про расчёт доставки, видимо по городам можно а не полный
        to_location=to_location,#LocationInfo(city=location.raw['address']['city'])    # todo уточнить у Лёни про расчёт доставки, видимо по городам можно а не полный
    )
    print(price)
    ######################################  todo

    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )

    if price.errors:
        update.message.reply_text(
            f'По данному адресу доставка не осуществляется'
        )

        return ConversationHandler.END

    update.message.reply_text(
        f'Стоимость доставки {price.total_sum}₽'
    )

    return ConversationHandler.END

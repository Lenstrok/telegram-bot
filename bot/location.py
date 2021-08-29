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

    # >>> from geopy.geocoders import Nominatim
    # >>> geolocator = Nominatim(user_agent="specify_your_app_name_here")
    # >>> location = geolocator.reverse("52.509669, 13.376294")
    # >>> print(location.address)
    # Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
    # >>> print((location.latitude, location.longitude))
    # (52.5094982, 13.3765983)
    # >>> print(location.raw)
    # {'place_id': '654513', 'osm_type': 'node', ...}

    geolocator = Nominatim(user_agent="lenstrok_tg_bot")
    location = geolocator.reverse(f"{user_location.latitude}, {user_location.longitude}")
    print(location.address)
    print(location.raw)

    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    update.message.reply_text(
        'Maybe I can visit you sometime! At last, tell me something about yourself.'
    )

    return ConversationHandler.END

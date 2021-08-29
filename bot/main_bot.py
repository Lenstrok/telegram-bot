# from telegram.ext import Updater
import logging
# from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

CATEGORIES, GOODS, BASKET, LOCATION, NAME, TAKE = range(4)


def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [['Да', 'Нет']]

    update.message.reply_text(
        'Добрый день! Вы хотите оформить заказ?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )

    return CATEGORIES


def categories(update: Update, context: CallbackContext) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    logger.info("Answer of %s: %s", user.first_name, update.message.text)

    if update.message.text == 'Да':
        reply_keyboard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12']]
        update.message.reply_text(
            '',
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True
            )
        )

        return GOODS
    else:
        update.message.reply_text(
            'Досвидули!'
        )
        return ConversationHandler.END


def goods(update: Update, context: CallbackContext) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    logger.info("Answer of %s: %s", user.first_name, update.message.text)

    if update.message.text == '1':
        reply_keyboard = [['Да', 'Нет']]
        update.message.reply_text(
            'Хотите выбрать что-то еще?',
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True
            )
        )

        return TAKE
    elif update.message.text == '2':
        reply_keyboard = [['Да','Нет']]
        update.message.reply_text(
            'Хотите выбрать что-то еще?',
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True
            )
        )

        return TAKE
    else:
        update.message.reply_text(
            'Выберите одну из предложенных категорий!'
        )
        return CATEGORIES


def take(update: Update, context: CallbackContext) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    logger.info("Answer of %s: %s", user.first_name, update.message.text)

    reply_keyboard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12']]
    update.message.reply_text(
        '',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True
        )
    )

    return BASKET


def basket(update: Update, context: CallbackContext) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return NAME


def name(update: Update, context: CallbackContext) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Name: %s", update.message.text)
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return LOCATION


def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.location
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!' 
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу `BIO`
    return GOODS


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1818495430:AAHRozBrINRMf0J_H9XoleDxoTFBYVPe4-c")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CATEGORIES: [MessageHandler(Filters.text & ~Filters.command, categories)],
            GOODS: [MessageHandler(Filters.text & ~Filters.command, goods)],
            TAKE: [MessageHandler(Filters.text & ~Filters.command, take)],
            BASKET: [MessageHandler(Filters.text & ~Filters.command, basket)],
            NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
            LOCATION: [MessageHandler(Filters.location, location)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conversation_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

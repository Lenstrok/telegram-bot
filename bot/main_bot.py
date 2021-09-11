import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler,
    RegexHandler,
    Filters,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
CASE, GOODS = range(2)
# Callback data
KV, BADGE, SHOPPER, ADD_TO_BASKET = range(4)


def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    reply_keyboard = [['Каталог', 'Корзина'], ['Заказы', 'Помощь']]

    update.message.reply_text(
        "Добрый день!\n"
        "Вы хотите сделать заказ?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            resize_keyboard=True,
            one_time_keyboard=False
        )
    )

    return CASE


def get_catalog(update: Update, context: CallbackContext) -> int:
    # todo здесь должен выводиться каталог с инлайн режимом выбора товаров

    if update.callback_query is not None:
        update.callback_query.answer()

    keyboard = list()
    keyboard.append(list())
    name = {"0": 'Кв', "1": 'Значки', "2": 'Шопперы'}
    for key, value in name.items():
        keyboard[0].append(InlineKeyboardButton(value, callback_data=key))

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Каталог \n"
    )

    update.message.reply_text(
        "Выберите категорию, чтобы вывести список товаров:",
        reply_markup=reply_markup,
    )

    return GOODS


def get_basket(update: Update, context: CallbackContext) -> int:
    return 1


def get_order(update: Update, context: CallbackContext) -> int:
    return 1


def get_help(update: Update, context: CallbackContext) -> int:
    return 1


def kv(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    # query.edit_message_text(
    #     text="Книги вслепую:"
    # )
    keyboard = [
        [
            InlineKeyboardButton("Добавить в корзину", callback_data=str(ADD_TO_BASKET)),

        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    photo = r"C:\Users\User\Desktop\tg_bot_flask_admin\telegram-bot\bot\user_photo.jpg"
    chat_id = int(context._chat_id_and_data[0])

    context.bot.send_photo(
        chat_id=chat_id,
        photo=open(photo, 'rb'),
        caption='Книжечка',
        reply_markup=reply_markup,
    )

    return GOODS


def badge(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("a", callback_data=str(A)),
            InlineKeyboardButton("b", callback_data=str(B)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="A category:",
        reply_markup=reply_markup,
    )
    return FIRST


def shopper(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Second CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return FIRST


c = int(0)


def add_to_basket(update: Update, context: CallbackContext) -> int:
    # todo добавляем в базу инфу о покупке товара
    query = update.callback_query
    query.answer()
    global c
    c += 1
    keyboard = [
        [
            InlineKeyboardButton(f"Добавить в корзину ({c} шт.)", callback_data=str(ADD_TO_BASKET))
        ],

        [
            InlineKeyboardButton("Корзина", callback_data=str(CASE)),
        ],

        [
            InlineKeyboardButton("Каталог", callback_data=str(CASE)),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_reply_markup(
        reply_markup=reply_markup,
    )

    return GOODS


def end(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1818495430:AAHRozBrINRMf0J_H9XoleDxoTFBYVPe4-c")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CASE: [
                # MessageHandler(Filters.regex('^(Каталог|Корзина|Заказы|Помощь)$'), case),
                MessageHandler(Filters.regex('^(Каталог)$'), get_catalog),
                MessageHandler(Filters.regex('^(Корзина)$'), get_basket),
                MessageHandler(Filters.regex('^(Заказы)$'), get_order),
                MessageHandler(Filters.regex('^(Помощь)$'), get_help),
                # Filters.text & ~Filters.command
            ],
            GOODS: [
                CallbackQueryHandler(kv, pattern='^' + str(KV) + '$'),
                CallbackQueryHandler(badge, pattern='^' + str(BADGE) + '$'),
                CallbackQueryHandler(shopper, pattern='^' + str(SHOPPER) + '$'),
                CallbackQueryHandler(add_to_basket, pattern='^' + str(ADD_TO_BASKET) + '$'),
                # CallbackQueryHandler(get_catalog_over, pattern='^' + str(ADD_TO_BASKET) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    dispatcher.add_handler(conversation_handler)

    updater.start_polling()

    updater.idle()

# CATEGORIES, GOODS, BASKET, LOCATION, NAME, TAKE, SELECT_CONNECT, MONEY = range(8)
#
#
# def start(update: Update, context: CallbackContext) -> int:
#     """Starts the conversation and asks the user about their gender."""
#     reply_keyboard = [['Да', 'Нет']]
#
#     update.message.reply_text(
#         'Добрый день! Вы хотите оформить заказ?',
#         reply_markup=ReplyKeyboardMarkup(
#             reply_keyboard, one_time_keyboard=True, resize_keyboard=True
#         ),
#     )
#
#     return CATEGORIES
#
#
# def categories(update: Update, context: CallbackContext) -> int:
#     """Stores the selected gender and asks for a photo."""
#     user = update.message.from_user
#     logger.info("Answer of %s: %s", user.first_name, update.message.text)
#
#     if update.message.text == 'Да':
#         reply_keyboard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12']]
#         update.message.reply_text(
#             'Выберите категорию',
#             reply_markup=ReplyKeyboardMarkup(
#                 reply_keyboard, one_time_keyboard=True
#             )
#         )
#
#         return GOODS
#     else:
#         update.message.reply_text(
#             'Досвидули!'
#         )
#         return ConversationHandler.END
#
#
# def goods(update: Update, context: CallbackContext) -> int:
#     """Stores the selected gender and asks for a photo."""
#     user = update.message.from_user
#     logger.info("Answer of %s: %s", user.first_name, update.message.text)
#
#     # здесь должны выводится товары выбранной категории
#
#     if update.message.text == '1':
#         reply_keyboard = [['Да', 'Нет']]
#         update.message.reply_text(
#             'Хотите выбрать что-то еще?',
#             reply_markup=ReplyKeyboardMarkup(
#                 reply_keyboard, one_time_keyboard=True, resize_keyboard=True
#             )
#         )
#
#         return BASKET
#     elif update.message.text == '2':
#         reply_keyboard = [['Да','Нет']]
#         update.message.reply_text(
#             'Хотите выбрать что-то еще?',
#             reply_markup=ReplyKeyboardMarkup(
#                 reply_keyboard, one_time_keyboard=True
#             )
#         )
#
#         return BASKET
#     else:
#         update.message.reply_text(
#             'Выберите одну из предложенных категорий!'
#         )
#         return CATEGORIES
#
#
# def basket(update: Update, context: CallbackContext) -> int:
#     user = update.message.from_user
#     logger.info("Bio of %s: %s", user.first_name, update.message.text)
#
#     # Здесь должна выводиться корзина
#     if update.message.text == 'Нет':
#         update.message.reply_text('Ваша корзина : кек')
#         update.message.reply_text('Как к вам обращаться?')
#         return NAME
#     else:
#         return CATEGORIES
#
#
# def name(update: Update, context: CallbackContext) -> int:
#     user = update.message.from_user
#     logger.info("Name: %s", update.message.text)
#     update.message.reply_text('Отправьте геопозицию, куда доставить товар.')
#
#     return LOCATION
#
#
# def location(update: Update, context:CallbackContext) -> int:
#     # определяем пользователя
#     user = update.message.from_user
#     # захватываем местоположение пользователя
#     user_location = update.message.location
#     # Пишем в журнал сведения о местоположении
#     logger.info(
#         "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
#     # Отвечаем на сообщение с местоположением
#     reply_keyboard = [['VK', 'TG'], ['Phone', 'Email']]
#     update.message.reply_text(
#         'Выберете способ связи из списка.',
#         reply_markup=ReplyKeyboardMarkup(
#             reply_keyboard, one_time_keyboard=True
#         )
#     )
#
#     return SELECT_CONNECT
#
#
# def selectconnect(update: Update, context: CallbackContext) -> int:
#     user = update.message.from_user
#     # logger.info("Способ связи для %s: %s", user.first_name, update.message.text)
#
#     update.message.reply_text(f'Введите {update.message.text}')
#
#     return MONEY
#
#
# def money(update: Update, context: CallbackContext) -> int:
#     user = update.message.from_user
#     logger.info("Контакты для %s: %s", user.first_name, update.message.text)
#
#     update.message.reply_text('Заплатите 200000 деняк')
#
#     return ConversationHandler.END
#
#
# def cancel(update: Update, context: CallbackContext) -> int:
#     """Cancels and ends the conversation."""
#     user = update.message.from_user
#     logger.info("User %s canceled the conversation.", user.first_name)
#     update.message.reply_text(
#         'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
#     )
#
#     return ConversationHandler.END
#
#
# def main() -> None:
#     """Run the bot."""
#     # Create the Updater and pass it your bot's token.
#     updater = Updater("1818495430:AAHRozBrINRMf0J_H9XoleDxoTFBYVPe4-c")
#
#     # Get the dispatcher to register handlers
#     dispatcher = updater.dispatcher
#
#     # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
#     conversation_handler = ConversationHandler(
#         entry_points=[CommandHandler('start', start)],
#         states={
#             CATEGORIES: [MessageHandler(Filters.text & ~Filters.command, categories)],
#             GOODS: [MessageHandler(Filters.text & ~Filters.command, goods)],
#             BASKET: [MessageHandler(Filters.text & ~Filters.command, basket)],
#             NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
#             LOCATION: [MessageHandler(Filters.location, location)],
#             SELECT_CONNECT: [MessageHandler(Filters.text & ~Filters.command, selectconnect)],
#             MONEY: [MessageHandler(Filters.text & ~Filters.command, money)],
#         },
#         fallbacks=[CommandHandler('cancel', cancel)],
#     )
#
#     dispatcher.add_handler(conversation_handler)
#
#     updater.start_polling()
#
#     updater.idle()


if __name__ == '__main__':
    main()

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_handler(bot, message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton('Написать в поддержку',
                             url='https://t.me/corvussharp'),
        InlineKeyboardButton('Получить список товаров',
                             callback_data='get_products')
    )
    keyboard.row(
        InlineKeyboardButton('Показать баланс', callback_data='balance'),
        InlineKeyboardButton('Подписаться', callback_data='subscribe')
    )
    keyboard.row(
        InlineKeyboardButton('Рассчитать поставку', callback_data='delivery')
    )
    bot.send_message(message.chat.id,
                     'Добро пожаловать! Выберите действие из меню.',
                     reply_markup=keyboard)

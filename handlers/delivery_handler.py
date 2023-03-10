from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def delivery_handler(bot, message):
    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton('7 дней', callback_data='7'),
        InlineKeyboardButton('21 день', callback_data='21')
    )
    keyboard.row(
        InlineKeyboardButton('14 дней', callback_data='14'),
        InlineKeyboardButton('30 дней', callback_data='21')
    )

    bot.send_message(message.chat.id, 'Выберите количество дней:',
                     reply_markup=keyboard)

from .products_handler import *
from .balance_handler import *
from .subscribe_handler import *
from .delivery_handler import *


def callback_handler(bot, call):
    if call.data == 'get_products':
        try:
            products_handler(bot, call.message)
        except Exception as e:
            # logging.exception('Ошибка при получении списка товаров')
            bot.send_message(call.message.chat.id,
                             'Ошибка при получении списка товаров. Попробуйте позже.')
    elif call.data == 'balance':
        try:
            balance_handler(bot, call.message)
        except Exception as e:
            # logging.exception('Ошибка при получении баланса')
            bot.send_message(call.message.chat.id,
                             'Ошибка при получении баланса. Попробуйте позже.')
    elif call.data == 'subscribe':
        try:
            subscribe_handler(bot, call.message)
        except Exception as e:
            # logging.exception('Ошибка при оформлении подписки')
            bot.send_message(call.message.chat.id,
                             'Ошибка при оформлении подписки. Попробуйте позже.')
    elif call.data == 'delivery':
        try:
            delivery_handler(bot, call.message)
        except Exception as e:
            # logging.exception('Ошибка при расчёте поставки')
            bot.send_message(call.message.chat.id,
                             'Ошибка при расчёте поставки. Попробуйте позже.')

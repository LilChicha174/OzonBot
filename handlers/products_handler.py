from Settings import OZON_API_TOKEN


def products_handler(bot, message):
    try:
        products = get_products()
        for product in products['result']['items']:
            bot.send_message(message.chat.id,
                             f"{product['name']}: {product['price']['value']} руб.")
    except Exception as e:
        bot.send_message(message.chat.id,
                         f'Ошибка при получении списка товаров: {e}')


def get_products():
    url = 'https://api.ozon.ru/merchant/v1/product/list'
    headers = {'Content-Type': 'application/json', 'Client-Id': OZON_API_TOKEN}
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    products = json.loads(response.text)
    return products

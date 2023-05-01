import requests
import json
import time


def get_price():
    """Получаем текущую цену из API binance"""

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    response = requests.get(url)
    data = json.loads(response.text)
    return float(data['price'])


def check_price():
    """Получаем текущую цену и проверяем ее изменение.
      Выводим сообщение в консоль, если цена изменилась на 1% за последний час"""
    prices = []
    while True:
        current_price = get_price()
        prices.append(current_price)
        if len(prices) > 3600:
            prices.pop(0)
        if len(prices) > 1:
            price_change = (current_price - prices[0]) / prices[0] * 100
            if abs(price_change) >= 1:
                print(f'Цена изменилась: {price_change:.2f}% за последний час')
            else:
                print('Цена не выросла более чем на 1% за последние 60 минут')
        time.sleep(60)


if __name__ == "__main__":
    check_price()

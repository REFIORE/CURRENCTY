import os
import requests
import argparse
from urllib.error import HTTPError
from dotenv import load_dotenv


def get_exchange_rates(token, base_currency):
    exchange_rates_url = f'https://v6.exchangerate-api.com/v6/{token}/latest/{base_currency}'
    response = requests.get(exchange_rates_url)
    response.raise_for_status()
    exchange_rates = response.json()['conversion_rates']
    return exchange_rates


def convert_amount(amount_money, exchange_rates, target_exchange_rates):
    target_rates = exchange_rates[target_exchange_rates]
    print('Целевая валюта: ', target_rates)
    convertible_currency = amount_money * target_rates
    return convertible_currency


def main():
    load_dotenv()
    token = os.getenv('API_KEY')
    parser = argparse.ArgumentParser(description='Эта програма конвертирует базовые валюты в целевые')
    parser.add_argument('-b', '--base', help='Базовая валюта', default='RUB')
    parser.add_argument('-t', '--target', help='Целевая валюта', default='USD')
    parser.add_argument('-a', '--amount', type=float, help='Сумма', default='1000')
    args = parser.parse_args()
    try:
        exchange_rates = get_exchange_rates(token, args.base)
        print('Конвертированная валюта: ', convert_amount(args.amount, exchange_rates, args.target))
    except HTTPError as err:
        if err.code == 404:
            print('CCЫЛКА НЕ НАЙДЕНА!')
        else:
            raise ValueError('ЦЕЛЕВАЯ ВАЛЮТА НЕДОСТУПНА')


if __name__ == '__main__':
    main()

import os
import requests
import argparse
from dotenv import load_dotenv


def get_exchange_rates(token, base_currency):
    exchange_rates_url = f'https://v6.exchangerate-api.com/v6/{token}/latest/{base_currency}'
    response = requests.get(exchange_rates_url)
    response.raise_for_status()
    exchange_rates = response.json()['conversion_rates']
    return exchange_rates


def convert_amount(amount_money, exchange_rates, target_exchange_rates):
    target_rates = exchange_rates[target_exchange_rates]
    print(target_rates)
    convertible_currency = amount_money * target_rates
    return convertible_currency


def main():
    load_dotenv()
    token = os.getenv('API_KEY')
    # base_currency = input('Введите код базовой валюты: ').upper()
    # target_currency = input('Введите код целевой валюты: ').upper()
    # amount_money = float(input('Введите сумму: '))
    parser = argparse.ArgumentParser(description='Ввести валюты')
    parser.add_argument('-b', '--base', help='Базовая валюта', default='RUB')
    parser.add_argument('-t', '--target', help='Целевая валюта', default='USD')
    parser.add_argument('-a', '--amount', type=int, help='Сумма', default='1000')
    args = parser.parse_args()
    print(args)
    # exchange_rates = get_exchange_rates(token, base_currency)
    # print(convert_amount(amount_money, exchange_rates, target_currency))


if __name__ == '__main__':
    main()

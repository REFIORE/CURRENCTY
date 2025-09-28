import os
import requests

api_key = '7fec70a40ce6aaf16cd4caa5'
token = os.getenv(api_key)
base_currency = input('Какую валюту вы хотит выбрать? ').upper()


def get_exchange_rates(token, base_currency):
    exchange_rates_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    response = requests.get(exchange_rates_url)
    response.raise_for_status()
    exchange_rates = response.json()['conversion_rates']
    return exchange_rates


def get_target_exchange_rates(base_currency):
    target_currency = input('Впишите целевую валюту: ').upper()
    exchange_rates_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    response = requests.get(exchange_rates_url)
    response.raise_for_status()
    target_exchange_rates = response.json()['conversion_rates'][target_currency]
    return target_exchange_rates


def main():
    print(get_exchange_rates(token, base_currency))
    print(get_target_exchange_rates(base_currency))


if __name__ == '__main__':
    main()

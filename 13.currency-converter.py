import json
import requests

def currency(from_currency, to_currency):
    base_url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}"
    
    response = requests.get(base_url)
    data = response.json()
    
    if from_currency in data['rates'] and to_currency in data['rates']:
        from_rate = data['rates'][from_currency]
        to_rate = data['rates'][to_currency]
        exchange_rate = to_rate / from_rate
        
        amount = float(input(f"Enter the amount in {from_currency}: "))
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} is {converted_amount} {to_currency}.")

from_currency = input("input from currency : ")
to_currency = input("input to currency : ")  
currency(from_currency, to_currency)

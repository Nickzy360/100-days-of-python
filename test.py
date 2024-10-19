import json
import requests

def currency(from_currency, to_currency):
    base_url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}.json"
    
    response = requests.get(base_url)
    
    if response.status_code != 200:
        print("Error fetching data from the API.")

    data = response.json()
    
    if from_currency in data and to_currency in data[from_currency]:
        print(data[from_currency[to_currency]] )

        


from_currency = input("Input from currency (e.g., USD): ").lower()  
to_currency = input("Input to currency (e.g., EUR): ").lower()    
#currency(from_currency, to_currency)
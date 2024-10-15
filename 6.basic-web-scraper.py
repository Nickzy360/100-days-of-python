import requests
URL = input("input a valid URL: ")
page = requests.get(URL)
print(page.text)
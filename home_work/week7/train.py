import requests
try:
    r = requests.get('http://yax.ru/h/?text=%D0%BC%D0%B2186620')
    print(r.text)
except requests.exceptions.ConnectionError:
    print("Connection so long")
except requests.exceptions.InvalidSchema:
    print("Invalid")

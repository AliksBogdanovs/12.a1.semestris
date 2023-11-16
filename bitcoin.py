import requests
import json
URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

bitcoin = requests.get(URL)
print(json.dumps(bitcoin.json(),indent=2))
cena = bitcoin.json()['bpi']['USD']['rate_float']

input = float(input('ievadi cik gribi nopirkt: '))

print(cena * input)

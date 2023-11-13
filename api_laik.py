#Laika noteikšana

import requests

URL = "http://worldtimeapi.org/api/timezone/Europe/Riga"  

dati = requests.get(URL)

print(dati)

laiksLatvija = dati.json()

print(laiksLatvija)

print(laiksLatvija["utc_datatime"])

#ASV laiks,Ņujorka
URL2 = "http://worldtimeapi.org/api/timezone/America/New_York"
dati2 = requests.get(URL2)
print(dati2)
laiksNewYork = dati2.json()
print(laiksNewYork)
print(laiksNewYork["datetime"])

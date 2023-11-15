import requests
import json
URL ="https://itunes.apple.com/search?entity=song&limit=1&term=weezer"

atbilde = requests.get(URL)

print(atbilde)

dati = atbilde.json()

print(json.dumps(dati,indet = 2))

print(dati["results"][0]["trackName"])

#izveido veidu,kā var iegut jebkādu skaitu ar dziesmu nosaukumiem.

for a in dati["results"]:
    nosaukums = a["trackName"]
    print(nosaukums)

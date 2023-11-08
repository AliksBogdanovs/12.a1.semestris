#Datu kriptēšana

from cryptography.fernet import fernet

atslega = fernet.generate_key()

print(atslega)

a = Fernet(atslega) #objekta izveide

teksts = b'slepeni dati'

kripDati = a.encrypt(teksts) #Metodes encrypt izmantošana

print(kriptDati)

print(a.decrypt(kriptDati)) #Metodes decrypt izmantošana

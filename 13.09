
#minimalas prasibas
class datora_sastavdala():
    #konstruktors
    def __init__(self, veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    #informacijas apskate
    def izdrukat(self):
        print("Veids: ", self.veids)
        print("Modelis: ", self.modelis)
        print("Cena: ", self.cena)
    
    def labosana(self,veids,modelis,cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    def saglabat(self):
        with open('sastavdalas.txt', 'w', encoding="utf-8") as fails :
            fails.write("-datora sastāvdaļas-")
            fails.write(" \n")
            fails.write(str(dators.veids))
            fails.write(" \n")
            fails.write(str(dators.modelis))
            fails.write(" \n")
            fails.write(str(dators.cena))

dators = datora_sastavdala(veids='RAM',modelis= 'Corsair Vengeance LPX 16GB',cena= '99,99 EUR')
dators.izdrukat()
dators.labosana(veids= input("ievadi veidu: "), modelis= input("ievadi modeli: "), cena= input("ievadi cenu: "))
dators.izdrukat()

#datu saglabašana

dators.saglabat()

import PySimpleGUI as psg

psg.theme('DarkAmber')
layout = [[psg.Text('Komponents')]]

layout2 = [[psg.Text('Rediģēšana')]]

tabgrp = [
    psg.TabGroup(
        [
            
        ]
    )
]

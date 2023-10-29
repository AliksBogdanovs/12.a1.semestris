class Sastavdala():
   
    def __init__(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    #Datu izvade
    def apskate(self):
        print(self.veids)
        print(self.modelis)
        print(self.cena)
    #Datu labošana
    def labosana(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    #Datu saglabāšana
    def saglabat(self):
        with open('sastavdalas.txt','w',encoding="utf-8") as fails:
            fails.write(self.modelis)

import PySimpleGUI as psg

psg.theme('DarkAmber')
logs = [
          [psg.Text('Komponentes')],
          [psg.Text('Veids'),psg.InputText()],
          [psg.Text('Modelis'),psg.InputText()],
          [psg.Text('Cena'),psg.InputText()],
          [psg.Button('Saglabāt')]
          ]
logs2 = [[psg.Text("Rediģēšana")],
         [psg.Text('Veids'),psg.InputText()],
          [psg.Text('Modelis'),psg.InputText()],
          [psg.Text('Cena'),psg.InputText()],
          [psg.Button('Rediģēt')]]
#Grupēsim divus logus
loguGrupa = [[
    [psg.TabGroup(
        [
            [
                psg.Tab('Datu ievade',logs),
                psg.Tab('Datu rediģēšana',logs2)
            ]
        ]
    )],
    [psg.Button('Aizvērt'),
    psg.Button('Datu apskate')]
]]
window = psg.Window('Datora komponentes', loguGrupa)
#Pārbauda notikumus grafiskajā saskarnē
while True:
    event,values = window.read() #Nolasa ievadītās vērtības un darbības
    #Apgalvojumi
    if event == "Saglabāt":
        print(values) 
        veids = values[0]
        modelis = values[1]
        cena = values[2]
        jauns = Sastavdala(veids,modelis,cena)
        jauns.saglabat()
    if event == "Rediģēt":
        veids = values[3]
        modelis = values[4]
        cena = values[5]
        jauns.labosana(veids,modelis,cena)
        jauns.saglabat()
    if event == "Datu apskate":
        psg.theme("BlueMono")
        layout = [
                  [psg.Text("Esošās komponentes")],
                  [psg.Text("Veids: " + values[0])],
                  [psg.Text("Modelis: " + values[1])],
                  [psg.Text("Cena: " + values[2])]
                  ]
        window = psg.Window('',layout)
        event,values = window.read()
    if event in (psg.WIN_CLOSED,'Aizvērt'):
        break

window.close()

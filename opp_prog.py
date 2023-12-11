import PySimpleGUI as ps

class Salons():
    def __init__(self):
        self.klienta_vards = ""
        self.klienta_uzvards = ""
        self.klienta_mobilais = ""
        self.skaistumkopsanas_cena = ""
        self.skaistumkopsanas_mobilais = ""
        self.skaistumkopsanas_pieteikuma_datums = ""
    def skaistumkopsana_Save(self):
        with open('Skaistumkopsana.txt','w',encoding="utf-8") as fails:
            fails.write('=Skaistumkopšana=\n')
            fails.write(f'Klienta vārds:{self.klienta_vards}\n')
            fails.write(f'Klienta uzvārds:{self.klienta_uzvards}\n')
            fails.write(f'Klienta mobilais:{self.klienta_mobilais}\n')
            fails.write(f'Skaistumkopšanas terapijas cena:{self.skaistumkopsanas_cena} EUR\n')
            fails.write(f'Skaistumkopšanas salona mobilais:{self.skaistumkopsanas_mobilais}\n')
            fails.write(f'Skaistumkopšanas pieteikuma datums:{self.skaistumkopsanas_pieteikuma_datums}\n')

    def skaistumkopsana_info_print(self):
        print(self.klienta_vards)
        print(self.klienta_uzvards)
        print(self.klienta_mobilais)
        print(f'{self.skaistumkopsanas_cena} EUR')
        print(self.skaistumkopsanas_mobilais)
        print(self.skaistumkopsanas_pieteikuma_datums)
    
    def interface(self):
        ps.theme('Black')

        layout =[

                [ps.Text('Ievadi klienta datus')],
                [ps.Text('Klienta vārds'),ps.InputText()],
                [ps.Text('Klienta uzvārds'),ps.InputText()],
                [ps.Text('Telefona numurs'),ps.InputText()],
                [ps.Text('Skaistumkopšanas cena'),ps.InputText()],
                [ps.Text('Skaistumkopšanas Tālrunis'),ps.InputText()],
                [ps.Text('Skaistumkopšanas Pieteikuma Datums'),ps.InputText()],
                [ps.Button('Apstiprināt'), ps.Button('Saglabāt'), ps.Button('Apskatīt datus'), ps.Button('Beigt')]
                ]
        window = ps.Window('Skaistumkopsana', layout)

        while True:
            event,values = window.read()

            if event in (ps.WINDOW_CLOSED,'Beigt'):
                break
            
            # work in progress
            if event == 'Apstiprināt':
                self.klienta_vards = values[0]
                self.klienta_uzvards = values[1]
                self.klienta_mobilais = values[2]
                self.skaistumkopsanas_cena = values[3]
                self.skaistumkopsanas_mobilais = values[4]
                self.skaistumkopsanas_pieteikuma_datums = values[5]
            
            if event == "Saglabāt":
                self.skaistumkopsana_Save()

            if event == 'Apskatīt datus':
                ps.theme("Black")
                layout2 = [
                            [ps.Text("Apskatīt datus")],
                            [ps.Text(self.klienta_vards)],
                            [ps.Text(self.klienta_uzvards)],
                            [ps.Text(self.klienta_mobilais)],
                            [ps.Text(f'{self.skaistumkopsanas_cena} EUR')],
                            [ps.Text(self.skaistumkopsanas_mobilais)],
                            [ps.Text(self.skaistumkopsanas_pieteikuma_datums)]
                        ]
                window2 = ps.Window('',layout2)
                self.skaistumkopsana_info_print()
                while True:
                    event,values = window2.read()
                    if event in (ps.WIN_CLOSED,):
                        break
        window.close()

SkaistumkopsanasSalons = Salons().interface()
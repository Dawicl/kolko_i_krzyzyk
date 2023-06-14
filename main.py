plansza = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

def plansza_do_gry():
    
    print(plansza[0][0], "|", plansza[0][1], "|", plansza[0][2])
    print("---------")
    print(plansza[1][0], "|", plansza[1][1], "|", plansza[1][2])
    print("---------")
    print(plansza[2][0], "|", plansza[2][1], "|", plansza[2][2])

def kolko():
    print("Kolej Gracza 1: O")
    lista_temp = input("Podaj pole w które chcesz wstawić znak: ").split(sep=',')
    a = int(lista_temp[0])
    b = int(lista_temp[1])
    plansza[a][b] = "O"
    

def krzyzyk():
    print("Kolej Gracza 2: X")
    lista_temp = input("Podaj pole w które chcesz wstawić znak: ").split(sep=',')
    a = int(lista_temp[0])
    b = int(lista_temp[1])
    plansza[a][b] = "X"

while True:
    plansza_do_gry()
    kolko()
    plansza_do_gry()
    krzyzyk()
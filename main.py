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

def sprawdzenie():
    a1 = plansza[0][0]
    a2 = plansza[0][1]
    a3 = plansza[0][2]
    b1 = plansza[1][0]
    b2 = plansza[1][1]
    b3 = plansza[1][2]
    c1 = plansza[2][0]
    c2 = plansza[2][1]
    c3 = plansza[2][2]
    
    if a1 == a2 and a2 == a3:
        print("Koniec gry!")
        return True
    elif b1 == b2 and b2 == b3:
        print("Koniec gry!")
        return True
    elif c1 == c2 and c2 == c3:
        print("Koniec gry!")
        return True
    else:
        return False

while True:
    plansza_do_gry()
    kolko()
    plansza_do_gry()
    if sprawdzenie() == True:
        break
    krzyzyk()
    plansza_do_gry()
    if sprawdzenie() == True:
        break
    
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
    for i in range(0, 3):
        if plansza[i][0] == plansza[i][1] and plansza[i][0] == plansza[i][2] and plansza[i][0] !=' ':
            print("Koniec gry!")
            return True
        
        elif plansza[0][i] == plansza[1][i] and plansza[0][i] == plansza[2][i] and plansza[0][i] !=' ':
            print("Koniec gry!")
            return True

    if plansza[0][0] == plansza[1][1] and plansza[0][0] == plansza[2][2] and plansza[0][0] !=' ':
        print("Koniec gry!")
        return True
        
    elif plansza[2][0] == plansza[1][1] and plansza[2][0] == plansza[0][2] and plansza[2][0] !=' ':
        print("Koniec gry!")
        return True

plansza_do_gry()

while True:
    kolko()
    if sprawdzenie() == True:
        break
    plansza_do_gry()
    krzyzyk()
    if sprawdzenie() == True:
        break
    plansza_do_gry()

plansza_do_gry()
    
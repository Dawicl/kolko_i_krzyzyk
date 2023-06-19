plansza = []

def budowanie_planszy():
    rozmiar = int(input("Podaj rozmiar planszy: "))
    for _ in range(rozmiar):
        temp = []
        for _ in range(rozmiar):
            temp.append(' ')
        plansza.append(temp)

def plansza_do_gry():
    for j in range(len(plansza)):
        for i in range(len(plansza)):
            if i == len(plansza) - 1:
                print(plansza[j][i])
            else:
                print(plansza[j][i], "|", end="")       
        if j == len(plansza) - 1:
            continue
        else:
            print("---"*len(plansza))

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
    for i in range(0, len(plansza)):
        for j in range(0, len(plansza)):
            if plansza[j][0] == plansza[j][len(plansza) -1] and plansza[j][0] == plansza[j][1] and plansza[j][0] != " ":
                print("Koniec gry!")
                return True
            elif plansza[0][j] == plansza[len(plansza) -1][j] and plansza[0][j] == plansza[1][j] and plansza[0][j] != " ":
                print("Koniec gry!")
                return True
        
    #         elif plansza[0][i] == plansza[1][i] and plansza[0][i] == plansza[2][i] and plansza[0][i] !=' ':
    #             print("Koniec gry!")
    #             return True

    # if plansza[0][0] == plansza[1][1] and plansza[0][0] == plansza[2][2] and plansza[0][0] !=' ':
    #     print("Koniec gry!")
    #     return True
        
    # elif plansza[2][0] == plansza[1][1] and plansza[2][0] == plansza[0][2] and plansza[2][0] !=' ':
    #     print("Koniec gry!")
    #     return True

budowanie_planszy()
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
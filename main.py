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
    if plansza[a][b] == " ":
        plansza[a][b] = "O"
    elif plansza[a][b] == "X":
        print("To pole jest zajęte!")
        lista_temp = input("Podaj pole w które chcesz wstawić znak: ").split(sep=',')
        a = int(lista_temp[0])
        b = int(lista_temp[1])
        plansza[a][b] = "O"

def krzyzyk():
    print("Kolej Gracza 2: X")
    lista_temp = input("Podaj pole w które chcesz wstawić znak: ").split(sep=',')
    a = int(lista_temp[0])
    b = int(lista_temp[1])
    if plansza[a][b] == " ":
        plansza[a][b] = "X"
    elif plansza[a][b] == "O":
        print("To pole jest zajęte!")
        lista_temp = input("Podaj pole w które chcesz wstawić znak: ").split(sep=',')
        a = int(lista_temp[0])
        b = int(lista_temp[1])
        plansza[a][b] = "X"

def sprawdzenie():
    for i in range(0, len(plansza)):
        if len(set(plansza[i])) == 1 and plansza[i][0] != " ":
            print("Koniec gry!")
            return True
    temp = []
    for i in range(0, len(plansza)):
        temp.append(plansza[i][0])
    if len(set(temp)) == 1 and temp[0] != " ":
        print("Koniec gry!")
        return True
    
    temp_2 = []
    for i in range(0, len(plansza)):
        temp_2.append(plansza[i][i])
    if len(set(temp_2)) == 1 and temp[0] != " ":
        print("Koniec gry!")
        return True
    
    
        
    return False

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
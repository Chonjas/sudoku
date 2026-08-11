import numpy as np
import json
import sys
def quit(wg):
    data = read_json()
    data["wg"] = wg.tolist()
    save_json(data)
    sys.exit()
def back_to_menu(wg):
    data = read_json()
    data["wg"] = wg.tolist()
    save_json(data)
    main()
def pr_field(array):
    print("")
    print("   1 2 3   4 5 6   7 8 9")
    print("")
    for i in range(9):
        print(i+1," ",end="")
        for j in range(9):
            if array[i][j] == 0:
                print("-", end=" ")
            elif array[i][j] > 0 and array[i][j] < 10:
                print(int(array[i][j]),end=" ")
            if j == 2 or j == 5:
                print("|",end=" ")
            elif j == 8:
                print("")
        if i == 2 or i == 5:
            print("   ---------------------")
    print("")
def is_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
def innitnd2():
    wg = np.zeros([9,9])
    wg[0] = [7,5,4, 0,9,3, 2,6,1]
    wg[1] = [3,1,8, 2,6,4, 7,9,5]
    wg[2] = [6,9,2, 1,7,5, 8,4,3]
    wg[3] = [9,2,3, 4,8,7, 1,5,6]
    wg[4] = [1,4,8, 6,5,2, 3,7,9]
    wg[5] = [5,7,6, 9,3,1, 4,2,8]
    wg[6] = [2,3,7, 5,1,6, 9,8,4]
    wg[7] = [1,8,5, 7,4,9, 6,3,2]
    wg[8] = [4,6,9, 3,2,8, 5,1,7]
    return wg
def innitnd1():
    wg = np.zeros([9,9])
    wg[0] = [0,0,4, 0,9,3, 0,0,0]
    wg[1] = [3,0,0, 0,6,0, 0,9,5]
    wg[2] = [6,0,2, 0,7,0, 0,0,0]
    wg[3] = [0,0,0, 4,8,0, 1,5,6]
    wg[4] = [8,0,0, 6,5,2, 0,7,0]
    wg[5] = [5,0,0, 0,0,1, 4,0,0]
    wg[6] = [0,3,0, 0,0,0, 9,0,4]
    wg[7] = [1,8,0, 7,0,0, 0,0,2]
    wg[8] = [0,0,9, 0,0,0, 5,0,0]
    wg = wg.astype(int)
    return wg
def inpuut(wg):
    while True:
        zeile = input("Zeile: ")
        if is_int(zeile):
            zeile = int(zeile) -1
            if zeile >= 0 and zeile <= 8:
                break
        elif zeile == "q":
            quit(wg)
        elif zeile == "m":
            back_to_menu(wg)

    while True:
        spalte = input("Spalte: ")
        if is_int(spalte):
            spalte = int(spalte) -1
            if spalte >= 0 and spalte <= 8:
                        break
        elif spalte == "q":
            quit(wg)
        elif spalte == "m":
            back_to_menu(wg)

    while True:
        eingabe = input("Eingabe: ")
        if is_int(eingabe):
            eingabe = int(eingabe)
            if eingabe >= 0 and eingabe < 10:
                        break
        elif eingabe == "q":
            quit(wg)
        elif eingabe == "m":
            back_to_menu(wg)
        else:
            eingabe = 0
            break
    if eingabe == 0:
        wg[zeile,spalte] = 0
        pr_field(wg)
    else:
        wg[zeile,spalte] = eingabe
    return wg
def checkkk(wg): #dead
    for i in range(9):
        for j in range(9):  # 2. for schleife unnötig? vllt fehler
            if any((2 * x) in set(wg[i]) for x in wg[i]) == False:
                print(f"Fehlerhafte Eingabe in Zeile {i+1}")
                check1 = False
            elif any((2 * x) in set(wg[i]) for x in wg[i]) == True:
                if any((2 * x) in set(wg[:,i]) for x in wg[i]) == False:
                    print(f"Fehlerhafte Eingabe in Spalte {i+1}")
                elif any((2 * x) in set(wg[:,i]) for x in wg[i]) == True:
                    check1 = True
    for m in range(3):
        for n in range(3):
            wg_kl = wg[m*3:m*3+3,n*3:n*3+3]
            wg_kl = wg_kl.flatten()
            check2_kl = any((2 * x) in set(wg_kl) for x in wg_kl)
            if check2_kl == True:
                print(f"Fehler im 3x3 Grid Zeile {m+1} und Spalte {n+1}")
                check2 = False
    if check1 == True and check2 == True:
        check = True
    else:
        check = False
    return check
def checkk(wg): #muss ausgetauscht werden, ganzes feld mit 5en füllen kommt als korrekt raus
    check1 = np.zeros([9,1], dtype=bool)
    check2 = np.zeros([9,1], dtype=bool)
    check3 = np.zeros([3,3], dtype=bool)
    for i in range(9):
        if np.sum(wg[i,:]) == 45:
            check1[i] = True
        else:
            print(f"Fehler in Zeile {i+1}")
    for i in range(9):
        if np.sum(wg[:,i]) == 45:
            check2[i] = True
        else:
            print(f"Fehler in Spalte {i+1}")
    for m in range(3):
        for n in range(3):
            wg_kl = wg[m*3:m*3+3,n*3:n*3+3]
            if np.sum(wg_kl) == 45:
                check3[m,n] = True
            else:
                print(f"Fehler in 3x3 Grid {m+1}, {n+1}")
    if check1.all() == True and check2.all() == True and check3.all() == True:
        check = 1
    else:
        check = 0
    return check
def save_json(data):
    with open("settings.json", "w") as file:
        json.dump(data, file)
def read_json():
    with open("settings.json", "r") as file:
        data = json.load(file)
    return data
def difficulty():
    data = read_json()
    print(f"Momentares Schwierigkeitslevel: {data["difficulty"]}\n")
    print("1 Leicht")
    print("2 Mittel")
    print("3 Schwer")
    while True:
        schwierigkeit = input("Neue Schwierigkeit: ")
        if is_int(schwierigkeit):
            schwierigkeit = int(schwierigkeit)
            if schwierigkeit >= 1 and schwierigkeit <= 3:
                        break
        elif schwierigkeit == "q":
            sys.exit()
        elif schwierigkeit == "m":
            main()
    print("hehe schwierigkeit ändern geht noch nicht lol")
    data["difficulty"] = schwierigkeit
    save_json(data)
def reset_all():
    data = read_json()
    data["counter"] = 0
    data["difficulty"] = 1
    wg = np.zeros([9,9])
    wg = wg.astype(int)
    data["wg"] = wg.tolist()
    save_json(data)
def reset_wg():
    data = read_json()
    wg = np.zeros([9,9])
    wg = wg.astype(int)
    data["wg"] = wg.tolist()
    save_json(data)
def menu():
    print("\nSudoku Menu\n")
    print("Willst du:")
    print("1 Neues Spiel starten")
    print("2 Letztes Spiel vortsetzen")
    print("3 Schwierigkeit ändern")
    print("4 Daten zurücksetzen")
    print("m Zum Menu zurück gelangen (geht immer)")
    print("q Spiel beenden (geht immer)")

    while True:
        wahl = input("Wahl:")
        print("")
        if is_int(wahl):
            menu_wahl = int(wahl)
            if menu_wahl == 3:
                difficulty()
                main()
            elif menu_wahl == 4:
                reset_all()
                main()
            elif menu_wahl > 0 and menu_wahl <=4:
                break
        elif wahl == "q":
            sys.exit()

    return menu_wahl

def valid_num(wg, zeile, spalte, num):
    if num in wg[zeile, :]:
        return False
    if num in wg[:, spalte]:
        return False
    start_zeile = (zeile//3)*3
    start_spalte = (spalte//3)*3
    wg_kl = wg[start_zeile:start_zeile+3, start_spalte:start_spalte+3]
    if num in wg_kl:
        return False
    return True
def solve_sudoku(wg):
    for i in range(9):
        for j in range(9):
            if wg[i,j] == 0:
                zahlen = np.arange(1,10)
                np.random.shuffle(zahlen)
                for num in zahlen:
                    if valid_num(wg, i, j, num):
                        wg[i,j] = num
                        if solve_sudoku(wg):
                            return True
                        wg[i,j] = 0
                return False
    return True
def gen_sudoku():
    data = read_json()
    diff = data["difficulty"]
    wg = np.zeros([9,9], dtype=int)
    solve_sudoku(wg)
    return wg









def main():
    wahl = menu()
    data = read_json()

    print(f"Erfolgreiche versuche: {data["counter"]}")
    if wahl == 1:
        wg = gen_sudoku()
    elif wahl == 2:
        wg = np.array(data["wg"])
    pr_field(wg)



    while True: # Game
        wg = inpuut(wg)
        pr_field(wg)
        if np.all(wg != 0):
            check = checkk(wg)
            if check == 1:
                print("Eyyy alles richtig!!")
                data["counter"] = data["counter"] + 1
                reset_wg()
                save_json(data)
                break
            if check == 0:
                pr_field(wg)



if __name__ == "__main__":
    main()
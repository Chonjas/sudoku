import numpy as np
import json
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
def innitnd():
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
def innit():
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
    while True:
        spalte = input("Spalte: ")
        if is_int(spalte):
            spalte = int(spalte) -1
            if spalte >= 0 and spalte <= 8:
                        break
    while True:
            eingabe = input("Eingabe: ")
            if is_int(eingabe):
                eingabe = int(eingabe)
                if eingabe >= 0 and eingabe < 10:
                            break
            else:
                eingabe = 0
                break
    if eingabe == 0:
        wg[zeile,spalte] = 0
        pr_field(wg)
    else:
        wg[zeile,spalte] = eingabe
        pr_field(wg)
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
def checkk(wg):
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
    file_path = "settings.json"
    with open("settings.json", "w") as file:
        json.dump(data, file)
def read_json():
    file_path = "settings.json"
    with open("settings.json", "r") as file:
        data = json.load(file)
    return data
    

def main():
    data = read_json()
    counter = data["counter"]
    print(f"Erfolgreiche versuche: {counter}")
    wg = innitnd()
    pr_field(wg)
    while True:
        wg = inpuut(wg)
        if np.all(wg != 0):
            check = checkk(wg)
            if check == 1 or check == 0:
                print("Eyyy alles richtig!!")
                counter = counter + 1
                data["counter"] = counter
                save_json(data)
                break
            if check == 0:
                pr_field(wg)



if __name__ == "__main__":
    main()
import numpy as np
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
def is_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
def innit():
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
    pr_field(wg)
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
def checkk(wg):
    for i in range(9):
        for j in range(9):
            if any((2 * x) in set(wg[i]) for x in wg[i]) == True:
                print(f"Fehlerhafte Eingabe in Zeile {i+1}")
                check1 = False
            elif any((2 * x) in set(wg[i]) for x in wg[i]) == False:
                if any((2 * x) in set(wg[:,i]) for x in wg[i]) == True:
                    print(f"Fehlerhafte Eingabe in Spalte {i+1}")
                elif any((2 * x) in set(wg[:,i]) for x in wg[i]) == False:
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



def main():
    wg = innit()
    while True:
        wg = inpuut(wg)
        if np.all(wg != 0):
            check = checkk(wg)
            if check == True:
                print("Eyyy alles richtig!!")
                break
            if check == False:
                pr_field(wg)



if __name__ == "__main__":
    main()
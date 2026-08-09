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
    wg[0] = [7,5,4, 0,9,3, 2,0,0]
    wg[1] = [3,1,8, 0,6,0, 0,9,5]
    wg[2] = [6,9,2, 0,7,0, 0,0,0]
    wg[3] = [9,2,3, 4,8,7, 1,5,6]
    wg[4] = [1,4,8, 6,5,2, 3,7,9]
    wg[5] = [5,7,6, 9,3,1, 4,2,8]
    wg[6] = [2,3,7, 0,1,0, 9,0,4]
    wg[7] = [1,8,5, 7,4,9, 0,0,2]
    wg[8] = [4,6,9, 0,2,0, 5,0,7]
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
        if np.equal(wg[zeile], eingabe).any() == True:
            print("Fehlerhafte Eingabe")
            pr_field(wg)
        elif np.equal(wg[zeile], eingabe).any() == False:
            if np.equal(wg[:, spalte], eingabe).any() == True:
                print("Fehlerhafte Eingabe")
                pr_field(wg)
            elif np.equal(wg[:, spalte], eingabe).any() == False:
                wg[zeile][spalte] = eingabe
                pr_field(wg)
            else:
                print("Fehler 2.if")
        else:
            print("Fehler 1. if")
    return wg
def check(wg):
    for i in range(9):
        for j in range(9):
            if np.equal(wg[i], j + 1).any() == True:
                print(f"Fehlerhafte Eingabe in Zeile {i+1}")
                pr_field(wg)
                check = False
            elif np.equal(wg[i], j + 1).any() == False:
                if np.equal(wg[:, i], j + 1).any() == True:
                    print(f"Fehlerhafte Eingabe in Spalte {i+1}")
                    pr_field(wg)
                elif np.equal(wg[:, i], j + 1).any() == False:
                    pr_field(wg)
                    check = True
                else:
                    print("Fehler 2.if")
            else:
                print("Fehler 1. if")
    return check



def main():
    wg = innit()
    while True:
        wg = inpuut(wg)
        if np.all(wg != 0):
            check = check(wg)
            if check == True:
                print("Eyyy alles richtig!!")
                break



if __name__ == "__main__":
    main()
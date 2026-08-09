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
    pr_field(wg)
    return wg
def inpuut(wg):
    zeile = int(input("Zeile: ")) - 1
    spalte = int(input("Spalte: ")) - 1
    eingabe = int(input("Eingabe: "))
    if eingabe == 0:
        wg[zeile,spalte] = 0
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
def main():
    wg = innit()
    while True:
        wg = inpuut(wg)



if __name__ == "__main__":
    main()
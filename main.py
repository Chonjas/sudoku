import numpy as np
def pr_field(array):
    print("")
    print("   1 2 3   4 5 6   7 8 9")
    print("")
    for i in range(9):
        print(i+1," ",end="")
        for j in range(9):
            print(int(array[i][j]),end=" ")
            if j == 2 or j == 5:
                print("|",end=" ")
            elif j == 8:
                print("")
        if i == 2 or i == 5:
            print("   ---------------------")
def main():
    wg = np.zeros([9,9])
    for i in range(9):
        wg[i] = i
    pr_field(wg)
    while True:
        zeile = int(input("Zeile: ")) - 1
        spalte = int(input("Spalte: ")) - 1
        print(wg[:, spalte])
        eingabe = int(input("Eingabe: "))
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



if __name__ == "__main__":
    main()
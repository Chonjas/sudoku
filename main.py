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
    wg[1] = 1
    wg[3] = 3
    pr_field(wg)

if __name__ == "__main__":
    main()
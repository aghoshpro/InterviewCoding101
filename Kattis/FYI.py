import fileinput
import os
os.system("cls")

data = [(f.strip().split("\t")) for f in fileinput.input("D:\Git-Space\PracticeCoding101\Kattis\input.txt")]

strinG= data[0][0]

if 1000000<= int(strinG) <= 9999999:
    if strinG[0:3] == "555":
        print(1)
    else:
        print(0)
import fileinput
import os
os.system("cls")

data = [(f.strip().split("\t")) for f in fileinput.input("D:\Git-Space\PracticeCoding101\Kattis\input.txt")]

strinG= data[0][0]
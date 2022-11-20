import fileinput
import os
os.system("cls")

data = [(f.strip().split("\t")) for f in fileinput.input("D:\Git-Space\PracticeCoding101\Kattis\input.txt")]

strinG= data[0][0]
result = ""

print(strinG.split("-")[2])
print(len(strinG.split("-")))

for x in range(0, len(strinG.split("-"))):
    result = result + strinG.split("-")[x][0]

print(result)

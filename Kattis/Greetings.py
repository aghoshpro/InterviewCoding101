import fileinput
import os
os.system("cls")

data = [(f.strip().split("\t")) for f in fileinput.input("D:\Git-Space\PracticeCoding101\Kattis\input.txt")]

strinG= data[0][0]
print(strinG)
# if 3<=len(strinG)<=1000:
#     print(strinG[0] + str(2*))

print(strinG[0])
print(strinG[-1])
print(strinG[1:len(strinG)-1])

print(strinG[0]+2*strinG[1:len(strinG)-1]+strinG[-1])
import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input("D:\Git-Space\PracticeCoding101\Kattis\Tarifa.txt")]

# convert str to int
GBmonth = list(map(int, data[0][0].split(" ")))[0]
months = list(map(int, data[1][0].split(" ")))[0]

remain = GBmonth - list(map(int, data[2][0].split(" ")))[0]

for x in range(3,len(data)):
    remain = remain + GBmonth - list(map(int, data[x][0].split(" ")))[0]

print(remain+GBmonth)


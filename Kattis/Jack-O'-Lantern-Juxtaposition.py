import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input("Z:\Git_PhD\PracticeCoding101\Kattis\Jack-O'-Lantern-Juxtaposition.txt")]

# Convert the data into integer
dataINT = list(map(int, data[0][0].split(" ")))

num01 = dataINT[0]
num02 = dataINT[1]
num03 = dataINT[2]

result = num01 * num02 * num03
print(result)
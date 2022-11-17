import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input("Z:\Git_PhD\PracticeCoding101\Kattis\sumSUM.txt")]

# Convert the data into integer
dataINT = list(map(int, data[0][0].split(" ")))

a = max(dataINT)
b = min(dataINT)

sum = a + b

print(sum)
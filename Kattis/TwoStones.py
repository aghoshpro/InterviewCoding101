import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input("D:\Git-Space\PracticeCoding101\Kattis\TwoStones.txt")]

# Convert the data into integer
dataINT = list(map(int, data[0][0].split(" ")))

numberOfStones = dataINT[0]

if numberOfStones%2 == 1:
    print("Alice")
else:
    print("Bob")

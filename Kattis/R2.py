import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input("Z:\Git_PhD\PracticeCoding101\Kattis\R2.txt")]

# Convert the data into integer
dataINT = list(map(int, data[0][0].split(" ")))

R1 = dataINT[0]
S = dataINT[1]

R2 = 0

if -1000<=S<=1000 and -1000<=R1<=1000:
   R2 = 2*S - R1

print(R2)
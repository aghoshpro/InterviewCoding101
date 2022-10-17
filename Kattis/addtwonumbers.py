import fileinput
# line = input()
# print(line)
# data = [(f.strip().split(" ")) for f in line]

data = [(f.strip().split("\t")) for f in fileinput.input("Z:\addSum.txt")]
a = int(data[0][0])

# a = int(data[0][0])
# b = int(data[1][0])
# b = int(b)

print(a)
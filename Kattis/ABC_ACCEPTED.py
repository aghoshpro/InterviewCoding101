import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input()]

numSTRING = data[0][0]
abcSTRING = data[1][0]

X = numSTRING.split(" ")
Z = list(map(int, X))

numMIN = min(list(map(int, Z))) 
Z.remove(min(Z))
numMAX = max(list(map(int, Z))) 
Z.remove(max(Z))
middle = max(list(map(int, Z)))

if numMAX <= 100:
    dict = {'A':numMIN,
            'B': middle,
            'C':numMAX}

    if abcSTRING == 'ABC':
        print(dict['A'],dict['B'],dict['C'])
    elif abcSTRING == 'ACB':
        print(dict['A'],dict['C'],dict['B'])
    elif abcSTRING == 'BAC':
        print(dict['B'],dict['A'],dict['C'])
    elif abcSTRING == 'BCA':
        print(dict['B'],dict['C'],dict['A'])
    elif abcSTRING == 'CAB':
        print(dict['C'],dict['A'],dict['B'])
    else:
        print(dict['C'],dict['B'],dict['A'])

    
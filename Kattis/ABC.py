import fileinput
import os
os.system("cls")

data = [(f.strip().split("\t")) for f in fileinput.input("D:\Git-Space\PracticeCoding101\Kattis\ABC.txt")]

numSTRING = data[0][0]
abcSTRING = data[1][0]
X = numSTRING.split(" ")
print(X)

numMAX = max(list(map(int, X))) # string to int
numMIN = min(list(map(int, X)))
middle = list(map(int, X))
print(middle.remove())


# if numMAX <= 100:
#     dict = {'A':numMIN,
#             'B': None,
#             'C':numMAX}
#     print(dict)
#     # print(numSTRING)
#     # stringLis = [1, 2, 3]
#     # print(stringLis)

#     # stringABC = "ABC"
#     # print(stringABC[1])
#     print(X)
#     X.remove(min(X))
#     print(X)
#     X.remove(max(X))
#     print(X)
#     dict['B'] = X[0]

#     if abcSTRING == 'ABC':
#         print(dict['A'],dict['B'],dict['C'])
#     elif abcSTRING == 'ACB':
#         print(dict['A'],dict['C'],dict['B'])
#     elif abcSTRING == 'BAC':
#         print(dict['B'],dict['A'],dict['C'])
#     elif abcSTRING == 'BCA':
#         print(dict['B'],dict['C'],dict['A'])
#     elif abcSTRING == 'CAB':
#         print(dict['C'],dict['A'],dict['B'])
#     else:
#         print(dict['C'],dict['B'],dict['A'])
# else:
#     print("Please enter a number less then 100")

# https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
    
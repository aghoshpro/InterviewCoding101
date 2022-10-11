import random

sum = 0
avgr = 0
count = 0
item = []

# Number of Test Cases
C = random.randint(1,50)
print("C", C)
print("------------------------LENEVO-------------------------------")

# the number of people in the class
for j in range(0,C):
    N = random.randint(1, 1000)
    print("N", N)
    for i in range(0, N):
        item.append(random.randint(1, 100))
        sum = sum+item[i]

    avgr = sum/N
    print(item)
    print("sum, avgr", sum, avgr)
    sum = 0

    for k in item:
       if k>avgr:
        count+=1
    
    item = []
    print("Number of Student above avg", count)
    print("{:.3f}%".format(100.0*count/float(N)))
    count = 0
    print("-----------------END-----------------")
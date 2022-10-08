from audioop import avg
import random

sum = 0
avgr = 0
count = 0
item = []

# Number of Test Cases
C = random.randint(1,5)
print("C", C)
print("-------------------------------------------------------")

# the number of people in the class
for j in range(0,C):
    N = random.randint(1, 5)
    print("N", N)
    for i in range(0,N):
        item.append(random.randint(1, 100))
        sum=sum+item[i]

    avgr = sum/N
    print(item)
    print("sum, avgr", sum, avgr)
    sum = 0

    for k in item:
       print(k)
       if k>avgr:
        count+=1
    
    item = []

    print("count", count)
    # print("int, float",(count/N)*100,float(count/N)*100)
    print("--------------------------")
# Generate a random number between 0 and 9
from audioop import avg
import random

sum = 0
avgr = 0

# Number of Test Cases
C = random.randint(1,5)
print(C)

# the number of people in the class
for j in range(0,C):
    N = random.randint(1, 5)
    # print("N", N)
    for i in range(0,N):
        print(random.randint(1, 100))
        sum+=random.randint(1, 100)

    avgr = sum/N
    
    print(avgr)
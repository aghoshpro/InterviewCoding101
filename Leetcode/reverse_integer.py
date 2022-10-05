count = 0
num=[]
x_inverse = 0
x = 123
print(x)

if pow(-2,31) <= x <= pow(2,31) - 1:
    while x%10!=0:
        num.append(x%10)
        count=count+1  
        x=x/10

for k in num:
        x_inverse+=k*pow(10,count)
        count = count-1




print(x_inverse/10)


#Faster solution------------------------------------
# class Solution:
#     def reverse(self, x: int) -> int:
#          if x > 0:  # handle positive numbers  
#             a =  int(str(x)[::-1])  
#          if x <=0:  # handle negative numbers  
#                 a = -1 * int(str(x*-1)[::-1])  
            
#          mina = -2**31  
#          maxa = 2**31 - 1  
#          if a not in range(mina, maxa):  
#               return 0  
#          else:  
#               return a
#----------------------------------------------------
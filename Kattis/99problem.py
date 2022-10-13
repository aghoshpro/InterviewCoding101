import fileinput

sum = 0
avgr = 0
count = 0
item = []
res = 0    

data = [(f.strip().split("\t")) for f in fileinput.input("Z:\99problem.txt")]
print(data)
N = int(data[3][0])
print("Price of product = " + str(N) + " SEK")

if N>= 1 and N<=10000 and N%100 != 99:
   N_temp = N

   while(N_temp!=0):
      remainder_N = N_temp % 10
      N_temp = N_temp/ 10
      count = count + 1
      print("remainder, N, count", remainder_N, N_temp, count)
   
   if count == 1:
      print(9)
   elif count == 2:
      print(99)
   elif count == 3:
      N_temp = N
      while(N_temp!=0):
         remainder_N = N_temp % 10
         N_temp = N_temp/ 10

      mask = 99 - (N - remainder_N * pow(10, (count-1)))
      if mask > 50:
         print(N - (100 - mask))
      else:
         print(N+mask)
   else:
      print("oops")
   

   # range_in = remainder_N * pow(10, (count-1))
   # # diff1 = N - remainder_N * pow(10, (count-1))
   # # diff2 = remainder_N * pow(10, (count-1)) + 
   # range_out = range_in + pow(10, (count-1))
   # print("range", range_in,"<", N, "<", range_out )
   print("Hurraaaay")

import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input()]

dataINT = list(map(int, data[0][0].split(" ")))

num = dataINT[0]

if 1 <= num <= 100:
   for x in range(1,num+1):
      print(str(x)+" "+"Abracadabra")
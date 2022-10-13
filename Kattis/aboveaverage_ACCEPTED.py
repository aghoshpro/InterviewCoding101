import fileinput

sum = 0
avgr = 0
count = 0
item = []
res = 0    

data = [(f.strip().split("\t")) for f in fileinput.input("Z:\TestAboveAvg.txt")]
C = int(data[0][0])

# res = [int(ele) for ele in data[10][0].split()] # convert list of strings to list of integer 
# print("res", res[0])
# res = 0    

# the number of people in the class
if C>= 1 and C<=50:
    for j in range(1,len(data)):
        res = [int(ele) for ele in data[j][0].split()]
        N = res[0] #int(data[j][0][0])
        if N>= 1 and N<=1000:
            for i in range(1,len(res)):
                item.append(res[i])
                sum=sum+res[i]

        avgr = sum/float(N)

        for k in item:
           if k>avgr:
            count+=1
        
        print(item, sum, avgr, N)
        print("{:.3f}%".format(100.0*count/float(N)))
        item = []
        sum = 0
        count = 0 
        
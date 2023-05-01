import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input("D:\Git-Space\PracticeCoding101\Kattis\input.txt")]

# print(data)
# convert str to int
N = list(map(int, data[0][0].split(" ")))[0]

dict = {-1:"do not advertise",
            0: "does not matter",
            1:"advertise"}

if 1 <= N <= 100:
    for i in range(1, N+1):
        r = list(map(int, data[i][0].split(" ")))[0]
        e = list(map(int, data[i][0].split(" ")))[1]
        c = list(map(int, data[i][0].split(" ")))[2]
        if -1000000<= r <=1000000 and -1000000<= e <=1000000 and 0<=c<=1000000:
            if max(r,e,c) == c:
                print(dict[-1])
            elif e-c > r:
                print(dict[1])
            elif e-c <= r:
                print(dict[0])

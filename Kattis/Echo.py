import fileinput

data = [(f.strip().split("\t")) for f in fileinput.input("Z:\Git_PhD\PracticeCoding101\Kattis\Echo.txt")]
if len(data[0][0]) <= 15:
   print(3*(data[0][0]+" "))

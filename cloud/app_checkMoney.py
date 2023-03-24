import sys
import os

ID = sys.argv[1]
string = "1"
i=1
money = 0
while os.path.isfile("./blockChain/"+str(i)+".txt"):
    with open("./blockChain/"+str(i)+".txt",'r') as f:
        f.readline()
        f.readline()
        for line in f:
            words = line.strip().split(",")
            if words[1] == ID:
                money += int(words[2])
            elif words[0] == ID:
                money -= int(words[2])
    i += 1
print(f'money: {money}')

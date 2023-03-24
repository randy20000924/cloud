import sys
import os

ID = sys.argv[1]
sring = "i"
i = 1
money = 0
while os.path.isfile("./blockChain/" + str(i) + ".txt"):
  with open("./blockChain/" + str(i) + ".txt") as f:
    f.readline()
    f.readline()
    for line in f:
      words = line.strip().split(",")
      if words[1] == ID:
        print(words[0] + " " + words[1] + " " + words[2])
      elif words[0] == ID:
        print(words[0] + " " + words[1] + " " + words[2])
  i += 1
import hashlib
import os

sring = "i"
i = 2
content = ""

with open("./blockChain/1.txt") as f:
  for line in f:
    content += line
  #print(content)
  message = content.encode('utf-8')
  hash_object = hashlib.sha256()
  hash_object.update(message)
  hash_hex = hash_object.hexdigest()
  #print("hash_hex: "+hash_hex)

while os.path.isfile("./blockChain/" + str(i) + ".txt"):
  with open("./blockChain/" + str(i) + ".txt") as f:
    first_line = f.readline()
    shanum = first_line.strip().split(" ")[4]
    #print(shanum)
    if shanum == hash_hex:
      print("no problem")
      for line in f:
        content += line
      print(content)
    else:
      print(content)
      print("the problem is in the " + str(i - 1) + " block")
  with open("./blockChain/" + str(i) + ".txt") as f:
    for line in f:
      content += line
    message = content.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(message)
    hash_hex = hash_object.hexdigest()
  i += 1




import sys
import os
import hashlib

giver = sys.argv[1]
receiver = sys.argv[2]
money = sys.argv[3]

string = giver + ',' + receiver + ',' + money

i=1
while os.path.isfile("./blockChain/"+str(i)+".txt"):
    i += 1
i -= 1
with open("./blockChain/"+str(i)+".txt",'r+') as f:
    content = ""
    txt_file = f.readlines()
    if len(txt_file) == 7:
        path = "./blockChain/"+str(i + 1)+".txt"
        for l in txt_file:
            content += l
        with open(path, 'w') as f2:
            print(content)
            message = content.encode('utf-8')

            # Create a SHA-256 hash object
            hash_object = hashlib.sha256()

            # Update the hash object with the message
            hash_object.update(message)

            # Get the hexadecimal representation of the hash value
            hash_hex = hash_object.hexdigest()
            f2.write("Sha256 of previous block: " + hash_hex + "\n")
            f2.write("Next block: " + str(i + 2) + ".txt\n")
            f2.write(string + "\n")
    else:
        # print(f.read())
        if len(txt_file) == 6:
            f.write(string)
        else:
            f.write(string + "\n")



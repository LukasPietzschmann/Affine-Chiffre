import sys
import os
import aclib

#Aufgabe 8

if len(sys.argv) == 4:
    opMode = sys.argv[1]
    keyPair = sys.argv[2]
    filePath = sys.argv[3]

else:
    print("missing parameters")
    exit()

if os.path.isfile(filePath):
    if aclib.switch[keyPair[0]] in aclib.keyTable and len(keyPair) == 2:
        if opMode == "e":
            f = open(filePath).read()
            print(aclib.acEncrypt(keyPair[0], keyPair[1], f))

        elif opMode == "d":
            f = open(filePath).read()
            print(aclib.acDecrypt(keyPair[0], keyPair[1], f))

        else:
            print("select opmode by entering either 'e' or 'd'")
    else:
        print("invalid or missing key")
else:
    print("invalid path or file does not exist")
    exit()
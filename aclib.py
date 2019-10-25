#############################
#-------helper dict----------
switch = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}

#############################
#------------aufg1-----------
def decode(text):
    numList = []

    for x in text.lower():
        if x.isalpha():
            numList.append(switch[x])

    return numList

#########################################
#-------------aufg2----------------------
def encode(charList):
    str = ""

    for x in charList:
        for y in switch:
            if x == switch[y]:
                str += y
                continue

    return str

#########################################
#-------------aufg3----------------------
keyTable={
    1: 1,
    3: 9,
    5: 21,
    7: 15,
    9: 3,
    11: 19,
    15: 7,
    17: 23,
    19: 11,
    21: 5,
    23: 17,
    25: 25
}

#########################################
#-------------aufg4----------------------
def acEncrypt(a, b, plainText):
    if a.isalpha():
        a = switch[a]

    if b.isalpha():
        b = switch[b]

    str = ""
    numList = []
    if a in keyTable:
        numList = decode(plainText)

        for i in range(len(numList)):
            numList[i] = (a * numList[i] + b) % 26

        return encode(numList).upper()

    else:
        print("invalid key")
        return str

#########################################
#------------aufg5-----------------------
def acDecrypt(a,b, cipherText):
    if a.isalpha():
        a = switch[a]

    if b.isalpha():
        b = switch[b]

    str =""
    if a in keyTable:
        numList = decode(cipherText)

        for i in range(len(numList)):
            numList[i] = ((numList[i] - b) * keyTable[a]) % 26

        return encode(numList).lower()

    else:
        print("invalid key")
        return str

###########################################
#------------aufg6-------------------------
#soll schlüsselumwrechnung in funktionen mit implementiert werden?
#d = 3, b = 2
#print(acEncrypt("d","b","strenggeheim"))
#p = 15, i = 8
print(acDecrypt("p","i","IFFYVQMJYFFDQ"))

#print(acDecrypt(11,23,acEncrypt(11,23,"botschaft")))


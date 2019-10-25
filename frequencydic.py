#########################################
#-------------aufg11----------------------

def computeFrequencyTable(char_list):
    freq = {}

    for c in char_list:
        if c in freq:
            freq[c] = freq[c] + 1
        else:
            freq[c] = 1

    freq = dict(sorted(freq.items()))
    printFrequencyTable(freq)
    return freq


#########################################
#-------------aufg12----------------------

def printFrequencyTable(freq_table):
    for k, v in freq_table.items():
        #print(chr(k+97), ' : ', v)
        continue

#########################################
#-------------aufg13----------------------

def computeMostFrequentChars(freq_table, n):
    map = dict(Sort_Tuple(list(freq_table.items())))
    freq_list = []

    if n > len(freq_table):
        #Fehlerabfangen
        print("n is too big")
        return

    for i in range(len(map)-1, len(map)-n-1, -1):
        freq_list.append(list(map.keys())[i])
        #print(chr(list(map.keys())[i]))

    return freq_list


def Sort_Tuple(tup):
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

def text_in_list(string):
    lst = []
    for s in string:
        lst.append(ord(s.lower()))

    return lst


#########################################
#-------------aufg14----------------------
def computeKeyPairs(char_list):
    lst = []
    for c0 in char_list:
        for c1 in char_list:
            if c0 != c1:
                lst.append((c0, c1))

    return lst

computeKeyPairs([1,2,3,4])
#computeMostFrequentChars(computeFrequencyTable(text_in_list("Lukas hat kein Waffeleisen. Jannik hat auch kein Waffeleisen. Und Josepf hat leider keinen Penis. Tim ist ein Bastard und Vincent eigentlich im vierten Semester und gleichzeitig auch im ersten. Ich mag Sascha. Viel Spaß den prozentualen Anteil jedes Buchstabens her zu prüfen. Mehr Text. Ich brauche noch einen piraten in meiner Story. Joo, sagt der Pirat! Ich mag Shakespear und Vincent aus m Vierten. ")), 10)
#computeMostFrequentChars(computeFrequencyTable([4, 8, 13, 11, 0, 13, 6, 4, 17, 19, 4, 23, 19, 14, 7, 13, 4, 18, 18, 8, 13, 13]), 8)
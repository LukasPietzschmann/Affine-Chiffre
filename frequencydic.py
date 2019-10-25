#########################################
#-------------aufg11----------------------

# computeFrequencyTable erzeugt ein Dictionary mit jedem Character
# aus char_list als Key und der zugehörigen absoluten Häufigkeit als value
# Das Dictionary wird in Abhängigkeit der Keys sortiert und ausgegeben
def computeFrequencyTable(char_list):
    freq = {}

    for c in char_list:
        if c in freq:               # Überprüfung ob Character c bereits als Key vorhanden ist
            freq[c] = freq[c] + 1   # Falls ja, wird die absolute Häufigkeit um 1 erhöht
        else:
            freq[c] = 1             # Falls, nein wird der Key neu angelegt und mit 1 initialisiert

    freq = dict(sorted(freq.items()))   # Sortieren des Dictionarys
    printFrequencyTable(freq)           # Ausgabe
    return freq


#########################################
#-------------aufg12----------------------

# printFrequencyTable gibt das Dictionary freq_table aus und stellt dabei die
# Keys als Buchstaben und nicht als Zahlen dar
def printFrequencyTable(freq_table):
    for k, v in freq_table.items():
        print(chr(k+97), ' : ', v)

#########################################
#-------------aufg13----------------------

# computeMostFrequentChars gibt eine Liste mit den n meist verwendetetn
# Buchstaben zurück
def computeMostFrequentChars(freq_table, n):
    map = dict(Sort_Tuple(list(freq_table.items())))    # Sortiert das Dictionary nach den Values
    freq_list = []

    if n > len(freq_table):                             # Fehlerabfrange falls n zu groß gewählt wurde
        print("n is too big")
        return

    for i in range(len(map)-1, len(map)-n-1, -1):
        freq_list.append(list(map.keys())[i])           # fügt die höchsten n Elemente zu einer Liste hinzu

    return freq_list

# Sortiert das Dictionary nach den Values
def Sort_Tuple(tup):
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


#########################################
#-------------aufg14----------------------

# Erstellt alle Permutationen an Tupeln
def computeKeyPairs(char_list):
    lst = []
    for c0 in char_list:
        for c1 in char_list:
            if c0 != c1:
                lst.append((c0, c1))

    return lst

computeMostFrequentChars(computeFrequencyTable([4, 8, 13, 11, 0, 13, 6, 4, 17, 19, 4, 23, 19, 14, 7, 13, 4, 18, 18, 8, 13, 13]), 8)
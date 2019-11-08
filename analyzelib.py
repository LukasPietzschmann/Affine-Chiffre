from aclib import acDecrypt2
from math import gcd

#########################################
#-------------aufg11----------------------

# computeFrequencyTable erzeugt ein Dictionary mit
# jedem Character aus char_list als Key und der
# zugehoerigen absoluten Haeufigkeit als Value
# Das Dictionary wird in Abhaengigkeit der Keys
# sortiert und ausgegeben

def computeFrequencyTable(char_list):
    freq = {}

    for c in char_list:
        if c in freq:                               # ueberpruefung ob Character c bereits als Key vorhanden ist
            freq[c] = freq[c] + 1                   # Falls ja, wird die absolute Haeufigkeit um 1 erhoeht
        else:
            freq[c] = 1                             # Falls, nein wird der Key neu angelegt und mit 1 initialisiert

    freq = dict(sorted(freq.items()))               # Sortieren des Dictionarys
    return freq


#########################################
#-------------aufg12----------------------

# printFrequencyTable gibt das Dictionary
# freq_table aus und stellt dabei die
# Keys als Buchstaben und nicht als Zahlen dar
def printFrequencyTable(freq_table):
    for k, v in freq_table.items():
        print(chr(k + 97), ' : ', v)


#########################################
#-------------aufg13----------------------

# computeMostFrequentChars gibt eine Liste mit
# den n meist verwendetetn Buchstaben zurueck
def computeMostFrequentChars(freq_table, n):
    map = dict(sortTuple(list(freq_table.items())))    # Sortiert das Dictionary nach den Values
    freq_list = []

    if n > len(freq_table):                            # Fehlerabfrange falls n zu gross gewaehlt wurde
        print("n is too big")
        return

    for i in range(len(map)-1, len(map)-n-1, -1):
        freq_list.append(list(map.keys())[i])           # fuegt die hoechsten n Elemente zu einer Liste hinzu

    return freq_list

# "Hilfsmethode" zum sortieren des Dictionaries
# nach den Values
def sortTuple(tup):
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst - i - 1):
            if tup[j][1] > tup[j + 1][1]:
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


#########################################
#-------------aufg14----------------------

# Erstellt alle Permutationen an Tupeln
def computeKeyPairs(char_list):
    perms = []
    for c0 in char_list:
        for c1 in char_list:
            if c0 != c1:                                # fuer jedes c0 wird jedes c1 ueberprueft ob es gleich ist und falls nicht
                perms.append((c0, c1))

    return perms


########################################
# ------------aufg15--------------------

# nimmt einen verschluesselten Text und eine Liste an
# Permutationen der haeufigsten Buchstaben
def analyzeCipherText(cipher_text, char_pairs):
    for i in char_pairs:                                # i laeuft ueber alle Permutationen
        a = (3 * (i[1] - i[0])) % 26                    # Berechnung eines moeglichen Schluessels (a, b)
        b = (i[0] - 4 * a) % 26

        if gcd(a, 26) == 1:                             # Test ob Geheimtext entschluesselt werden kann
            out = acDecrypt2(a, b, cipher_text)         # Entschluesslung des Geheimtexts
            print(out[0:50])

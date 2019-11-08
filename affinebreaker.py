import os
from sys import argv
from analyzelib import *
from aclib import decode


########################################
# ------------aufg16--------------------

# Analysiert den Geheimtext aus der Datei die
# unter dem Pfad path gespeichert ist
def main(path):
    if os.path.isfile(path) and os.access(path, os.R_OK):
        c_text = open(path).read()

        freq_table = computeFrequencyTable(decode(c_text))
        print("Vorkommnis aller Buchstaben im Geheimtext: ")
        printFrequencyTable(freq_table)

        n = 14
        freq_list = computeMostFrequentChars(freq_table, n)
        print("Die ", n, " am häufigsten vorkommenden Buchstaben: ")
        char_freq_list = []
        for c in freq_list:
            char_freq_list.append(chr(c + 97))
        print(char_freq_list)

        keys = computeKeyPairs(freq_list)
        print("Mögliche Schlüssel sind: ")
        print(keys)

        print("Analyse des Geheimtextes (Jeweils die ersten 50 Zeichen)")
        analyzeCipherText(c_text, keys)
    else:
        print("File Error")


if __name__ == '__main__':
    main(argv[1])

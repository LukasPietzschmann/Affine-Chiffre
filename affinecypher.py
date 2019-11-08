import sys
import os
import aclib

# es wird ueberprueft ob alle Eingaben Parameter beim Programmstart uebergeben wurden
# 4 Argumente muessen vorhanden sein da der erste immer der Programmname selbst ist
# die anderen 3 erwarteten Parameter sind der Modus ob ent- oder verschluesselt wird
# das Schluesselpaar und der Pfad der Datei mit der man arbeiten moechte
if len(sys.argv) == 4:
    op_mode = sys.argv[1]
    key_pair = sys.argv[2]
    file_path = sys.argv[3]

else:
    print("missing parameters")
    exit()

# es wird geprueft ob der angegebene Pfad auf eine Datei zeigt und ob man leseberechtigt ist
# nun wird geprueft ob der erste Key gueltig ist und ob das Schluesselpaar auch wirklich aus 2 Schluesseln besteht
# wenn encode als modus gewaehlt wurde wird die acEncrypt funktion aus der aclib benutzt
# um den Text in der uebergebenen Datei zu verschluessen
# falls decrypt gewaehlt wurde wird acDecrypt aus der aclib benutz um den Text zu verschluesseln

if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
    if aclib.switch[key_pair[0]] in aclib.keyTable and len(key_pair) == 2:
        if op_mode == "e":
            f = open(file_path).read()
            aclib.acEncrypt(key_pair[0], key_pair[1], f)

        elif op_mode == "d":
            f = open(file_path).read()
            aclib.acDecrypt(key_pair[0], key_pair[1], f)


        else:
            print("select opmode by entering either 'e' or 'd'")
    else:
        print("invalid or missing key")
else:
    print("invalid path or file does not exist or cannot read file")



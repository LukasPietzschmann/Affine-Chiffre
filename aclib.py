#############################
# -------helper dict----------
# dictonary der switch-case in python implementieren soll
# es werden die ASCII werte zwischen 97 und 123 benutzt da dies genau den bereich der kleinbuchstaben a-z abdeckt
# diese werte werden werden in ASCII buchstaben konvertiert und als key für den dictionary benutzt
# deren wert minus 97 wird dann als dessen value zugewiesen

switch = {}

for i in range(97, 123):
    switch[chr(i)] = i - 97

#############################
# ------------aufg1-----------
#  prueft ob "text" ein string ist
# danach wird über jedes zeichen in "text" iteriert und falls moeglich zu
# einem kleinbuchstaben konvertiert
# in der schleife wird getestet ob ob das zeichen ein buchstabe ist
# falls ja wird der buchstabe kodiert und zu num_list hinzugefuegt


def decode(text):
    num_list = []

    if isinstance(text, str):
        for x in text.lower():
            if x.isalpha():
                num_list.append(switch[x])
    else:
        print("please enter a string")
    return num_list

#########################################
# -------------aufg2----------------------
# es wird über die liste drüber iteriert
# innerhalb dieser schleife wird jeder key in switch durch gegeangen
# nun wird jedes value mit x verglichen
# falls es eine uebereinstimmung gibt wird der key
# zum string hinzugefuegt (somit werden die zahlen in charList
# in die korrespondierenden buchstaben umgewandelt

def encode(char_list):
    out = ""

    for x in char_list:
        for y in switch:
            if x == switch[y]:
                out += y
                continue

    return out

#########################################
# -------------aufg3----------------------
# keytable um die passenden inversen zu finden

key_table={
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
# -------------aufg4----------------------
# testet ob a und b Buchstaben, Zahlen oder Zahlen in Strings sind, wenn einer der ersten beiden Faelle
# zutrifft werden sie zu ihren korrespondierenden Zahlen Werte konvertiert
# wenn a eine gueltige invertierbare Zahl ist wird der Plaintext unter Verwendung der decode() Funktion
# in Zahlen umgewandelt
# wenn nein bricht die Funktion ab und gibt "invalid key" auf der Konsole aus,
# diese werden danach unter der Verwendung von den Schluesseln a und b verschluesselt
# die verschluesselte Zahlen Liste wird danach wieder in durch die encode() Funtkion in Buchstaben umgewandelt
# und als Großbuchstaben ausgegeben


def acEncrypt(a, b, plain_text):
    if isinstance(a, str):
        if a.isalpha():
            a = switch[a]
        else:
            a = int(a)

    if isinstance(b, str):
        if b.isalpha():
            b = switch[b]
        else:
            b = int(b)

    num_list = []
    if a in key_table:
        num_list = decode(plain_text)

        for i in range(len(num_list)):
            num_list[i] = (a * num_list[i] + b) % 26

        print(encode(num_list).upper())

    else:
        print("invalid key")
        return ""


#########################################
# ------------aufg5-----------------------
# es wird wieder geprueft ob a und b Buchstaben, Zahlen oder Zahlen in Strings sind, wenn einer der ersten beiden Faelle
# zutrifft werden sie zu ihren korrespondierenden Zahlen Werte konvertiert
# nun wird geprueft ob a ein gueltiger Schluessel ist, wenn nein bricht die Funktion ab und gibt "invalid key" auf der Konsole aus
# und mit encode wird der Text in eine Zahlen Liste umgewandelt
# die in der acEncrypt Funktion verwendete Gleichung zur Verschluesselung wird nun umgestellt um die Verschluesslung
# rueckgaengig zu machen
# anschliessend wird die Zahlen Liste wieder in Kleinbuchstaben umgewandelt und ausgegeben

def acDecrypt(a, b, cipher_text):
    if isinstance(a, str):
        if a.isalpha():
            a = switch[a]
        else:
            a = int(a)

    if isinstance(b, str):
        if b.isalpha():
            b = switch[b]
        else:
            b = int(b)

    if a in key_table:
        num_list = decode(cipher_text)

        for i in range(len(num_list)):
            num_list[i] = ((num_list[i] - b) * key_table[a]) % 26

        print(encode(num_list).lower())

    else:
        print("invalid key")
        return ""


#################################################################
# diese Funktionen müssen für aufg15 benutzt werden da ich was falsch interpretiert hab als ich acEncrypt und acDecrypt geschrieben hab
# in der aufgabe heißt es eigentlich das man den Output nicht zurückgeben sondern ausgeben soll...
# aber in aufg15 darf nichts anderes als die 50 Zeichen ausgegeben werden weshalb man diese leicht abgeänderten Funktionen benutzen muss
# der einzige Unterschied hier ist lediglich das die return Werte zurückgegeben werden


def acEncrypt2(a, b, plain_text):
    if isinstance(a, str):
        if a.isalpha():
            a = switch[a]
        else:
            a = int(a)

    if isinstance(b, str):
        if b.isalpha():
            b = switch[b]
        else:
            b = int(b)

    num_list = []
    if a in key_table:
        num_list = decode(plain_text)

        for i in range(len(num_list)):
            num_list[i] = (a * num_list[i] + b) % 26

        return encode(num_list).upper()

    else:
        print("invalid key")
        return ""

def acDecrypt2(a, b, cipher_text):
    if isinstance(a, str):
        if a.isalpha():
            a = switch[a]
        else:
            a = int(a)

    if isinstance(b, str):
        if b.isalpha():
            b = switch[b]
        else:
            b = int(b)

    if a in key_table:
        num_list = decode(cipher_text)

        for i in range(len(num_list)):
            num_list[i] = ((num_list[i] - b) * key_table[a]) % 26

        return encode(num_list).lower()

    else:
        print("invalid key")
        return ""
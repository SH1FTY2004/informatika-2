
def sifruj(text, posun):
    vysledek = ""

    for znak in text:
        
        if 'a' <= znak <= 'z':
            pos = ord(znak) - ord('a')
            pos = (pos + posun) % 26
            vysledek += chr(ord('a') + pos)

        
        elif 'A' <= znak <= 'Z':
            pos = ord(znak) - ord('A')
            pos = (pos + posun) % 26
            vysledek += chr(ord('A') + pos)

        
        else:
            vysledek += znak

    return vysledek



print(sifruj("Abc Z", 1))  

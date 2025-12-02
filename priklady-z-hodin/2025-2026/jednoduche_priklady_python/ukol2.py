
def spocitej_znaky(text):
    text = text.lower()        
    vysledky = {}              

    for znak in text:
        if znak == " ":       
            continue

        if znak in vysledky:   
            vysledky[znak] += 1
        else:                  
            vysledky[znak] = 1

    return vysledky



vstup = "Ahoj světe"
print(spocitej_znaky(vstup))


def vypis_statistiku(seznam):
    if len(seznam) == 0:
        print("Nebyla zadána žádná čísla.")
        return

    soucet = sum(seznam)
    nejvetsi = max(seznam)
    nejmensi = min(seznam)
    prumer = soucet / len(seznam)

    sude = 0
    liche = 0

    for cislo in seznam:
        if cislo % 2 == 0:
            sude += 1
        else:
            liche += 1

    print("===== STATISTIKA =====")
    print(f"Součet: {soucet}")
    print(f"Největší číslo: {nejvetsi}")
    print(f"Nejmenší číslo: {nejmensi}")
    print(f"Počet sudých čísel: {sude}")
    print(f"Počet lichých čísel: {liche}")
    print(f"Průměrná hodnota: {prumer:.2f}")



cisla = []

while True:
    vstup = input("Zadej číslo (nebo 'stop'): ")

    if vstup.lower() == "stop":
        break

    try:
        cislo = float(vstup)
        cisla.append(cislo)
    except ValueError:
        print("Zadal jsi neplatnou hodnotu, zkus to znovu.")

vypis_statistiku(cisla)


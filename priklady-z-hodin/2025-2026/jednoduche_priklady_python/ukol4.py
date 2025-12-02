
with open("system.log", "w", encoding="utf-8") as f:
    f.write("INFO: Systém byl spuštěn\n")
    f.write("WARNING: Nízká kapacita paměti\n")
    f.write("ERROR: Nepodařilo se načíst konfiguraci\n")
    f.write("INFO: Operace dokončena\n")
    f.write("ERROR: Selhalo připojení k databázi\n")


with open("system.log", "r", encoding="utf-8") as vstup:
    radky = vstup.readlines()

error_radky = []

for r in radky:
    if "ERROR" in r:
        error_radky.append(r)

with open("errors_only.txt", "w", encoding="utf-8") as vystup:
    for r in error_radky:
        vystup.write(r)

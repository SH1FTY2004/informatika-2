

studenti = []



def pridej_studenta(jmeno, znamky):
    student = {
        "jmeno": jmeno,
        "znamky": znamky
    }
    studenti.append(student)



def nejlepsi_student(seznam_studentu):
    if len(seznam_studentu) == 0:
        print("Žádní studenti nejsou v evidenci.")
        return

    nejlepsi = None
    nejlepsi_prumer = float('inf')

    for student in seznam_studentu:
        prumer = sum(student["znamky"]) / len(student["znamky"])
        if prumer < nejlepsi_prumer:
            nejlepsi_prumer = prumer
            nejlepsi = student

    print(f"Nejlepší student je: {nejlepsi['jmeno']} (průměr: {nejlepsi_prumer:.2f})")



pridej_studenta("Jan", [1, 2, 2])
pridej_studenta("Lucie", [1, 1, 2])
pridej_studenta("Petr", [2, 3, 1])



nejlepsi_student(studenti)

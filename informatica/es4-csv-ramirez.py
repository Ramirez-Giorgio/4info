import csv
def filtra_studenti(nome_file,classe_file):
    print(f"studenti in {classe_file}: ")
    try: 
        with open(nome_file, mode = "r", encoding="utf-8") as file:
            lettore = csv.DictReader(file)
            for riga in lettore:
                if riga["Classe"]==classe_file:
                    print(riga["Nome"])
    except FileNotFoundError:
        print("file non esiste")

if __name__ == "__main__":
    filtra_studenti("studenti.csv","3A")
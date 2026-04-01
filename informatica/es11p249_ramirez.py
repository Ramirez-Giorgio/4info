with open("nazionicapitali_es11.txt", "w") as f:
    n = int(input("n nazioni: "))
    for i in range(n):
        nazione = input("nazione: ")
        capitale = input("capitale: ")
        f.write(nazione + " - " + capitale + "\n")
print("dati salvati\n")

print("\ndati nel file\n")
with open("nazionicapitali_es11.txt", "r") as f:
    for riga in f:
        print(riga.strip())
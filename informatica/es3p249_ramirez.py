with open("squadre_es3.txt", "w") as f:
    n = int(input("n squadre serie a: "))
    for i in range(n):
        squadra = input("nome squadra: ")
        f.write(squadra + "\n")
with open("squadre_es3.txt", "a") as f:
    n = int(input("n squadre serie b: "))
    for i in range(n):
        squadra = input("nome squadra serie B: ")
        f.write(squadra + "\n")

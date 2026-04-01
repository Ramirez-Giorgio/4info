with open("province_es5.txt", "w") as f:
    n = int(input("n provincie: "))
    for i in range(n):
        provincia = input("Inserisci provincia: ")
        f.write(provincia + "\n")
with open("province_es5.txt", "r") as f:
    province = []
    for riga in f:
        province.append(riga.strip())
province.sort()
print(f"Province ordinate: {province}")

base = int(input("inserisci la base: "))
espo = int(input("inserisci l esponente: "))
pot = base**espo  # usando le proprietà delle potenze
potm = 1  # parte da 1 cosi da non rimanere sempre 0
for i in range(espo):  # usando le moltiplicazioni
    potm = potm * base
print(f"potenza usando prodotti {potm} ed usando le proprietà delle potenze {pot}")

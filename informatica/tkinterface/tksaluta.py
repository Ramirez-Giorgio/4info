import tkinter as tk
def saluta_utente():
    nome = campo_nome.get()
    if nome:
        etichetta_risultato.config(text=f"Ciao {nome}, benvenuto!")
    else:
        etichetta_risultato.config(text="Inserisci il tuo nome!")

# Finestra principale
finestra = tk.Tk()
finestra.title("Programma di saluto")
finestra.geometry("400x250")

# Etichetta istruzioni
etichetta_istruzioni = tk.Label(finestra, text="Inserisci il tuo nome:")
etichetta_istruzioni.pack(pady=10)

# Campo di input
campo_nome = tk.Entry(finestra, width=30)
campo_nome.pack(pady=5)

# Pulsante
pulsante_saluto = tk.Button(finestra, text="Salutami", command=saluta_utente)
pulsante_saluto.pack(pady=20)

# Etichetta risultato
etichetta_risultato = tk.Label(finestra, text="", fg="blue", font=("Arial", 12, "bold"))
etichetta_risultato.pack()

# Avvio programma
finestra.mainloop()
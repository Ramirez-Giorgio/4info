import tkinter as tk
from datetime import datetime

def calcola_eta():
    anno = campo_anno.get()

    if anno:
        try:
            anno = int(anno)#trasforma anno in int dal testo
            anno_corrente = datetime.now().year
            eta = anno_corrente - anno

            if eta < 0:
                etichetta.config(text="Non vieni dal futuro, gng ")
            else:
                etichetta.config(text=f"Hai {eta} anni")
        except ValueError:
            etichetta.config(text="Metti un numero valido my g")
    else:
        etichetta.config(text="Inserisci anno!")

finestra = tk.Tk()
finestra.title("Calcolo Età")
finestra.geometry("400x250")
finestra.resizable(False, False)

etichetta_istruzioni = tk.Label(finestra, text="Inserisci anno di nascita:")
etichetta_istruzioni.pack(pady=10)

campo_anno = tk.Entry(finestra, width=30)
campo_anno.pack(pady=5)

calc = tk.Button(finestra, text="Calcola", command=calcola_eta)
calc.pack(pady=20)

etichetta = tk.Label(finestra, text="", fg="blue", font=("Arial", 12, "bold"))
etichetta.pack()

finestra.mainloop()

import tkinter as tk
from tkinter import colorchooser

def scegli_colore_testo():
    # apre la finestra per scegliere il colore del testo
    colore = colorchooser.askcolor(title="Scegli colore testo")
    if colore[1]:  # colore[1] è la stringa esadecimale del colore
        txtTesto.config(fg=colore[1])

def scegli_colore_sfondo():
    # apre la finestra per scegliere il colore di sfondo
    colore = colorchooser.askcolor(title="Scegli colore sfondo")
    if colore[1]:
        txtTesto.config(bg=colore[1])

def main():
    global txtTesto

    root = tk.Tk()
    root.title("Colori della casella di testo")
    root.geometry("400x300")

    # Text widget
    txtTesto = tk.Text(root, width=40, height=10)
    txtTesto.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Pulsante per il colore del testo
    btnColore = tk.Button(root, text="Colore testo", command=scegli_colore_testo)
    btnColore.grid(row=1, column=0, padx=10, pady=10)

    # Pulsante per il colore di sfondo
    btnSfondo = tk.Button(root, text="Colore sfondo", command=scegli_colore_sfondo)
    btnSfondo.grid(row=1, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
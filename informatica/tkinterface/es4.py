import tkinter as tk
from tkinter import filedialog, messagebox


def apri_file():
    file = None
    try:
        percorso = filedialog.askopenfilename(
            title="Apri file",
            filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")]
        )

        if percorso == "":
            return

        txtPercorso.delete(0, tk.END)
        txtPercorso.insert(0, percorso)

        file = open(percorso, "r", encoding="utf-8")

        contatore = 0
        for riga in file:
            contatore += 1

        messagebox.showinfo(
            "Conteggio righe",
            f"Numero di righe nel file: {contatore}"
        )

    except:
        messagebox.showwarning(
            "Errore",
            "Problemi nell'apertura del file."
        )

    finally:
        if file is not None:
            file.close()


def main():
    global txtPercorso

    root = tk.Tk()
    root.title("Conteggio righe file")
    root.geometry("450x120")

    lbl = tk.Label(root, text="Percorso file:")
    lbl.pack(pady=5)

    txtPercorso = tk.Entry(root, width=60)
    txtPercorso.pack(pady=5)

    btnApri = tk.Button(root, text="Apri", command=apri_file)
    btnApri.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
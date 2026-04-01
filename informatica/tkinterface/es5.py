import tkinter as tk
from tkinter import filedialog, messagebox

percorso_file = ""  # variabile globale per il percorso del file

def apri_file():
    global percorso_file
    file = None
    try:
        percorso_file = filedialog.askopenfilename(
            title="Apri file",
            filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")]
        )
        if percorso_file == "":
            return

        txtPercorso.delete(0, tk.END)
        txtPercorso.insert(0, percorso_file)

        file = open(percorso_file, "r", encoding="utf-8")
        contenuto = file.read()
        '''"1.0" → inizia dalla prima riga, prima colonna (inizio del testo)
        tk.END → fino alla fine del testo'''
        areaTesto.delete("1.0", tk.END)
        areaTesto.insert(tk.END, contenuto)

    except Exception as e:
        messagebox.showwarning("Errore", f"Impossibile aprire il file.\n{e}")

    finally:
        if file is not None:
            file.close()


def salva_file():
    global percorso_file
    file = None
    try:
        if percorso_file == "":
            percorso_file = filedialog.asksaveasfilename(
                title="Salva file",
                defaultextension=".txt",
                filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")]
            )
            if percorso_file == "":
                return

        file = open(percorso_file, "w", encoding="utf-8")
        testo = areaTesto.get("1.0", "end-1c")  # end-1c per non prendere il carattere finale extra
        file.write(testo)
        messagebox.showinfo("Salvataggio", "File salvato correttamente!")

        txtPercorso.delete(0, tk.END)
        txtPercorso.insert(0, percorso_file)

    except Exception as e:
        messagebox.showwarning("Errore", f"Impossibile salvare il file.\n{e}")

    finally:
        if file is not None:
            file.close()


def analizza_file():
    try:
        '''areaTesto.get("1.0", "end-1c")
        areaTesto → è la Text widget.
        get(start, end) → prende il testo da start a end.
        Parametri:
        "1.0" → significa riga 1, colonna 0, cioè l’inizio del testo.
        "end" → significa alla fine del testo, ma attenzione: 
        Tkinter aggiunge sempre un carattere di fine riga invisibile alla fine della Text widget.
        "end-1c" → significa fino a un carattere prima della fine, così eviti il carattere extra.'''
        testo = areaTesto.get("1.0", "end-1c").strip()
        if not testo:
            messagebox.showinfo("Analisi del file", "Il file è vuoto!")
            return

        righe = len(testo.splitlines())
        parole = len(testo.split())
        caratteri = len(testo)
        paragrafi = len([p for p in testo.split("\n\n") if p.strip()])

        messagebox.showinfo(
            "Analisi del file",
            f"Righe: {righe}\nParole: {parole}\nCaratteri: {caratteri}\nParagrafi: {paragrafi}"
        )

    except Exception as e:
        messagebox.showwarning("Errore", f"Errore durante l'analisi del file.\n{e}")


def main():
    global txtPercorso, areaTesto

    root = tk.Tk()
    root.title("Editor di testo con analisi")
    root.geometry("600x500")

    tk.Label(root, text="Percorso file:").pack(pady=5)
    txtPercorso = tk.Entry(root, width=80)
    txtPercorso.pack(pady=5)

    frame_btn = tk.Frame(root)
    frame_btn.pack(pady=5)

    btnApri = tk.Button(frame_btn, text="Apri", command=apri_file)
    btnApri.pack(side=tk.LEFT, padx=5)

    btnSalva = tk.Button(frame_btn, text="Salva", command=salva_file)
    btnSalva.pack(side=tk.LEFT, padx=5)

    btnAnalizza = tk.Button(frame_btn, text="Analizza", command=analizza_file)
    btnAnalizza.pack(side=tk.LEFT, padx=5)

    areaTesto = tk.Text(root, width=70, height=25)
    areaTesto.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
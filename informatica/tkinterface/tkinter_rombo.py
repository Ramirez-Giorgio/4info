import tkinter as tk
from tkinter import messagebox  # Per mostrare avvisi in caso di errore

class Rombo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master # Salviamo il riferimento al master
        self.master.title("Calcolo Rombo")
        self.master.geometry("350x380") # Leggermente più alto per stare comodi
        
        # Impostiamo il colore di sfondo del frame e della finestra principale
        self.config(bg='pink')
        self.master.config(bg='pink')
        
        self.pack(expand=True, fill="both") # Usiamo pack per centrare il contenuto
        self.crea_widgets()

    def crea_widgets(self):
        # Container interno per centrare i widget nella griglia
        container = tk.Frame(self, bg="pink")
        container.place(relx=0.5, rely=0.5, anchor="center")

        # Label e Entry Diagonale Maggiore
        tk.Label(container, text="Diagonale Maggiore:", bg="pink").grid(row=0, column=0, pady=5, padx=10, sticky="e")
        self.txtMag = tk.Entry(container, bg="#FFF0F5")
        self.txtMag.grid(row=0, column=1)

        # Label e Entry Diagonale Minore
        tk.Label(container, text="Diagonale Minore:", bg="pink").grid(row=1, column=0, pady=5, padx=10, sticky="e")
        self.txtMin = tk.Entry(container, bg="#FFF0F5")
        self.txtMin.grid(row=1, column=1)

        # Label e Entry Lato
        tk.Label(container, text="Lato:", bg="pink").grid(row=2, column=0, pady=5, padx=10, sticky="e")
        self.txtLato = tk.Entry(container, bg="#FFF0F5")
        self.txtLato.grid(row=2, column=1)

        # Bottone Calcola (Standard Tkinter)
        # Su Windows il parametro 'bg' funziona bene con i bottoni standard
        self.btnCalcola = tk.Button(container, text="Calcola", bg="#FF69B4", fg="white", font=('Helvetica', 10, 'bold'), command=self.calcolo)
        self.btnCalcola.grid(row=3, column=0, columnspan=2, pady=20, ipadx=20)

        # Risultato Area
        tk.Label(container, text="Area:", bg="pink").grid(row=4, column=0, sticky="e")
        self.lblAreaRisultato = tk.Label(container, text="0.0", bg="#FFF0F5", width=12, relief="sunken")
        self.lblAreaRisultato.grid(row=4, column=1, pady=5)

        # Risultato Perimetro
        tk.Label(container, text="Perimetro:", bg="pink").grid(row=5, column=0, sticky="e")
        self.lblPeriRisultato = tk.Label(container, text="0.0", bg="#FFF0F5", width=12, relief="sunken")
        self.lblPeriRisultato.grid(row=5, column=1, pady=5)

        # Bottone ESCI
        self.btnEsci = tk.Button(container, text="ESCI", bg="#FF69B4", fg="black", 
                                 command=self.master.destroy)
        self.btnEsci.grid(row=6, column=0, columnspan=2, pady=15, ipadx=10)

    def calcolo(self):
        try:
            # Recupero valori e conversione
            D = float(self.txtMag.get() or 0)
            d = float(self.txtMin.get() or 0)
            L = float(self.txtLato.get() or 0)
        
            area = (D * d) / 2
            perimetro = L * 4
            
            # Aggiornamento label con formattazione a 2 decimali
            self.lblAreaRisultato.config(text=f"{area:.2f}")
            self.lblPeriRisultato.config(text=f"{perimetro:.2f}")
            
        except ValueError:
            messagebox.showerror("Errore", "valore non valido")

if __name__ == "__main__":
    root = tk.Tk()
    app = Rombo(master=root)
    app.mainloop()
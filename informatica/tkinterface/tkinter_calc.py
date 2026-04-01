import tkinter as tk
from tkinter import messagebox

class CalcolatriceSemplice(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master 
        self.master.title("Calcolatrice")
        self.master.geometry("400x450")
        
        self.config(bg='blue')
        self.master.config(bg='blue') 
        self.pack(expand=True, fill="both")
        
        self.crea_widgets()

    def crea_widgets(self):
        main_container = tk.Frame(self, bg="blue")
        main_container.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(main_container, text="1 numero:", bg="blue", font=('Arial', 10, 'bold')).grid(row=0, column=0, pady=5)
        self.txtNum1 = tk.Entry(main_container, bg="#FFF0F5", font=('Arial', 12))
        self.txtNum1.grid(row=0, column=1, padx=10)
        tk.Label(main_container, text="2 numero:", bg="blue", font=('Arial', 10, 'bold')).grid(row=1, column=0, pady=5)
        self.txtNum2 = tk.Entry(main_container, bg="#FFF0F5", font=('Arial', 12))
        self.txtNum2.grid(row=1, column=1, padx=10)
        btn_frame = tk.Frame(main_container, bg="blue")
        btn_frame.grid(row=2, column=0, columnspan=2, pady=20)
        self.btnPiu = tk.Button(btn_frame, text="+", width=5, bg="#FF69B4", font=('Arial', 12, 'bold'), command=self.somma)
        self.btnPiu.grid(row=0, column=0, padx=5)
        self.btnMeno = tk.Button(btn_frame, text="-", width=5, bg="#FF69B4", font=('Arial', 12, 'bold'), command=self.sottrazione)
        self.btnMeno.grid(row=0, column=1, padx=5)
        self.btnPer = tk.Button(btn_frame, text="*", width=5, bg="#FF69B4", font=('Arial', 12, 'bold'), command=self.moltiplicazione)
        self.btnPer.grid(row=0, column=2, padx=5)
        self.btnDiviso = tk.Button(btn_frame, text="/", width=5, bg="#FF69B4", font=('Arial', 12, 'bold'), command=self.divisione)
        self.btnDiviso.grid(row=0, column=3, padx=5)

        tk.Label(main_container, text="risultato:", bg="blue", font=('Arial', 12, 'bold')).grid(row=3, column=0, pady=10)
        self.lblRisultato = tk.Label(main_container, text="0.00", bg="#FFF0F5", width=15, font=('Arial', 12, 'bold'),)
        self.lblRisultato.grid(row=3, column=1)

        self.btnReset = tk.Button(main_container, text="chiudi", bg="white", width=10, command=self.master.destroy)
        self.btnReset.grid(row=4, column=0, columnspan=2, pady=20)

    def ottieni_numeri(self):
        try:
            n1 = float(self.txtNum1.get())
            n2 = float(self.txtNum2.get())
            return n1, n2
        except ValueError:
            messagebox.showerror("Errore", "valore non valido")
            return None

    def somma(self):
        valori = self.ottieni_numeri()
        if valori is not None:
            risultato = valori[0] + valori[1]
            self.lblRisultato.config(text=f"{risultato:.2f}")

    def sottrazione(self):
        valori = self.ottieni_numeri()
        if valori is not None:
            risultato = valori[0] - valori[1]
            self.lblRisultato.config(text=f"{risultato:.2f}")

    def moltiplicazione(self):
        valori = self.ottieni_numeri()
        if valori is not None:
            risultato = valori[0] * valori[1]
            self.lblRisultato.config(text=f"{risultato:.2f}")

    def divisione(self):
        valori = self.ottieni_numeri()
        if valori is not None:
            if valori[1] == 0:
                messagebox.showwarning("Errore", "divisione per zero!")
            else:
                risultato = valori[0] / valori[1]
                self.lblRisultato.config(text=f"{risultato:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalcolatriceSemplice(master=root)
    app.mainloop()
import tkinter as tk 
from tkinter import messagebox 

class Articolo:
    def __init__(self, prodotto, quantita):
        self.prodotto = prodotto
        self.quantita = quantita

class Gestione_Spesa:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestione Spesa")
        self.root.geometry("800x650")

        self.elenco_prodotti = []

        self.crea_interfaccia()


    def crea_interfaccia(self): 

        frame_titolo = tk.Frame(self.root)
        frame_titolo.pack(fill=tk.X, pady=40)

       

        frame_sx = tk.Frame(self.root)
        frame_sx.pack(side=tk.LEFT, fill=tk.Y, padx=(250,5), pady=(0,100))

        frame_dx = tk.Frame(self.root)
        frame_dx.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 300), pady=(0,100))



        tk.Label(frame_titolo, text="Gestione Spesa", font=("Arial", 15, "bold")).pack()
        tk.Label(frame_sx, text="Aggiunta", font=("Arial", 12, "bold")).pack()

        tk.Label(frame_sx, text="Prodotto *").pack(anchor="w")
        self.entry_prod = tk.Entry(frame_sx, width=40)
        self.entry_prod.pack(fill=tk.X)

        tk.Label(frame_sx, text="Quantità *").pack(anchor="w")
        self.entry_quant = tk.Entry(frame_sx, width=40)
        self.entry_quant.pack(fill=tk.X)

        tk.Button(frame_sx, text="Aggiungi al Carrello", command=self.aggiungi).pack()





        tk.Label(frame_dx, text="Carrello", font=("Arial", 12, "bold")).pack()


        self.lista_carrello = tk.Listbox(frame_dx)
        self.lista_carrello.pack(fill=tk.BOTH, expand=True, pady=(0,10))

        tk.Button(frame_dx, text="Elimina selezionato", command=self.elimina, bg="red").pack(fill=tk.X)


    def aggiungi(self):

        prodotto = self.entry_prod.get()
        quantita = self.entry_quant.get()

        if prodotto == "" or quantita == "":
            messagebox.showinfo("Attenzione",  "Compilare tutti i capi richiesti (*)")
            return
        

        nuovo_articolo = Articolo(prodotto, quantita)
        self.elenco_prodotti.append(nuovo_articolo)
        self.aggiorna()

        self.entry_prod.delete(0, tk.END)
        self.entry_quant.delete(0, tk.END)





    def aggiorna(self):

        self.lista_carrello.delete(0, tk.END)
        
        for art in self.elenco_prodotti:
            riga = f"{art.prodotto} - {art.quantita}"
            self.lista_carrello.insert(tk.END, riga)


    def elimina(self):

        riga_selezionata = self.lista_carrello.curselection()

        if not riga_selezionata:
            messagebox.showinfo("Attenzione",  "Nessuna riga selezionata")
            return

        self.elenco_prodotti.pop(riga_selezionata[0])
        self.aggiorna()


def main():
    root = tk.Tk()
    nuova_finestra = Gestione_Spesa(root)
    root.mainloop()


if __name__=="__main__":
        main() 

            





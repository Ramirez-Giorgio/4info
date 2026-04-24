import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

class Finestra(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)        
        self.master.title("Finestra grafica")        
        self.master.geometry("600x700")        
        self.grid() 
        self.crea_widgets()

    def crea_widgets(self):
        # 1. Carico l'immagine
        img_originale = Image.open("finessi_prekirk.jpg") 
        
        # 2. La ridimensiono (es. 100x100 pixel)
        img_resized = img_originale.resize((100, 100))
        
        # 3. La converto per Tkinter
        self.foto = ImageTk.PhotoImage(img_resized)
        
        # 4. La metto in una Label
        self.lbl_img = tk.Label(self, image=self.foto)
        self.lbl_img.grid(row=0, column=0, columnspan=2, pady=10)
        self.nomi = [] # Archivio dati
        
        # Riga 0
        self.lbl1 = tk.Label(self, text = "GESTIONE NOMI")
        self.lbl1.grid(row = 0, column = 0, columnspan=2, pady=10)

        # Riga 1
        self.btn1 = tk.Button(self, text = "INVIA E MOSTRA", command=self.mostra)
        self.btn1.grid(row = 1, column = 0, padx=5)
        
        self.btn2 = tk.Button(self, text = "ESCI", command=self.master.destroy)
        self.btn2.grid(row = 1, column = 1, padx=5)

        # Riga 2
        self.btnUp = tk.Button(self, text='UP')
        self.btnUp.grid(row = 2, column = 0, pady=5)
        
        self.btnUp2 = tk.Button(self, text='DOWN')
        self.btnUp2.grid(row = 2, column = 1, pady=5)

        # Riga 3: Casella di input
        self.VaEn = tk.StringVar()
        self.en = tk.Entry(self, textvariable=self.VaEn)
        self.en.grid(row = 3, column = 0, columnspan=2, pady=10)

        # Riga 4: Titolo della lista (Sostituito .pack con .grid)
        self.lbl_lista = tk.Label(self, text="Lista nomi salvati:")
        self.lbl_lista.grid(row = 4, column = 0, columnspan=2)

        # Riga 5: Listbox (Sostituito .pack con .grid)
        self.lista_box = tk.Listbox(self, width=40)
        self.lista_box.grid(row = 5, column = 0, columnspan=2, pady=5, padx=10)

    def mostra(self):
        testo = self.en.get().strip() # .strip() toglie spazi inutili all'inizio/fine
        
        if testo != "":
            # 1. Aggiungo all'archivio (lista Python)
            self.nomi.append(testo)
            
            # 2. Aggiungo alla Listbox (grafica)
            self.lista_box.insert(tk.END, testo)
            
            # 3. Messaggio di conferma
            messagebox.showinfo('Info', f"Aggiunto correttamente: {testo}")
            
            # 4. Svuoto la casella e riporto il focus
            self.en.delete(0, tk.END)
            self.en.focus_set()
        else:
            messagebox.showwarning("Errore", "La casella è vuota!")

def main():
    f = Finestra()    
    f.mainloop()

if __name__ == "__main__":
    main()
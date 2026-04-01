import tkinter as tk
class Finestra(tk.Frame):
    # costruttore
    def __init__(self, master = None): #master = finestra padre e Finestra è al interno
        super().__init__(master)        
        self.master.title("Finestra grafica")        
        self.master.geometry("300x200")
        self.master.resizable(0,0)#rende la pagine non ridimensionabile
        self.grid()        
        self.crea_widgets()
        # inserimento dei widget
    def crea_widgets(self):
        self.lbl1 = tk.Label(self, text = "Etichetta")
        self.lbl1.grid(row = 0, column = 0)
        self.btn1 = tk.Button(self, text = "Pulsante")
        self.btn1.grid(row = 0, column = 1)
def main():
    f = Finestra()    
    f.mainloop()
main()

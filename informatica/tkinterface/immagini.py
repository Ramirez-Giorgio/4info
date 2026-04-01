# immagini.py: scorrimento di immagini
 #            con testo di spiegazione
import tkinter as tk
# testi delle spiegazioni delle immagini
from spiegazioni_img import *
class FinestraImmagini(tk.Frame):
    i = 0# indice dell'immagine    
    n = 2 # numero delle immagini - 1
    # costruttore 
    def __init__(self, master = None):
        super().__init__(master)        
        self.master.title("Immagini")        
        self.master.geometry("600x400")        
        self.grid()        
        self.crea_widgets()
# inserimento dei widget
    def crea_widgets(self):# pulsante indietro        
        self.btnIndietro = tk.Button( self, text = "<",width = 5,command = self.img_indietro)        
        self.btnIndietro.grid(row = 0, column = 0)# riquadro immagine        
        nomeimg = "img" + str(self.i) + ".png"        
        self.img = tk.PhotoImage(file = nomeimg)        
        self.lblImg = tk.Label( self, image = self.img,width= 210, height = 300)        
        self.lblImg.grid(row = 0, column = 1)        
        self.lblImg.bind("<Enter>", self.spiega_on)        
        self.lblImg.bind("<Leave>", self.spiega_off)# pulsante avanti        
        self.btnAvanti = tk.Button( self, text = ">",width = 5,command = self.img_avanti)        
        self.btnAvanti.grid(row = 0, column = 2)# riquadro spiegazione        
        self.lblSpiega = tk.Label( self,justify = tk.LEFT,bg = "lightyellow",width = 30)
        # pulsante di uscita        
        self.btnEsci = tk.Button( self, text = "Esci",command = self.master.destroy)        
        self.btnEsci.grid(row = 1, column = 1)
    def img_indietro(self):        
        self.i -= 1        
        if self.i < 0: self.i = 0        
        nomeimg = "img" + str(self.i) + ".png"        
        self.img = tk.PhotoImage(file = nomeimg)        
        self.lblImg.config(image = self.img)
    def img_avanti(self):        
        self.i += 1
        if self.i > self.n: self.i = self.n        
        nomeimg = "img" + str(self.i) + ".png"        
        self.img = tk.PhotoImage(file = nomeimg)        
        self.lblImg.config(image = self.img)
    def spiega_on(self, event):        
        self.lblSpiega.config(text = testi[self.i])        
        self.lblSpiega.grid(row = 0, column = 3, sticky = tk.NW)
    def spiega_off(self, event):        
            self.lblSpiega.grid_remove()
def main():    
    f = FinestraImmagini()    
    f.mainloop()
main()
#ESECUZIONEVisualizzatore di immagini 




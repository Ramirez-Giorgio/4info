# spiegazioni.py: scorrimento di immagini 
#con testo di spiegazione
# testi delle spiegazioni
testi = []
testi.append("""\
    La Gioconda (Monna Lisa)
    Leonardo da Vinci 
    77x53 
    Museo del Louvre di Parigi
    """)
testi.append("""\
    Vaso con quindici girasoli
    Vincent Van Gogh
    95x73 
    Van Gogh Museum di Amsterdam
    """)
testi.append("""\
    Il bacio (Episodio della giovinezza)
    Francesco Hayez
    112x88
    Pinacoteca di Brera
    """)
nomeimg = "img" + str(self.i) + ".png"
self.img = tk.PhotoImage(file = nomeimg)
self.lblImg = tk.Label( self, image = self.img,width = 210, height = 300)
def img_indietro(self):    
    self.i -= 1
    if self.i < 0: 
        self.i = 0    
    nomeimg = "img" + str(self.i) + ".png"    
    self.img = tk.PhotoImage(file = nomeimg)            
    self.lblImg.config(image = self.img)
self.lblImg.bind("<Enter>", self.spiega_on)
def spiega_on(self, event):
    self.lblSpiega.config(text = testi[self.i])    
    self.lblSpiega.grid(row = 0, column = 3, sticky = tk.NW)
self.lblImg.bind("<Leave>", self.spiega_off)
def spiega_off(self, event):
    self.lblSpiega.grid_remove()
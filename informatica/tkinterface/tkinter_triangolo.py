# AreaTriangolo.py: finestra grafica per il calcolo dell'area del triangolo
import tkinter as tk
class Triangolo(tk.Frame):
    # costruttore 
    def __init__(self, master = None):
        super().__init__(master)        
        self.master.title("Area del triangolo")        
        self.master.geometry("500x500")        
        self.grid()        
        self.crea_widgets()
        self.master.config(bg = 'pink')
        # inserimento dei widget
    def crea_widgets(self):
        self.master.config(bgwww = 'pink')
        # input misura della base         
        self.lblBase = tk.Label(self, text = "D maggiore")        
        self.lblBase.grid(row = 0, column = 0)        
        self.vBase = tk.IntVar()        
        self.txtBase = tk.Entry( self,textvariable = self.vBase)        
        self.txtBase.grid(row = 0, column = 1)
        # input misura dell'altezza        
        self.lblAltezza = tk.Label(self, text = "D minore")        
        self.lblAltezza.grid(row = 1, column = 0)        
        self.vAltezza = tk.IntVar()        
        self.txtAltezza = tk.Entry( self,textvariable = self.vAltezza)        
        self.txtAltezza.grid(row = 1, column = 1)
        #input misura lato
        self.lblLato = tk.Label(self, text = "Lato")        
        self.lblLato.grid(row = 2, column = 0)        
        self.vLato = tk.IntVar()        
        self.txtLato = tk.Entry( self,textvariable = self.vLato)        
        self.txtLato.grid(row = 2, column = 1)
        # pulsante per il calcolo        
        self.btnCalcolo = tk.Button( self, text = "Calcolo area",command = self.calcolo_area)# comando che calcola l'area
        self.btnCalcolo.grid(row = 3, column = 1, columnspan = 2) 
        self.btnCalcoloP = tk.Button( self, text = "Calcolo perimetro",command = self.calcolo_permitro)# comando che calcola l'area
        self.btnCalcoloP.grid(row = 4, column = 1, columnspan = 2)
        # output del risultato        
        self.lblArea = tk.Label(self, text = "Area")        
        self.lblArea.grid(row = 5, column = 0)        
        self.vArea = tk.DoubleVar()        
        self.txtArea = tk.Entry( self,textvariable = self.vArea)        
        self.txtArea.grid(row = 5, column = 1)
        
        self.lblPerimetro = tk.Label(self, text = "Perimetro")        
        self.lblPerimetro.grid(row = 6, column = 0)        
        self.vPerimetro = tk.DoubleVar()        
        self.txtPerimetro = tk.Entry( self,textvariable = self.vPerimetro)        
        self.txtPerimetro.grid(row = 6, column = 1)
        # pulsante di uscita        
        self.btnEsci = tk.Button( self, text = "Esci",command = self.master.destroy) #command destry cosi chiude la pagina       
        self.btnEsci.grid(row = 7, column = 1, columnspan = 2) 
# calcolo dell'area del triangolo
    def calcolo_area(self):        
        b = self.vBase.get()        
        h = self.vAltezza.get()        
        a = b * h / 2
        self.vArea.set(a)#valore viene inserito nella casella entry vArea
    def calcolo_permitro(self):        
        lato = self.vLato.get()
        a = lato*4       
        self.vPerimetro.set(a)
def main():    
    f = Triangolo()    
    f.mainloop()
main()

import tkinter as tk
from tkinter import messagebox

class CTemp(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.title('temperature')
        self.master.geometry('500x500')
        self.config(bg='#E0F7FA')
        self.grid()
        self.crea_widgets()
    def crea_widgets(self):
        self.master.config(bg='#E0F7FA')
        self.lbl_main = tk.Label(self,bg='#E0F7FA',fg='#0D47A1', text='Convertitore Temperature', font=('Arial', 20, 'bold'))
        self.lbl_main.grid(row = 0,column=0)

        self.vtemp = tk.IntVar()
        self.txtTemp = tk.Entry(self,textvariable=self.vtemp,bg='#B3E5FC')
        self.txtTemp.grid(row=1,column=0)

        btn_frame = tk.Frame(self,bg='#E0F7FA')
        btn_frame.grid(row=2, column=0, columnspan=2, pady=20)
        self.btnF = tk.Button(btn_frame,text='C -> F',fg='white',command=self.CtoF)
        self.btnF.grid(row=2,column=0,padx=10)        
        
        self.btnC = tk.Button(btn_frame,text='F -> C',fg='white',command=self.FtoC)
        self.btnC.grid(row=2,column=3,padx=10)        
        
        self.btnP = tk.Button(btn_frame,text='Pulisci',fg='white',command=self.Pulisci)
        self.btnP.grid(row=3,column=1,padx=10)        
        
        self.vR = tk.DoubleVar()
        self.txtR = tk.Entry(self,textvariable=self.vR,bg='#B3E5FC')
        self.txtR.grid(row=4,column=0)

    def CtoF(self):
        c = self.vtemp.get()
        r = c*(9/5)+32 
        self.vR.set(r) 
    def FtoC(self):
        f = self.vtemp.get()
        r = (f- 32)*5/9 
        self.vR.set(r) 

    def Pulisci(self):
        pass


def main():
    f= CTemp()
    f.mainloop()

main()
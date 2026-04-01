import tkinter as tk
from tkinter import messagebox
import csv

TEMPO = 20 * 60 # 1200 secondi
tempo_rimanente = TEMPO

class Patente(tk.Frame):
   
    def __init__(self,master = None):
        super().__init__(master)
        self.master.title('simulatore Patente')
        self.master.geometry('500x500')
        self.pack(expand=True, fill="both")
        self.crea_widgets()
    
    def crea_widgets(self):
        main_container = tk.Frame(self)
        main_container.place(relx=0.5,rely=0.5,anchor='center')
        
        tk.Label(main_container,text='Simulatore quiz patente',font=('Helvetica', 22, 'bold')).grid(row=0,column=1)
        tk.Label(main_container,text='Nome:').grid(row=1,column=0,pady=5)
       
        self.vnome = tk.StringVar()
        self.txtNome = tk.Entry(main_container,textvariable=self.vnome)
        self.txtNome.grid(row=1,column=1)

        self.btnS = tk.Button(main_container,text='SIMULAZIONE',command=self.simulazione).grid(row=2,column=1) 
        self.btnP = tk.Button(main_container,text='PATENTE',command=self.esame).grid(row=3,column=1) 
        self.btnEsci = tk.Button(main_container, text="ESCI", fg="black", command=self.master.destroy).grid(row=4, column=1)

    def carica_domande(self):
        try:
            with open('domande.csv',mode='r') as f:
                reader = csv.DictReader(f)
                self.domande = list(reader)
        except FileNotFoundError:
            messagebox.showerror('errore','file non trovato')

    def simulazione(self):
        if self.vnome.get() == '':
            messagebox.showwarning('attenzione','inserisci nome')
        
    def esame(self):
        if self.vnome.get() == '':
            messagebox.showwarning('attenzione','inserisci nome')

if __name__ == '__main__':
    root = tk.Tk()
    app = Patente(master=root)
    root.mainloop()
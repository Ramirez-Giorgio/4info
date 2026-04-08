import tkinter as tk
from tkinter import messagebox,ttk
import csv

class Patente(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.title('Simulatore quiz Patente')
        self.master.geometry('800x700')
        self.pack(expand=True,fill='both')

        self.tot_domande=[]
        self.domande=[]
        self.indice_dmd=0
        self.risposte={}
        self.max_tempo=30*60
        self.tempo_rimanente=self.max_tempo
        self.timer_a = False
        self.mod_revisione=False

        self.container=tk.Frame(self,bg='#393D6B')
        self.container.pack(expand=True,fill='both')

        self.carica_domande()
        self.crea_widget()

    def carica_domande(self):
        try:
            with open('domande_patente.csv', mode='r') as f:
                righe=f.readlines()
            if not righe:
                raise ValueError('file vuoto')
            reader=csv.DictReader(righe,delimiter=';')
            
            nomi_p=[]
            for name in reader.fieldnames:
                parola = name.strip()
                p_maiuscola = parola.lower()
                nomi_p.append(p_maiuscola)
            reader.fieldnames = nomi_p

            self.tot_domande=list(reader)
        except FileNotFoundError:
            messagebox.showerror('errore','file domande non trocato')
        except Exception as e:
            messagebox.showerror('errore',f'errore:{e}')
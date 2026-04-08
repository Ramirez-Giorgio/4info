import tkinter as tk
from tkinter import messagebox, ttk
import csv

class Patente(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Simulatore Quiz Patente')
        self.master.geometry('800x700')
        self.pack(expand=True, fill='both')

        self.tot_domande = []
        self.domande = []
        self.indice_domanda = 0
        self.risposte = {}
        self.max_tempo = 1800
        self.tempo_rimanente = 1800
        self.timer_attivo = 0
        self.mod_revisione = 0

        self.container = tk.Frame(self, bg='#1A1B26')
        self.container.pack(expand=True, fill='both')

        self.carica_domande()
        self.crea_widget()

    def carica_domande(self):
        try:
            with open('domande_patente.csv', mode='r', encoding='utf-8') as f:
                righe = f.readlines()
            
            conteggio = len(righe)
            if conteggio == 0:
                messagebox.showerror('Errore', 'File vuoto')
                return

            reader = csv.DictReader(righe, delimiter=',')
            puliti = []
            for n in reader.fieldnames:
                puliti.append(n.strip().lower())
            reader.fieldnames = puliti
            
            self.tot_domande = list(reader)
        except FileNotFoundError:
            messagebox.showerror('Errore', 'File non trovato')
        except Exception as e:
            messagebox.showerror('Errore', str(e))

    def reset_schermo(self):
        self.container.destroy()
        self.container = tk.Frame(self, bg='#1A1B26')
        self.container.pack(expand=True, fill='both')

    def crea_widget(self):
        self.reset_schermo()
        self.timer_attivo = 0
        self.mod_revisione = 0
        
        # Pannello centrale: Blu Ardesia
        inner = tk.Frame(self.container, bg='#24283B')
        inner.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(inner, text='SIMULATORE QUIZ PATENTE', bg='#24283B', fg='#7AA2F7', font=('Arial', 24, 'bold')).pack(pady=20)
        tk.Label(inner, text='Inserisci il tuo nome:', bg='#24283B', fg='#C0CAF5', font=('Arial', 12)).pack()
        
        self.vnome = tk.StringVar()
        tk.Entry(inner, textvariable=self.vnome, font=("Arial", 14), width=30, bg='#1F2335', fg='#FFFFFF', insertbackground='white').pack(pady=10)

        # Bottoni: Blu Elettrico e Ciano
        tk.Button(inner, text='SIMULAZIONE (Senza tempo)', width=30, height=2, bg='#419DFF', fg='white', font=('Arial', 10, 'bold'), relief='flat', command=lambda: self.avvia_quiz(0)).pack(pady=5)
        tk.Button(inner, text='ESAME (30 min - Con Timer)', width=30, height=2, bg='#2AC3DE', fg='white', font=('Arial', 10, 'bold'), relief='flat', command=lambda: self.avvia_quiz(1)).pack(pady=5)
        tk.Button(inner, text="ESCI", width=30, bg='#24283B', fg='#F7768E', font=('Arial', 10, 'bold'), relief='flat', command=self.master.destroy).pack(pady=20)

    def avvia_quiz(self, con_timer):
        nome_inserito = self.vnome.get().strip()
        if nome_inserito == "":
            messagebox.showwarning('Attenzione', 'inserisci il nome')
            return
        
        self.domande = self.tot_domande
        self.indice_domanda = 0
        self.risposte = {}
        self.timer_attivo = con_timer
        self.tempo_rimanente = self.max_tempo
        self.mod_revisione = 0
        
        self.schermata_quiz()
        
        if con_timer == 1: 
            self.aggiorna_timer()

    def schermata_quiz(self):
        self.reset_schermo()        
        # Header: Grigio Scuro / Nero
        header = tk.Frame(self.container, bg='#16161E', height=50)
        header.pack(fill="x")
        tk.Label(header, text=f"Candidato: {self.vnome.get()}", bg='#16161E', fg='#7AA2F7', font=("Arial", 10, "bold")).pack(side="left", padx=20)
        
        if self.timer_attivo == 1:
            # Timer: Rosso Acceso / Magenta
            self.lbl_timer = tk.Label(header, text="", font=("Arial", 12, "bold"), fg='#BB9AF7', bg='#16161E')
            self.lbl_timer.pack(side="right", padx=20)
            
            self.time_bar = ttk.Progressbar(self.container, maximum=self.max_tempo, length=700)
            self.time_bar.pack(fill="x", padx=10)
            self.time_bar['value'] = self.tempo_rimanente

        total_d = len(self.domande)
        risposte_date = len(self.risposte)
        
        prog_val = 0
        if total_d > 0:
            prog_val = (risposte_date / total_d) * 100

        pb = ttk.Progressbar(self.container, length=700, value=prog_val)
        pb.pack(pady=10)
        tk.Label(self.container, text=f"Risposte date: {risposte_date}/{total_d}", bg='#1A1B26', fg='#C0CAF5').pack()

        # Corpo domanda: Blu Scuro
        corpo = tk.Frame(self.container, bg='#24283B')
        corpo.pack(expand=True, fill="both", padx=40)
        
        domanda_attuale = self.domande[self.indice_domanda]
        
        colore_testo = "#FFFFFF"
        if self.mod_revisione == 1:
            scelta = self.risposte.get(self.indice_domanda, "")
            corretta = domanda_attuale.get('risposta', "").upper()
            if scelta == corretta:
                colore_testo = "#9ECE6A" # Verde brillante
            else:
                colore_testo = "#F7768E" # Rosso acceso

        tk.Label(corpo, text=f"DOMANDA {self.indice_domanda + 1} / {total_d}", bg='#24283B', fg='#E0AF68', font=("Arial", 12, "bold")).pack()
        tk.Label(corpo, text=domanda_attuale.get('domanda', ""), font=("Arial", 16), bg='#24283B', fg=colore_testo, wraplength=600, justify="center").pack(pady=20)

        valore_precedente = self.risposte.get(self.indice_domanda, "")
        self.var_risposta = tk.StringVar(value=valore_precedente)
        radio_frame = tk.Frame(corpo, bg='#24283B')
        radio_frame.pack(pady=20)

        # Radio buttons stile: Indaco
        tk.Radiobutton(radio_frame, text="VERO", variable=self.var_risposta, value="VERO", font=("Arial", 12, "bold"), width=10, indicatoron=0, bg='#7AA2F7', selectcolor='#3D59A1', fg='white').pack(side="left", padx=10)
        tk.Radiobutton(radio_frame, text="FALSO", variable=self.var_risposta, value="FALSO", font=("Arial", 12, "bold"), width=10, indicatoron=0, bg='#7AA2F7', selectcolor='#3D59A1', fg='white').pack(side="left", padx=10)

        nav = tk.Frame(self.container, bg='#1A1B26')
        nav.pack(side="bottom", fill="x", pady=20)
        
        tk.Button(nav, text="<< Precedente", command=self.domanda_precedente, width=15, bg='#414868', fg='white', relief='flat').pack(side="left", padx=20)
        
        if self.indice_domanda < total_d - 1:
            tk.Button(nav, text="Successiva >>", command=self.domanda_successiva, width=15, bg='#414868', fg='white', relief='flat').pack(side="left")
        
        if self.mod_revisione == 0:
            tk.Button(nav, text="INVIA QUIZ", bg="#9ECE6A", fg="#1A1B26", font=("Arial", 10, "bold"), command=self.conferma_invio, width=15, relief='flat').pack(side="right", padx=20)
        else:
            tk.Button(nav, text="TORNA AI RISULTATI", bg="#7AA2F7", fg="white", command=self.mostra_risultato, width=18, relief='flat').pack(side="right", padx=20)

    def domanda_successiva(self):
        if self.mod_revisione == 0:
            self.risposte[self.indice_domanda] = self.var_risposta.get()
        
        limite = len(self.domande) - 1
        if self.indice_domanda < limite:
            self.indice_domanda = self.indice_domanda + 1
            self.schermata_quiz()

    def domanda_precedente(self):
        if self.mod_revisione == 0:
            self.risposte[self.indice_domanda] = self.var_risposta.get()
            
        if self.indice_domanda > 0:
            self.indice_domanda = self.indice_domanda - 1
            self.schermata_quiz()

    def aggiorna_timer(self):
        if self.timer_attivo == 1:
            if self.tempo_rimanente >= 0:
                ore, resto = divmod(self.tempo_rimanente, 3600)
                minuti, secondi = divmod(resto, 60)
                
                self.lbl_timer.config(text=f"{ore:02d}:{minuti:02d}:{secondi:02d}")
                self.time_bar['value'] = self.tempo_rimanente
                
                self.tempo_rimanente = self.tempo_rimanente - 1
                self.after(1000, self.aggiorna_timer)
            else:
                self.lbl_timer.config(text="Tempo finito!")
                messagebox.showinfo("Tempo finito", "Invio del quiz")
                self.mostra_risultato()

    def conferma_invio(self):
        self.risposte[self.indice_domanda] = self.var_risposta.get()
        conferma = messagebox.askyesno("Conferma", "consegni il quiz?")
        if conferma == 1:
            self.mostra_risultato()

    def mostra_risultato(self):
        self.timer_attivo = 0
        self.reset_schermo()
        
        corrette = 0
        sbagliate = 0
        totale = len(self.domande)

        for i in range(totale):
            utente = self.risposte.get(i, "")
            data = utente.strip().upper()
            originale = self.domande[i].get('risposta', "")
            real = originale.strip().upper()
            if data == real: 
                corrette = corrette + 1
            else: 
                sbagliate = sbagliate + 1
        
        if sbagliate <= 3:
            esito = "PROMOSSO"
            colore = "#9ECE6A" # Verde
        else: 
            esito = "BOCCIATO"
            colore = "#F7768E" # Rosso

        res_frame = tk.Frame(self.container, bg='#24283B')
        res_frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(res_frame, text="RISULTATO FINALE", font=("Arial", 20, "bold"), bg='#24283B', fg="#FFFFFF").pack(pady=10)
        tk.Label(res_frame, text=f"Candidato: {self.vnome.get()}", font=("Arial", 14), bg='#24283B', fg="#C0CAF5").pack()
        tk.Label(res_frame, text=f"Risposte giuste: {corrette}", font=("Arial", 12), bg='#24283B', fg="#9ECE6A").pack()
        tk.Label(res_frame, text=f"Risposte sbagliate: {sbagliate}", font=("Arial", 12), bg='#24283B', fg="#FF9E64").pack()
        tk.Label(res_frame, text=f"Punteggio: {corrette}/{totale}", font=("Arial", 14, "bold"), bg='#24283B', fg="#FFFFFF").pack(pady=10)
        tk.Label(res_frame, text=f"ESITO: {esito}", font=("Arial", 24, "bold"), bg='#24283B', fg=colore).pack(pady=20)

        tk.Button(res_frame, text="REVISIONA", width=25, bg='#7AA2F7', fg='white', relief='flat', command=self.avvia_revisione).pack(pady=5)
        tk.Button(res_frame, text="HOME", width=25, bg='#414868', fg='white', relief='flat', command=self.crea_widget).pack(pady=5)
        tk.Button(res_frame, text="ESCI", width=25, bg='#F7768E', fg='white', relief='flat', command=self.master.destroy).pack(pady=5)

    def avvia_revisione(self):
        self.mod_revisione = 1
        self.indice_domanda = 0
        self.schermata_quiz()

if __name__ == '__main__':
    root = tk.Tk()
    app = Patente(master=root)
    root.mainloop()
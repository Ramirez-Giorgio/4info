import tkinter as tk
from tkinter import messagebox
import csv

class Patente(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Simulatore Patente')
        self.master.geometry('700x600')
        self.pack(expand=True, fill="both")
        
        # Inizializzazione variabili
        self.domande_totali = []
        self.domande = [] 
        self.indice_domanda = 0
        self.risposte_utente = {}
        self.tempo_rimanente = 20 * 60 
        self.timer_attivo = False
        
        self.container = tk.Frame(self, bg='#393D6B')
        self.container.pack(expand=True, fill="both")
        
        self.carica_domande()
        self.crea_widgets_home()

    def carica_domande(self):
        try:
            with open('domande_patente.csv', mode='r') as f:
                prima_riga = f.readline()
                separatore = ';' if ';' in prima_riga else ','
                f.seek(0)
                
                reader = csv.DictReader(f, delimiter=separatore)
                reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]
                self.domande_totali = list(reader)

            if not self.domande_totali:
                raise ValueError("Il file CSV è vuoto")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore file: {e}")
            self.domande_totali = [{"domanda": "Errore caricamento", "risposta": "FALSO"}]

    def reset_schermo(self):
        self.container.destroy()
        self.container = tk.Frame(self, bg='#393D6B')
        self.container.pack(expand=True, fill="both")

    def crea_widgets_home(self):
        self.reset_schermo()
        self.timer_attivo = False
        
        inner_frame = tk.Frame(self.container, bg='#393D6B')
        inner_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(inner_frame, text='Simulatore Quiz Patente', bg='#393D6B', fg='white', font=('Arial', 22, 'bold')).pack(pady=20)
        tk.Label(inner_frame, text='Inserisci il tuo nome:', bg='#393D6B', fg='white').pack()
        
        self.vnome = tk.StringVar()
        tk.Entry(inner_frame, textvariable=self.vnome, font=("Arial", 12)).pack(pady=10)

        # Rimosse le lambda: usiamo riferimenti diretti a funzioni wrapper
        tk.Button(inner_frame, text='SIMULAZIONE', width=25, height=2, command=self.avvia_simulazione).pack(pady=5)
        tk.Button(inner_frame, text='ESAME (20 min)', width=25, height=2, bg="#d1e7ff", command=self.avvia_esame).pack(pady=5)
        tk.Button(inner_frame, text="ESCI", width=25, fg="red", command=self.master.destroy).pack(pady=20)

    def avvia_simulazione(self):
        self.avvia_quiz(False)

    def avvia_esame(self):
        self.avvia_quiz(True)

    def avvia_quiz(self, con_timer):
        if not self.vnome.get().strip():
            messagebox.showwarning('Attenzione', 'Inserisci il nome!')
            return
        
        # Selezione sequenziale (senza random) delle prime 30 domande
        self.domande = self.domande_totali[:30]
            
        self.indice_domanda = 0
        self.risposte_utente = {}
        self.timer_attivo = con_timer
        self.tempo_rimanente = 20 * 60 
        self.schermata_quiz()
        
        if con_timer: 
            self.aggiorna_timer()

    def schermata_quiz(self):
        self.reset_schermo()
        
        # Header
        header = tk.Frame(self.container, bg="#f0f0f0")
        header.pack(fill="x")
        tk.Label(header, text=f"Candidato: {self.vnome.get()}", bg="#f0f0f0").pack(side="left", padx=20)
        
        if self.timer_attivo:
            self.lbl_timer = tk.Label(header, text="", font=("Arial", 12, "bold"), fg="red", bg="#f0f0f0")
            self.lbl_timer.pack(side="right", padx=20)

        # Domanda
        corpo = tk.Frame(self.container, bg='#393D6B')
        corpo.pack(expand=True, fill="both", padx=40)
        
        domanda_attuale = self.domande[self.indice_domanda]
        tk.Label(corpo, text=f"DOMANDA {self.indice_domanda + 1} / {len(self.domande)}", 
                 bg='#393D6B', fg='white', font=("Arial", 12, "bold")).pack(pady=10)
        
        testo = domanda_attuale.get('domanda', "Testo mancante").strip()
        tk.Label(corpo, text=testo, font=("Arial", 15), bg='#393D6B', fg='white', wraplength=550).pack(pady=30)

        # Input Risposta
        self.var_risposta = tk.StringVar(value=self.risposte_utente.get(self.indice_domanda, ""))
        radio_frame = tk.Frame(corpo, bg='#393D6B')
        radio_frame.pack(pady=20)
        
        tk.Radiobutton(radio_frame, text="VERO", variable=self.var_risposta, value="VERO", indicatoron=0, width=10).pack(side="left", padx=20)
        tk.Radiobutton(radio_frame, text="FALSO", variable=self.var_risposta, value="FALSO", indicatoron=0, width=10).pack(side="left", padx=20)

        # Navigazione
        nav = tk.Frame(self.container)
        nav.pack(side="bottom", fill="x", pady=30)
        
        if self.indice_domanda > 0:
            tk.Button(nav, text="<<", command=self.domanda_precedente, width=10).pack(side="left", padx=20)
        
        if self.indice_domanda < len(self.domande) - 1:
            tk.Button(nav, text=">>", command=self.domanda_successiva, width=10).pack(side="left", padx=10)
        else:
            tk.Button(nav, text="INVIA", bg="green", command=self.conferma_invio, width=10).pack(side="right", padx=20)

    def domanda_successiva(self):
        self.risposte_utente[self.indice_domanda] = self.var_risposta.get()
        self.indice_domanda += 1
        self.schermata_quiz()

    def domanda_precedente(self):
        self.risposte_utente[self.indice_domanda] = self.var_risposta.get()
        self.indice_domanda -= 1
        self.schermata_quiz()

    def aggiorna_timer(self):
        if self.timer_attivo and self.tempo_rimanente > 0:
            m, s = divmod(self.tempo_rimanente, 60)
            if hasattr(self, 'lbl_timer'):
                self.lbl_timer.config(text=f"Tempo: {m:02d}:{s:02d}")
            self.tempo_rimanente -= 1
            self.after(1000, self.aggiorna_timer)
        elif self.tempo_rimanente <= 0 and self.timer_attivo:
            self.mostra_risultato()

    def conferma_invio(self):
        self.risposte_utente[self.indice_domanda] = self.var_risposta.get()
        if messagebox.askyesno("Fine", "Consegnare il quiz?"):
            self.mostra_risultato()

    def mostra_risultato(self):
            self.timer_attivo = False
            self.reset_schermo()
            
            errori = 0
            numero_domande = len(self.domande)
            
            for i in range(numero_domande):
                q = self.domande[i]
                risposta_data = self.risposte_utente.get(i,"").strip().upper()
                risposta_corretta = q.get('risposta',"").strip().upper()
                
                if risposta_data != risposta_corretta:
                    errori += 1
            
            if errori <= 3:
                esito = "SUPERATO"
                colore = "green"
            else:
                esito = "BOCCIATO"
                colore = "red"

            tk.Label(self.container, text=f"ERRORI: {errori}", font=("Arial", 20), bg='#393D6B', fg=colore).pack(pady=20)
            tk.Label(self.container, text=esito, font=("Arial", 30, "bold"), bg='#393D6B', fg=colore).pack(pady=20)
            
            tk.Button(self.container, text="HOME", command=self.crea_widgets_home, width=15).pack(pady=10)
if __name__ == '__main__':
    root = tk.Tk()
    app = Patente(master=root)
    root.mainloop()
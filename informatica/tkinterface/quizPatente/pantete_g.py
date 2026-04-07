import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
#from PIL import Image, ImageTk # Necessaria per le immagini (pip install Pillow)

class Patente(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Simulatore Quiz Patente A e B')
        self.master.geometry('800x700')
        self.pack(expand=True, fill="both")
        
        # Variabili di stato
        self.domande_totali = []
        self.domande = [] 
        self.indice_domanda = 0
        self.risposte_utente = {}
        self.tempo_massimo = 30 * 60 # 30 minuti
        self.tempo_rimanente = self.tempo_massimo
        self.timer_attivo = False
        self.modalita_revisione = False
        
        self.container = tk.Frame(self, bg='#393D6B')
        self.container.pack(expand=True, fill="both")
        
        self.carica_domande()
        self.crea_widgets_home()

    def carica_domande(self):
        """Carica le domande dal CSV"""
        try:
            if not os.path.exists('domande_patente.csv'):
                raise FileNotFoundError("File 'domande_patente.csv' non trovato.")
                
            with open('domande_patente.csv', mode='r', encoding='utf-8') as f:
                prima_riga = f.readline()
                separatore = ';' if ';' in prima_riga else ','
                f.seek(0)
                reader = csv.DictReader(f, delimiter=separatore)
                reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]
                self.domande_totali = list(reader)
        except Exception as e:
            messagebox.showerror("Errore", f"Errore caricamento dati: {e}")
            self.domande_totali = [{"domanda": "Errore database", "risposta": "FALSO", "immagine": ""}]

    def reset_schermo(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def crea_widgets_home(self):
        self.reset_schermo()
        self.timer_attivo = False
        self.modalita_revisione = False
        
        inner = tk.Frame(self.container, bg='#393D6B')
        inner.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(inner, text='SIMULATORE QUIZ PATENTE A e B', bg='#393D6B', fg='white', font=('Arial', 24, 'bold')).pack(pady=20)
        tk.Label(inner, text='Inserisci il tuo nome per iniziare:', bg='#393D6B', fg='white', font=('Arial', 12)).pack()
        
        self.vnome = tk.StringVar()
        tk.Entry(inner, textvariable=self.vnome, font=("Arial", 14), width=30).pack(pady=10)

        tk.Button(inner, text='SIMULAZIONE (Esercitazione)', width=30, height=2, command=lambda: self.avvia_quiz(False)).pack(pady=5)
        tk.Button(inner, text='ESAME (30 min - Con Timer)', width=30, height=2, bg="#d1e7ff", command=lambda: self.avvia_quiz(True)).pack(pady=5)
        tk.Button(inner, text="ESCI", width=30, fg="red", command=self.master.destroy).pack(pady=20)

    def avvia_quiz(self, con_timer):
        if not self.vnome.get().strip():
            messagebox.showwarning('Attenzione', 'Inserisci il tuo nome prima di iniziare!')
            return
        
        # In esame prendiamo 30 domande (o quante ne hai), in simulazione tutte
        self.domande = self.domande_totali[:30]
        self.indice_domanda = 0
        self.risposte_utente = {}
        self.timer_attivo = con_timer
        self.tempo_rimanente = self.tempo_massimo
        self.modalita_revisione = False
        self.schermata_quiz()
        
        if con_timer: 
            self.aggiorna_timer()

    def schermata_quiz(self):
        self.reset_schermo()
        
        # --- HEADER (Nome + Timer) ---
        header = tk.Frame(self.container, bg="#f0f0f0", height=50)
        header.pack(fill="x")
        tk.Label(header, text=f"Candidato: {self.vnome.get()}", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(side="left", padx=20)
        
        if self.timer_attivo:
            self.lbl_timer = tk.Label(header, text="", font=("Arial", 12, "bold"), fg="red", bg="#f0f0f0")
            self.lbl_timer.pack(side="right", padx=20)
            
            # Barra del tempo visiva
            self.time_bar = ttk.Progressbar(self.container, maximum=self.tempo_massimo, length=700)
            self.time_bar.pack(fill="x", padx=10)
            self.time_bar['value'] = self.tempo_rimanente

        # --- PROGRESSO DOMANDE ---
        prog_val = (len(self.risposte_utente) / len(self.domande)) * 100
        pb = ttk.Progressbar(self.container, length=700, value=prog_val)
        pb.pack(pady=10)
        tk.Label(self.container, text=f"Completato: {len(self.risposte_utente)}/{len(self.domande)}", bg='#393D6B', fg='white').pack()

        # --- CORPO DOMANDA ---
        corpo = tk.Frame(self.container, bg='#393D6B')
        corpo.pack(expand=True, fill="both", padx=40)
        
        domanda_attuale = self.domande[self.indice_domanda]
        
        # # Immagine (se presente)
        # img_path = domanda_attuale.get('immagine', '').strip()
        # if img_path and os.path.exists(img_path):
        #     try:
        #         img = Image.open(img_path)
        #         img = img.resize((200, 150), Image.LANCZOS)
        #         self.photo = ImageTk.PhotoImage(img)
        #         #tk.Label(corpo, image=self.photo, bg='#393D6B').pack(pady=10)
        #     except: 
        #         pass

        # Testo Domanda
        colore_testo = "white"
        if self.modalita_revisione:
            data = self.risposte_utente.get(self.indice_domanda, "")
            corretta = domanda_attuale.get('risposta', "").upper()
            colore_testo = "green" if data == corretta else "red"

        tk.Label(corpo, text=f"DOMANDA {self.indice_domanda + 1} / {len(self.domande)}", 
                 bg='#393D6B', fg='yellow', font=("Arial", 12, "bold")).pack()
        
        tk.Label(corpo, text=domanda_attuale.get('domanda', ""), font=("Arial", 16), 
                 bg='#393D6B', fg=colore_testo, wraplength=600, justify="center").pack(pady=20)

        # --- INPUT ---
        self.var_risposta = tk.StringVar(value=self.risposte_utente.get(self.indice_domanda, ""))
        radio_frame = tk.Frame(corpo, bg='#393D6B')
        radio_frame.pack(pady=10)
        
        state = "disabled" if self.modalita_revisione else "normal"
        tk.Radiobutton(radio_frame, text="VERO", variable=self.var_risposta, value="VERO", font=("Arial", 12, "bold"), width=10, indicatoron=0, state=state).pack(side="left", padx=10)
        tk.Radiobutton(radio_frame, text="FALSO", variable=self.var_risposta, value="FALSO", font=("Arial", 12, "bold"), width=10, indicatoron=0, state=state).pack(side="left", padx=10)

        # --- NAVIGAZIONE ---
        nav = tk.Frame(self.container, bg='#393D6B')
        nav.pack(side="bottom", fill="x", pady=20)
        
        tk.Button(nav, text="<< Precedente", command=self.domanda_precedente, width=15).pack(side="left", padx=20)
        
        if self.indice_domanda < len(self.domande) - 1:
            tk.Button(nav, text="Successiva >>", command=self.domanda_successiva, width=15).pack(side="left")
        
        if not self.modalita_revisione:
            tk.Button(nav, text="INVIA QUIZ", bg="#4CAF50", fg="white", font=("bold"), command=self.conferma_invio, width=15).pack(side="right", padx=20)
        else:
            tk.Button(nav, text="FINE REVISIONE", command=self.mostra_risultato, width=15).pack(side="right", padx=20)

    def domanda_successiva(self):
        if not self.modalita_revisione:
            self.risposte_utente[self.indice_domanda] = self.var_risposta.get()
        if self.indice_domanda < len(self.domande) - 1:
            self.indice_domanda += 1
            self.schermata_quiz()

    def domanda_precedente(self):
        if not self.modalita_revisione:
            self.risposte_utente[self.indice_domanda] = self.var_risposta.get()
        if self.indice_domanda > 0:
            self.indice_domanda -= 1
            self.schermata_quiz()

    def aggiorna_timer(self):
        if self.timer_attivo and self.tempo_rimanente > 0:
            m, s = divmod(self.tempo_rimanente, 60)
            if hasattr(self, 'lbl_timer'):
                self.lbl_timer.config(text=f"Tempo rimasto: {m:02d}:{s:02d}")
            if hasattr(self, 'time_bar'):
                self.time_bar['value'] = self.tempo_rimanente
            self.tempo_rimanente -= 1
            self.after(1000, self.aggiorna_timer)
        elif self.tempo_rimanente <= 0 and self.timer_attivo:
            messagebox.showinfo("Tempo Scaduto", "Il tempo è terminato! Il quiz verrà inviato automaticamente.")
            self.mostra_risultato()

    def conferma_invio(self):
        self.risposte_utente[self.indice_domanda] = self.var_risposta.get()
        if messagebox.askyesno("Conferma", "Sei sicuro di voler consegnare il quiz?"):
            self.mostra_risultato()

    def mostra_risultato(self):
        self.timer_attivo = False
        self.reset_schermo()
        
        corrette = 0
        sbagliate = 0
        for i in range(len(self.domande)):
            data = self.risposte_utente.get(i, "").strip().upper()
            real = self.domande[i].get('risposta', "").strip().upper()
            if data == real: 
                corrette += 1
            else: 
                sbagliate += 1
        
        esito = "SUPERATO" if sbagliate <= 3 else "NON SUPERATO"
        colore = "green" if sbagliate <= 3 else "red"

        res_frame = tk.Frame(self.container, bg='#393D6B')
        res_frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(res_frame, text="RISULTATO FINALE", font=("Arial", 20, "bold"), bg='#393D6B', fg="white").pack(pady=10)
        tk.Label(res_frame, text=f"Candidato: {self.vnome.get()}", font=("Arial", 14), bg='#393D6B', fg="white").pack()
        tk.Label(res_frame, text=f"Risposte corrette: {corrette}", font=("Arial", 12), bg='#393D6B', fg="lightgreen").pack()
        tk.Label(res_frame, text=f"Risposte sbagliate: {sbagliate}", font=("Arial", 12), bg='#393D6B', fg="orange").pack()
        tk.Label(res_frame, text=f"Punteggio: {corrette}/{len(self.domande)}", font=("Arial", 14, "bold"), bg='#393D6B', fg="white").pack(pady=10)
        tk.Label(res_frame, text=f"ESAME {esito}", font=("Arial", 24, "bold"), bg='#393D6B', fg=colore).pack(pady=20)

        tk.Button(res_frame, text="RIVEDI LE RISPOSTE", width=25, command=self.avvia_revisione).pack(pady=5)
        tk.Button(res_frame, text="TORNA ALLA HOME", width=25, command=self.crea_widgets_home).pack(pady=5)
        tk.Button(res_frame, text="ESCI", width=25, fg="red", command=self.master.destroy).pack(pady=5)

    def avvia_revisione(self):
        self.modalita_revisione = True
        self.indice_domanda = 0
        self.schermata_quiz()

if __name__ == '__main__':
    root = tk.Tk()
    app = Patente(master=root)
    root.mainloop()
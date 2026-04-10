import tkinter as tk
from tkinter import messagebox, ttk
import csv
import random
from PIL import Image, ImageTk

class Patente(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Simulatore Quiz Patente')
        self.master.geometry('850x850')
        self.pack(expand=True, fill='both')

        # --- TEMA CROMATICO ---
        self.color_bg = '#0F172A'
        self.color_card = '#1E293B'
        self.color_accent = '#38BDF8'
        self.color_text = '#F8FAFC'
        self.color_btn_sim = '#0EA5E9'
        self.color_btn_exam = '#8B5CF6'
        self.color_btn_exit = '#EF4444'

        self.tot_domande = []
        self.domande = []
        self.indice_domanda = 0
        self.risposte = {}
        self.tempo_rimanente = 1800
        self.timer_attivo = 0 # Usato come intero 0/1
        self.mod_revisione = 0 # Usato come intero 0/1

        self.container = tk.Frame(self, bg=self.color_bg)
        self.container.pack(expand=True, fill='both')
        self.content_frame = tk.Frame(self.container, bg=self.color_bg)
        self.content_frame.pack(expand=True, fill='both')

        self.carica_domande()
        self.crea_widget()

    def carica_domande(self):
        try:
            with open('domande_patente.csv', mode='r', encoding='utf-8') as f:
                self.tot_domande = list(csv.DictReader(f))
        except Exception as e:
            print(f"Errore: {e}")

    def svuota_interfaccia(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.container, bg=self.color_bg)
        self.content_frame.pack(expand=True, fill='both')

    def crea_widget(self):
        self.svuota_interfaccia()
        self.timer_attivo = 0
        self.mod_revisione = 0
        
        inner = tk.Frame(self.content_frame, bg=self.color_bg)
        inner.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(inner, text='QUIZ PATENTE', bg=self.color_bg, fg=self.color_accent, font=('Helvetica', 32, 'bold')).pack(pady=30)
        
        self.vnome = tk.StringVar()
        tk.Entry(inner, textvariable=self.vnome, font=("Helvetica", 14), width=25, justify='center').pack(pady=15, ipady=8)

        # Pulsanti Menu
        tk.Button(inner, text='SIMULAZIONE LIBERA', bg=self.color_btn_sim, fg='white', width=35, height=2, command=lambda: self.avvia_quiz(0)).pack(pady=8)
        tk.Button(inner, text='ESAME (30 MIN)', bg=self.color_btn_exam, fg='white', width=35, height=2, command=lambda: self.avvia_quiz(1)).pack(pady=8)
        tk.Button(inner, text="ESCI", bg=self.color_btn_exit, fg='white', width=35, height=2, command=self.master.destroy).pack(pady=20)

    def avvia_quiz(self, usa_timer):
        nome = self.vnome.get().strip()
        if len(nome) == 0:
            messagebox.showwarning('Manca Nome', 'Inserisci il tuo nome')
            return
        
        # Selezione domande (minimo 30 o tutte)
        quantita = len(self.tot_domande)
        if quantita > 30:
            self.domande = random.sample(self.tot_domande, 30)
        else:
            self.domande = self.tot_domande
        
        self.indice_domanda = 0
        self.risposte = {}
        self.timer_attivo = usa_timer
        self.tempo_rimanente = 1800
        
        self.schermata_quiz()
        
        if usa_timer == 1:
            self.aggiorna_timer()

    def schermata_quiz(self):
        self.svuota_interfaccia()
        
        # Header
        header = tk.Frame(self.content_frame, bg="#020617", height=50)
        header.pack(fill="x")
        tk.Label(header, text=self.vnome.get().upper(), bg="#020617", fg=self.color_accent, font=("Helvetica", 11, "bold")).pack(side="left", padx=20)
        
        if self.timer_attivo == 1:
            self.lbl_timer = tk.Label(header, text="", font=("Helvetica", 12, "bold"), fg="#EF4444", bg="#020617")
            self.lbl_timer.pack(side="right", padx=20)

        # Area Domanda
        corpo = tk.Frame(self.content_frame, bg=self.color_card, padx=30, pady=20)
        corpo.pack(expand=True, fill="both", padx=50, pady=20)
        
        item = self.domande[self.indice_domanda]
        
        # Immagine
        img_path = item.get('immagine', "").strip()
        try:
            img = Image.open(img_path)
            img = img.resize((350, 220), Image.Resampling.LANCZOS)
            self.foto_tk = ImageTk.PhotoImage(img)
            tk.Label(corpo, image=self.foto_tk, bg=self.color_card).pack(pady=10)
        except:
            pass

        # Colore testo in revisione
        txt_color = self.color_text
        if self.mod_revisione == 1:
            scelta = self.risposte.get(self.indice_domanda, "")
            corretta = item.get('risposta', "").upper()
            if scelta == corretta:
                txt_color = "#22C55E"
            else:
                txt_color = "#F43F5E"

        tk.Label(corpo, text=item.get('domanda', ""), font=("Helvetica", 18), bg=self.color_card, fg=txt_color, wraplength=600).pack(pady=30)

        # Input
        self.var_risposta = tk.StringVar(value=self.risposte.get(self.indice_domanda, ""))
        radio_f = tk.Frame(corpo, bg=self.color_card)
        radio_f.pack(pady=10)
        
        tk.Radiobutton(radio_f, text="VERO", variable=self.var_risposta, value="VERO", indicatoron=0, width=12, font=("Helvetica", 12, "bold")).pack(side="left", padx=10)
        tk.Radiobutton(radio_f, text="FALSO", variable=self.var_risposta, value="FALSO", indicatoron=0, width=12, font=("Helvetica", 12, "bold")).pack(side="left", padx=10)

        # Navigazione
        nav = tk.Frame(self.content_frame, bg=self.color_bg)
        nav.pack(side="bottom", fill="x", pady=30)
        
        tk.Button(nav, text="<< INDIETRO", command=self.vai_indietro, width=15).pack(side="left", padx=50)
        
        # Gestione pulsante destro (Avanti o Fine)
        if self.indice_domanda < (len(self.domande) - 1):
            tk.Button(nav, text="AVANTI >>", command=self.vai_avanti, width=15).pack(side="left")
        
        if self.mod_revisione == 0:
            tk.Button(nav, text="CONSEGNA", bg="#22C55E", fg="white", command=self.consegna).pack(side="right", padx=50)
        else:
            tk.Button(nav, text="ESITO", bg=self.color_btn_exam, fg="white", command=self.mostra_risultato).pack(side="right", padx=50)

    def vai_avanti(self):
        if self.mod_revisione == 0:
            self.risposte[self.indice_domanda] = self.var_risposta.get()
        self.indice_domanda += 1
        self.schermata_quiz()

    def vai_indietro(self):
        if self.mod_revisione == 0:
            self.risposte[self.indice_domanda] = self.var_risposta.get()
        if self.indice_domanda > 0:
            self.indice_domanda -= 1
            self.schermata_quiz()

    def aggiorna_timer(self):
        if self.timer_attivo == 1:
            if self.tempo_rimanente > 0:
                m, s = divmod(self.tempo_rimanente, 60)
                self.lbl_timer.config(text=f"{m:02d}:{s:02d}")
                self.tempo_rimanente -= 1
                self.after(1000, self.aggiorna_timer)
            else:
                self.mostra_risultato()

    def consegna(self):
        self.risposte[self.indice_domanda] = self.var_risposta.get()
        if messagebox.askyesno("Fine", "Vuoi consegnare?"):
            self.mostra_risultato()

    def mostra_risultato(self):
        self.timer_attivo = 0
        self.svuota_interfaccia()
        
        corrette = 0
        totale_domande = len(self.domande)

        for i in range(totale_domande):
            # Prendiamo la risposta dell'utente (se non c'è, mettiamo "NON DATA")
            risposta_utente = self.risposte.get(i, "VUOTA").strip().upper()
            # Prendiamo la risposta corretta dal CSV
            risposta_corretta = self.domande[i].get('risposta', "").strip().upper()
            
            # Debug veloce in console (opzionale)
            # print(f"D{i}: Utente({risposta_utente}) - Corretta({risposta_corretta})")

            if risposta_utente == risposta_corretta:
                corrette += 1
        
        sbagliate = totale_domande - corrette
        
        # Logica esito: se non rispondi a nulla, corrette sarà 0, sbagliate sarà 30.
        esito = "BOCCIATO"
        color = "#F43F5E" # Rosso
        if corrette >= (totale_domande - 3): # Massimo 3 errori
            esito = "PROMOSSO"
            color = "#22C55E" # Verde

        res_frame = tk.Frame(self.content_frame, bg=self.color_card, padx=40, pady=40)
        res_frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(res_frame, text=esito, font=("Helvetica", 32, "bold"), bg=self.color_card, fg=color).pack(pady=20)
        tk.Label(res_frame, text=f"Risposte corrette: {corrette} / {totale_domande}", font=("Helvetica", 14), bg=self.color_card, fg="white").pack()
        tk.Label(res_frame, text=f"Errori: {sbagliate}", font=("Helvetica", 14), bg=self.color_card, fg="white").pack(pady=10)
        
        tk.Button(res_frame, text="RIVEDI ERRORI", command=self.attiva_revisione, width=20).pack(pady=10)
        tk.Button(res_frame, text="MENU PRINCIPALE", command=self.crea_widget, width=20).pack(pady=5)

    def attiva_revisione(self):
        self.mod_revisione = 1
        self.indice_domanda = 0
        self.schermata_quiz()

if __name__ == '__main__':
    root = tk.Tk()
    app = Patente(master=root)
    root.mainloop()
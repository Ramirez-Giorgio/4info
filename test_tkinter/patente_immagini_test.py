import tkinter as tk
from tkinter import messagebox
import csv
import random
from PIL import Image, ImageTk

class Patente(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Simulatore Quiz Patente')
        self.master.geometry('800x800')
        self.pack(expand=True, fill='both')

        # Palette Colori
        self.color_bg = '#1A1B26'
        self.color_card = '#24283B'
        self.color_accent = '#7AA2F7'
        self.color_text = '#C0CAF5'
        self.color_correct = '#9ECE6A'
        self.color_wrong = '#F7768E'

        self.tot_domande = []
        self.domande = []
        self.indice_domanda = 0
        self.risposte = {}
        self.max_tempo = 1800
        self.tempo_rimanente = 1800
        self.timer_attivo = 0
        self.mod_revisione = 0

        self.container = tk.Frame(self, bg=self.color_bg)
        self.container.pack(expand=True, fill='both')

        self.carica_domande()
        self.crea_widget()

    def carica_domande(self):
        try:
            with open('domande_patente.csv', mode='r', encoding='utf-8') as f:
                righe = []
                for riga in f:
                    if riga.strip():
                        righe.append(riga)
            
            if not righe:
                return
                
            reader = csv.DictReader(righe, delimiter=',')
            nuovi_nomi = []
            for n in reader.fieldnames:
                nuovi_nomi.append(n.strip().lower())
            reader.fieldnames = nuovi_nomi
            self.tot_domande = list(reader)
        except Exception as e:
            print(f"Errore caricamento CSV: {e}")

    def reset_schermo(self):
        # Reset senza l'uso di winfo_children
        for widget in list(self.container.children.values()):
            widget.destroy()

    def crea_widget(self):
        self.reset_schermo()
        self.timer_attivo = 0
        self.mod_revisione = 0
        
        inner = tk.Frame(self.container, bg=self.color_card)
        inner.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(inner, text='SIMULATORE QUIZ', bg=self.color_card, fg=self.color_accent, font=('Arial', 24, 'bold')).pack(pady=20, padx=20)
        
        self.vnome = tk.StringVar()
        tk.Entry(inner, textvariable=self.vnome, font=("Arial", 14), width=25, justify='center').pack(pady=10)

        btn_opt = {'width': 30, 'height': 2, 'font': ('Arial', 10, 'bold'), 'relief': 'flat', 'cursor': 'hand2'}
        
        tk.Button(inner, text='SIMULAZIONE LIBERA', bg='#419DFF', fg='white', command=lambda: self.avvia_quiz(0), **btn_opt).pack(pady=5)
        tk.Button(inner, text='ESAME (30 MIN)', bg='#2AC3DE', fg='white', command=lambda: self.avvia_quiz(1), **btn_opt).pack(pady=5)
        tk.Button(inner, text="ESCI", bg=self.color_card, fg=self.color_wrong, command=self.master.destroy, **btn_opt).pack(pady=10)

    def avvia_quiz(self, con_timer):
        if not self.vnome.get().strip():
            messagebox.showwarning('Manca Nome', 'Inserisci il tuo nome')
            return
        
        n_estrazione = min(30, len(self.tot_domande))
        self.domande = random.sample(self.tot_domande, n_estrazione)
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
        
        # --- HEADER ---
        header = tk.Frame(self.container, bg='#16161E', height=50)
        header.pack(fill="x")
        tk.Label(header, text=f"Candidato: {self.vnome.get().upper()}", bg='#16161E', fg=self.color_accent, font=("Arial", 10, "bold")).pack(side="left", padx=20)
        
        if self.timer_attivo == 1:
            self.lbl_timer = tk.Label(header, text="", font=("Arial", 12, "bold"), fg='#BB9AF7', bg='#16161E')
            self.lbl_timer.pack(side="right", padx=20)

        # Info progresso
        risposte_date = len(self.risposte)
        testo_progresso = f"Domanda {self.indice_domanda + 1} di {len(self.domande)} | Risposte date: {risposte_date}"
        tk.Label(self.container, text=testo_progresso, bg=self.color_bg, fg=self.color_text, font=("Arial", 9)).pack(pady=10)

        # --- CORPO ---
        corpo = tk.Frame(self.container, bg=self.color_card, padx=20, pady=20)
        corpo.pack(expand=True, fill="both", padx=60, pady=10)
        
        domanda_attuale = self.domande[self.indice_domanda]
        
        # --- LOGICA IMMAGINE (CORRETTA) ---
        img_nome = domanda_attuale.get('img', "").strip()
        if img_nome:
            try:
                percorso = f"immagini/{img_nome}"
                img_pil = Image.open(percorso)
                
                # IMPORTANTE: salviamo in self.foto_quiz per non farla sparire
                self.foto_quiz = ImageTk.PhotoImage(img_pil)
                
                # Creiamo la label e assegniamo l'immagine
                lbl_img = tk.Label(corpo, image=self.foto_quiz, bg=self.color_card)
                lbl_img.pack(pady=10)
                
            except Exception as e:
                # Se l'immagine non si vede, questo errore ti dice perché nel terminale
                print(f"ERRORE: Impossibile caricare {img_nome}. Dettaglio: {e}")
                tk.Label(corpo, text="[Immagine non trovata]", fg="red", bg=self.color_card).pack()

        # Testo Domanda
        txt_col = "#FFFFFF"
        if self.mod_revisione == 1:
            u = self.risposte.get(self.indice_domanda, "").strip().upper()
            c = domanda_attuale.get('risposta', "").strip().upper()
            txt_col = self.color_correct if u == c else self.color_wrong

        tk.Label(corpo, text=domanda_attuale.get('domanda', ""), font=("Arial", 16), 
                 bg=self.color_card, fg=txt_col, wraplength=550, justify="center").pack(pady=20)

        # Scelte
        self.var_risposta = tk.StringVar(value=self.risposte.get(self.indice_domanda, ""))
        radio_f = tk.Frame(corpo, bg=self.color_card)
        radio_f.pack(pady=20)
        
        rb_style = {'indicatoron': 0, 'width': 14, 'height': 2, 'bg': self.color_accent, 'selectcolor': '#3D59A1', 'fg': 'white', 'font': ('Arial', 11, 'bold'), 'cursor': 'hand2'}
        tk.Radiobutton(radio_f, text="VERO", variable=self.var_risposta, value="VERO", **rb_style).pack(side="left", padx=20)
        tk.Radiobutton(radio_f, text="FALSO", variable=self.var_risposta, value="FALSO", **rb_style).pack(side="left", padx=20)

        # Navigazione
        nav = tk.Frame(self.container, bg=self.color_bg)
        nav.pack(side="bottom", fill="x", pady=30)
        
        btn_nav = {'width': 15, 'bg': '#414868', 'fg': 'white', 'relief': 'flat', 'cursor': 'hand2'}
        tk.Button(nav, text="<< INDIETRO", command=self.salva_e_indietro, **btn_nav).pack(side="left", padx=50)
        
        if self.indice_domanda < len(self.domande) - 1:
            tk.Button(nav, text="AVANTI >>", command=self.salva_e_avanti, **btn_nav).pack(side="left")
        
        if self.mod_revisione == 0:
            tk.Button(nav, text="CONSEGNA", bg=self.color_correct, fg=self.color_bg, font=("Arial", 10, "bold"), command=self.conferma_invio, width=15, relief='flat').pack(side="right", padx=50)
        else:
            tk.Button(nav, text="FINE REVISIONE", bg=self.color_accent, fg="white", command=self.mostra_risultato, width=15, relief='flat').pack(side="right", padx=50)

    def salva_e_avanti(self):
        if self.mod_revisione == 0:
            self.risposte[self.indice_domanda] = self.var_risposta.get()
        if self.indice_domanda < len(self.domande) - 1:
            self.indice_domanda += 1
            self.schermata_quiz()

    def salva_e_indietro(self):
        if self.mod_revisione == 0:
            self.risposte[self.indice_domanda] = self.var_risposta.get()
        if self.indice_domanda > 0:
            self.indice_domanda -= 1
            self.schermata_quiz()

    def aggiorna_timer(self):
        if self.timer_attivo == 1 and self.tempo_rimanente > 0:
            m, s = divmod(self.tempo_rimanente, 60)
            if hasattr(self, 'lbl_timer'):
                self.lbl_timer.config(text=f"{m:02d}:{s:02d}")
            self.tempo_rimanente -= 1
            self.after(1000, self.aggiorna_timer)
        else:
            if self.timer_attivo == 1:
                self.mostra_risultato()

    def conferma_invio(self):
        self.risposte[self.indice_domanda] = self.var_risposta.get()
        if messagebox.askyesno("Conferma", "Concludere il test?"):
            self.mostra_risultato()

    def mostra_risultato(self):
        self.timer_attivo = 0
        self.reset_schermo()
        corrette = 0
        for i, d in enumerate(self.domande):
            risposta_utente = self.risposte.get(i, "").strip().upper()
            risposta_vera = d.get('risposta', "").strip().upper()
            if risposta_utente == risposta_vera and risposta_utente != "":
                corrette += 1
        sbagliate = len(self.domande) - corrette
        esito = "PROMOSSO" if sbagliate <= 3 else "BOCCIATO"
        col = self.color_correct if esito == "PROMOSSO" else self.color_wrong
        res_f = tk.Frame(self.container, bg=self.color_card, padx=40, pady=40)
        res_f.place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(res_f, text=esito, font=("Arial", 30, "bold"), bg=self.color_card, fg=col).pack(pady=10)
        tk.Label(res_f, text=f"Errori: {sbagliate}", font=("Arial", 14), bg=self.color_card, fg=self.color_text).pack()
        tk.Button(res_f, text="REVISIONA", width=20, bg=self.color_accent, fg='white', command=self.avvia_revisione).pack(pady=10)
        tk.Button(res_f, text="HOME", width=20, bg='#414868', fg='white', command=self.crea_widget).pack()

    def avvia_revisione(self):
        self.mod_revisione = 1
        self.indice_domanda = 0
        self.schermata_quiz()

if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(800, 700)
    app = Patente(master=root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox, ttk
import csv
import random
from PIL import Image, ImageTk # Assicurati di avere 'Pillow' installato

class Patente(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Simulatore Quiz Patente con Immagini')
        self.master.geometry('800x850') # Aumentata leggermente l'altezza per le foto
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
        self.max_tempo = 120 #1800
        self.tempo_rimanente = 120 #1800
        self.timer_attivo = 0
        self.mod_revisione = 0

        self.container = tk.Frame(self, bg=self.color_bg)
        self.container.pack(expand=True, fill='both')

        self.carica_domande()
        self.crea_widget()

    def carica_domande(self):
        try:
            with open('domande_patente.csv', mode='r', encoding='utf-8') as f:
                righe = [riga for riga in f if riga.strip()]
            if not righe: return
            
            # Leggiamo il CSV (domanda,risposta,img)
            reader = csv.DictReader(righe, delimiter=',')
            reader.fieldnames = [n.strip().lower() for n in reader.fieldnames]
            self.tot_domande = list(reader)
        except Exception as e:
            messagebox.showerror("Errore CSV", f"Controlla il file CSV: {e}")

    def reset_schermo(self):
        for widget in self.container.winfo_children():
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
        if con_timer == 1: self.aggiorna_timer()

    def schermata_quiz(self):
        self.reset_schermo()
        
        # --- HEADER ---
        header = tk.Frame(self.container, bg='#16161E', height=50)
        header.pack(fill="x")
        tk.Label(header, text=f"Candidato: {self.vnome.get().upper()}", bg='#16161E', fg=self.color_accent, font=("Arial", 10, "bold")).pack(side="left", padx=20)
        
        if self.timer_attivo == 1:
            self.lbl_timer = tk.Label(header, text="", font=("Arial", 12, "bold"), fg='#BB9AF7', bg='#16161E')
            self.lbl_timer.pack(side="right", padx=20)

        # --- PROGRESS BARS ---
        if self.timer_attivo == 1:
            self.time_bar = ttk.Progressbar(self.container, maximum=self.max_tempo, length=600)
            self.time_bar.pack(fill="x", padx=100, pady=(10, 0))
            self.time_bar['value'] = self.tempo_rimanente

        total_d = len(self.domande)
        risposte_date = len(self.risposte)
        prog_val = (risposte_date / total_d) * 100 if total_d > 0 else 0
        pb = ttk.Progressbar(self.container, length=600, value=prog_val)
        pb.pack(fill="x", padx=100, pady=5)

        # --- CORPO DOMANDA ---
        corpo = tk.Frame(self.container, bg=self.color_card, padx=20, pady=10)
        corpo.pack(expand=True, fill="both", padx=60, pady=10)
        
        domanda_attuale = self.domande[self.indice_domanda]
        
        # --- LOGICA IMMAGINE ---
        # Prende il nome dalla colonna 'img' del CSV
        img_nome = domanda_attuale.get('img', "").strip()
        if img_nome:
            try:
                percorso = f"immagini/{img_nome}"
                img_aperta = Image.open(percorso)
                # Ridimensiona l'immagine per farla stare bene (max 300px altezza)
                img_aperta.thumbnail((400, 250), Image.Resampling.LANCZOS)
                self.foto_tk = ImageTk.PhotoImage(img_aperta)
                tk.Label(corpo, image=self.foto_tk, bg=self.color_card).pack(pady=5)
            except:
                tk.Label(corpo, text="[Immagine non trovata]", fg="gray", bg=self.color_card).pack()

        # Testo Domanda
        txt_col = "#FFFFFF"
        if self.mod_revisione == 1:
            u = self.risposte.get(self.indice_domanda, "").strip().upper()
            c = domanda_attuale.get('risposta', "").strip().upper()
            txt_col = self.color_correct if u == c else self.color_wrong

        tk.Label(corpo, text=f"DOMANDA {self.indice_domanda + 1}", bg=self.color_card, fg='#E0AF68', font=("Arial", 11, "bold")).pack()
        tk.Label(corpo, text=domanda_attuale.get('domanda', ""), font=("Arial", 16), bg=self.color_card, fg=txt_col, wraplength=550, justify="center").pack(pady=10)

        # Scelte
        self.var_risposta = tk.StringVar(value=self.risposte.get(self.indice_domanda, ""))
        radio_f = tk.Frame(corpo, bg=self.color_card)
        radio_f.pack(pady=10)
        
        tk.Radiobutton(radio_f, text="VERO", variable=self.var_risposta, value="VERO", indicatoron=0, width=12, height=2, bg=self.color_accent, selectcolor='#3D59A1', fg='white', font=('Arial', 10, 'bold')).pack(side="left", padx=15)
        tk.Radiobutton(radio_f, text="FALSO", variable=self.var_risposta, value="FALSO", indicatoron=0, width=12, height=2, bg=self.color_accent, selectcolor='#3D59A1', fg='white', font=('Arial', 10, 'bold')).pack(side="left", padx=15)

        # --- NAVIGAZIONE ---
        nav = tk.Frame(self.container, bg=self.color_bg)
        nav.pack(side="bottom", fill="x", pady=20)
        
        tk.Button(nav, text="<< INDIETRO", command=self.salva_e_indietro, width=15, bg='#414868', fg='white', relief='flat').pack(side="left", padx=50)
        
        if self.indice_domanda < total_d - 1:
            tk.Button(nav, text="AVANTI >>", command=self.salva_e_avanti, width=15, bg='#414868', fg='white', relief='flat').pack(side="left")
        
        if self.mod_revisione == 0:
            tk.Button(nav, text="CONSEGNA", bg=self.color_correct, fg=self.color_bg, font=("Arial", 10, "bold"), command=self.conferma_invio, width=15, relief='flat').pack(side="right", padx=50)
        else:
            tk.Button(nav, text="FINE", bg=self.color_accent, fg="white", command=self.mostra_risultato, width=15, relief='flat').pack(side="right", padx=50)

    def salva_e_avanti(self):
        if self.mod_revisione == 0: self.risposte[self.indice_domanda] = self.var_risposta.get()
        if self.indice_domanda < len(self.domande)-1:
            self.indice_domanda += 1
            self.schermata_quiz()

    def salva_e_indietro(self):
        if self.mod_revisione == 0: self.risposte[self.indice_domanda] = self.var_risposta.get()
        if self.indice_domanda > 0:
            self.indice_domanda -= 1
            self.schermata_quiz()

    def aggiorna_timer(self):
        if self.timer_attivo == 1 and self.tempo_rimanente > 0:
            m, s = divmod(self.tempo_rimanente, 60)
            self.lbl_timer.config(text=f"{m:02d}:{s:02d}")
            if hasattr(self, 'time_bar'): self.time_bar['value'] = self.tempo_rimanente
            self.tempo_rimanente -= 1
            self.after(1000, self.aggiorna_timer)
        elif self.timer_attivo == 1:
            self.mostra_risultato()

    def conferma_invio(self):
        self.risposte[self.indice_domanda] = self.var_risposta.get()
        if messagebox.askyesno("Conferma", "Vuoi consegnare il quiz?"):
            self.mostra_risultato()

    def mostra_risultato(self):
        self.timer_attivo = 0
        self.reset_schermo()
        corrette = sum(1 for i, d in enumerate(self.domande) if self.risposte.get(i, "").strip().upper() == d.get('risposta', "").strip().upper() and self.risposte.get(i, "") != "")
        sbagliate = len(self.domande) - corrette
        esito = "PROMOSSO" if sbagliate <= 3 else "BOCCIATO"
        col = self.color_correct if esito == "PROMOSSO" else self.color_wrong

        res_f = tk.Frame(self.container, bg=self.color_card, padx=40, pady=40)
        res_f.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(res_f, text=esito, font=("Arial", 30, "bold"), bg=self.color_card, fg=col).pack(pady=10)
        tk.Label(res_f, text=f"Errori commessi: {sbagliate}", font=("Arial", 14), bg=self.color_card, fg=self.color_text).pack()
        
        tk.Button(res_f, text="REVISIONA ERRORI", width=20, bg=self.color_accent, fg='white', command=self.avvia_revisione).pack(pady=10)
        tk.Button(res_f, text="TORNA AL MENU", width=20, bg='#414868', fg='white', command=self.crea_widget).pack()

    def avvia_revisione(self):
        self.mod_revisione = 1
        self.indice_domanda = 0
        self.schermata_quiz()

if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(800, 750)
    app = Patente(master=root)
    root.mainloop()
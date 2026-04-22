import tkinter as tk
from tkinter import messagebox

class Prenotazione:
    def __init__(self, nome, eta, telefono, visite, priorita):
        self.nome = nome
        self.eta = eta
        self.telefono = telefono
        self.visite = visite  # Questa sarà una stringa formattata
        self.priorita = priorita

    def __str__(self):
        return self.nome + " - " + self.visite + " - " + self.priorita

class GestionePrenotazioni:
    def __init__(self, root):
        self.root = root
        self.root.title("Studio Medico - Gestione")
        self.root.geometry("600x700")
        
        # Lista per memorizzare gli oggetti Prenotazione
        self.archivio = []
        
        # --- Interfaccia Grafica ---
        # Titolo
        self.lbl_titolo = tk.Label(root, text="GESTIONE PRENOTAZIONI", font=("Arial", 16, "bold"))
        self.lbl_titolo.pack(pady=10)

        # Frame Dati Paziente
        self.f_dati = tk.LabelFrame(root, text=" Dati Paziente ")
        self.f_dati.pack(padx=20, fill="x")

        tk.Label(self.f_dati, text="Nome e Cognome:").pack()
        self.ent_nome = tk.Entry(self.f_dati, width=40)
        self.ent_nome.pack()

        tk.Label(self.f_dati, text="Età:").pack()
        self.ent_eta = tk.Entry(self.f_dati, width=10)
        self.ent_eta.pack()

        tk.Label(self.f_dati, text="Telefono:").pack()
        self.ent_tel = tk.Entry(self.f_dati, width=20)
        self.ent_tel.pack()

        # Checkbox Visite
        self.f_visite = tk.LabelFrame(root, text=" Tipologia Visita ")
        self.f_visite.pack(padx=20, fill="x", pady=10)

        self.v1 = tk.BooleanVar()
        self.v2 = tk.BooleanVar()
        self.v3 = tk.BooleanVar()
        self.v4 = tk.BooleanVar()

        tk.Checkbutton(self.f_visite, text="Generale", variable=self.v1).pack(side="left")
        tk.Checkbutton(self.f_visite, text="Cardiologia", variable=self.v2).pack(side="left")
        tk.Checkbutton(self.f_visite, text="Dermatologia", variable=self.v3).pack(side="left")
        tk.Checkbutton(self.f_visite, text="Ortopedia", variable=self.v4).pack(side="left")

        # Radiobutton Priorità
        self.f_prio = tk.LabelFrame(root, text=" Priorità ")
        self.f_prio.pack(padx=20, fill="x")

        self.var_prio = tk.StringVar(value="Normale")
        tk.Radiobutton(self.f_prio, text="Normale", variable=self.var_prio, value="Normale").pack(side="left")
        tk.Radiobutton(self.f_prio, text="Urgente", variable=self.var_prio, value="Urgente").pack(side="left")
        tk.Radiobutton(self.f_prio, text="Molto urgente", variable=self.var_prio, value="Molto urgente").pack(side="left")

        # Pulsanti
        self.btn_prenota = tk.Button(root, text="Prenota Visita", command=self.aggiungi)
        self.btn_prenota.pack(pady=5)

        self.btn_elimina = tk.Button(root, text="Elimina Selezionata", command=self.elimina)
        self.btn_elimina.pack(pady=2)

        self.btn_salva = tk.Button(root, text="Salva su File", command=self.salva)
        self.btn_salva.pack(pady=2)

        self.btn_carica = tk.Button(root, text="Carica da File", command=self.carica)
        self.btn_carica.pack(pady=2)

        self.btn_pulisci = tk.Button(root, text="Pulisci Tutto", command=self.pulisci_interfaccia)
        self.btn_pulisci.pack(pady=2)

        # Ricerca
        tk.Label(root, text="Cerca per nome:").pack()
        self.ent_cerca = tk.Entry(root)
        self.ent_cerca.pack()
        tk.Button(root, text="Cerca", command=self.cerca).pack()

        # Listbox
        self.lista_box = tk.Listbox(root, width=60)
        self.lista_box.pack(pady=10)

        # Stato
        self.lbl_totale = tk.Label(root, text="Totale prenotazioni: 0")
        self.lbl_totale.pack()

    def aggiungi(self):
        nome = self.ent_nome.get()
        eta = self.ent_eta.get()
        tel = self.ent_tel.get()
        prio = self.var_prio.get()
        
        # Recupero visite selezionate
        scelte = []
        if self.v1.get(): 
            scelte.append("Generale")
        if self.v2.get(): 
            scelte.append("Cardiologia")
        if self.v3.get(): 
            scelte.append("Dermatologia")
        if self.v4.get(): 
            scelte.append("Ortopedia")

        if nome == "" or eta == "" or tel == "" or len(scelte) == 0:
            messagebox.showwarning("Errore", "Compila tutti i campi!")
            return

        visite_str = ", ".join(scelte)
        nuova_p = Prenotazione(nome, eta, tel, visite_str, prio)
        
        self.archivio.append(nuova_p)
        self.aggiorna_lista_grafica()
        self.pulisci_campi_input()

    def elimina(self):
        indice = self.lista_box.curselection()
        if not indice:
            messagebox.showwarning("Attenzione", "Seleziona una riga!")
            return
        
        conferma = messagebox.askyesno("Conferma", "Vuoi davvero eliminare?")
        if conferma:
            pos = indice[0]
            self.archivio.pop(pos)
            self.aggiorna_lista_grafica()

    def aggiorna_lista_grafica(self):
        self.lista_box.delete(0, tk.END)
        contatore = 0
        for p in self.archivio:
            testo = str(p)
            self.lista_box.insert(tk.END, testo)
            
            # Colore in base alla priorità
            if p.priorita == "Molto urgente":
                self.lista_box.itemconfig(contatore, fg="red")
            elif p.priorita == "Urgente":
                self.lista_box.itemconfig(contatore, fg="orange")
            else:
                self.lista_box.itemconfig(contatore, fg="green")
            contatore = contatore + 1
        
        self.lbl_totale.config(text="Totale prenotazioni: " + str(len(self.archivio)))

    def salva(self):
        f = open("prenotazioni.txt", "w")
        for p in self.archivio:
            riga = p.nome + "|" + p.visite + "|" + p.priorita + "|" + p.eta + "|" + p.telefono + "\n"
            f.write(riga)
        f.close()
        messagebox.showinfo("Salvataggio", "Dati salvati con successo!")

    def carica(self):
        try:
            f = open("prenotazioni.txt", "r")
            self.archivio = []
            for riga in f:
                riga = riga.strip()
                dati = riga.split("|")
                if len(dati) == 5:
                    p_caricata = Prenotazione(dati[0], dati[3], dati[4], dati[1], dati[2])
                    self.archivio.append(p_caricata)
            f.close()
            self.aggiorna_lista_grafica()
        except FileNotFoundError:
            messagebox.showerror("Errore", "File non trovato!")

    def cerca(self):
        nome_cercato = self.ent_cerca.get().lower()
        self.lista_box.selection_clear(0, tk.END)
        
        indice = 0
        for p in self.archivio:
            if nome_cercato in p.nome.lower():
                self.lista_box.selection_set(indice)
                self.lista_box.see(indice)
            indice = indice + 1

    def pulisci_campi_input(self):
        self.ent_nome.delete(0, tk.END)
        self.ent_eta.delete(0, tk.END)
        self.ent_tel.delete(0, tk.END)
        self.v1.set(False)
        self.v2.set(False)
        self.v3.set(False)
        self.v4.set(False)
        self.var_prio.set("Normale")

    def pulisci_interfaccia(self):
        conferma = messagebox.askyesno("Conferma", "Vuoi svuotare tutto l'archivio?")
        if conferma:
            self.archivio = []
            self.aggiorna_lista_grafica()
            self.pulisci_campi_input()

if __name__ == "__main__":
    finestra = tk.Tk()
    app = GestionePrenotazioni(finestra)
    finestra.mainloop()
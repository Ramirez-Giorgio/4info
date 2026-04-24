import tkinter as tk
from tkinter import messagebox

class Prenotazione:
    def __init__(self, nome, eta, telefono, visite, priorita):
        self.nome = nome
        self.eta = eta
        self.telefono = telefono
        self.visite = visite
        self.priorita = priorita



class Gestione_Prenotazioni:
    def __init__(self, root):
       self.root = root
       self.root.title("gestione prenotazioni")
       self.root.geometry("800x650")

       self.elenco_prenotazioni = []

       self.crea_interfaccia()
       self.aggiorna_lista()


    def crea_interfaccia(self):

        frame_sx = tk.Frame(self.root)
        frame_sx.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20, )

        frame_dx = tk.Frame(self.root)
        frame_dx.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        frame_logo = tk.Frame(frame_sx)
        frame_logo.pack(anchor="w", pady=(0, 10))

        try:
            self.logo_img = tk.PhotoImage(file="./logo.png")
            self.logo_img = self.logo_img.subsample(4, 4) 
            tk.Label(frame_logo, image=self.logo_img).pack(side=tk.LEFT)
        except:
            tk.Label(frame_logo, text="[LOGO ASSENTE]").pack(side=tk.LEFT)

        tk.Label(frame_logo, text="Studio Medico", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=10)


        tk.Label(frame_sx,  text="Nuova prenotazione").pack(pady=(0,10))
        tk.Label(frame_sx,  text="Nome e Cognome").pack(anchor="w")

        self.entry_nome = tk.Entry(frame_sx, width=30)
        self.entry_nome.pack(pady=(0,10))

        tk.Label(frame_sx,  text="Età").pack(anchor="w")
        self.entry_eta = tk.Entry(frame_sx, width=30)
        self.entry_eta.pack(pady=(0,10))

        tk.Label(frame_sx,  text="Telefono").pack(anchor="w")
        self.entry_telefono = tk.Entry(frame_sx, width=30)
        self.entry_telefono.pack(pady=(0,10))



        tk.Label(frame_sx,  text="Visite").pack(anchor="w", pady=(10,0))

        self.var_gen = tk.BooleanVar()
        self.var_cardio = tk.BooleanVar()
        self.var_derma = tk.BooleanVar()
        self.var_orto = tk.BooleanVar()

        tk.Checkbutton(frame_sx, text="Visita generale", variable = self.var_gen).pack(anchor="w")
        tk.Checkbutton(frame_sx, text="Cardiologia", variable = self.var_cardio).pack(anchor="w")
        tk.Checkbutton(frame_sx, text="Dermatologica", variable = self.var_derma).pack(anchor="w")
        tk.Checkbutton(frame_sx, text="Ortopedia",  variable=self.var_orto).pack(anchor="w")

        tk.Label(frame_sx,  text="Priorità").pack(anchor="w", pady=(10,0))

        self.var_prio = tk.StringVar(value="Normale")
        tk.Radiobutton(frame_sx, text="Normale", variable = self.var_prio, value="Normale").pack(anchor="w")
        tk.Radiobutton(frame_sx, text="urgente", variable = self.var_prio, value="Urgente").pack(anchor="w")
        tk.Radiobutton(frame_sx, text="Molto Urgente", variable = self.var_prio, value="Molto Urgente").pack(anchor="w")

        tk.Button(frame_sx, text="Prenota Visita", command=self.prenota_visita).pack()
        tk.Button(frame_sx, text="Salva su file", command=self.salva_file).pack()
        tk.Button(frame_sx, text="Carica da file", command=self.carica_file).pack()
        tk.Button(frame_sx, text="Pulisci tutto", command=self.pulisci_tutto).pack()

        tk.Label(frame_dx,  text="Elenco Prenotazioni").pack(pady=(0,10))

        frame_ricerca = tk.Frame(frame_dx)
        frame_ricerca.pack(fill=tk.X, pady=(0,10))

        tk.Label(frame_ricerca, text="Ricerca").pack(anchor="w")

        self.entry_cerca = tk.Entry(frame_ricerca, width=30)
        self.entry_cerca.pack(side=tk.LEFT, padx=(0,10))

        tk.Button(frame_ricerca, text="cerca", command=self.ricerca).pack(side=tk.LEFT, padx=(0,5))
        tk.Button(frame_ricerca, text="mostra tutto", command=self.aggiorna_lista).pack(side=tk.LEFT)

        self.box_lista = tk.Listbox(frame_dx)
        self.box_lista.pack(fill=tk.BOTH, expand=True, pady=(0,10))
        
        tk.Button(frame_dx, text="Elimina selezionata", command=self.elimina_selezionata).pack(fill=tk.X)
        tk.Button(frame_dx, text="elimina tutto", command=self.elimina_tutto ,bg="orange").pack(fill=tk.X)

        self.label_totale = tk.Label(frame_dx, text="Totale prenotazioni: 0")
        self.label_totale.pack(pady=10)

    def prenota_visita(self):
        nome = self.entry_nome.get()
        eta = self.entry_eta.get()
        tel = self.entry_telefono.get()
        prio = self.var_prio.get()

        visite_scelte = []

        if self.var_gen.get():
             visite_scelte.append("Generale")
        if self.var_cardio.get():
             visite_scelte.append("Cardiologica")
        if self.var_derma.get():
             visite_scelte.append("Dermatologica")
        if self.var_orto.get():
             visite_scelte.append("Ortopedica")

        if nome == "" or len(visite_scelte) == 0 :
            messagebox.showwarning("Attenzione", "inserire almeno il nome e una visita")
            return
        
        nuova_prenotazione = Prenotazione(nome, eta, tel, visite_scelte, prio)

        self.elenco_prenotazioni.append(nuova_prenotazione)


        self.entry_nome.delete(0, tk.END)
        self.entry_eta.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_cerca.delete(0, tk.END)

        self.var_gen.set(False)
        self.var_cardio.set(False)
        self.var_derma.set(False)
        self.var_orto.set(False)
        self.var_prio.set("Normale")

        self.aggiorna_lista()



    def elimina_selezionata(self):

        if not messagebox.askyesno("Conferma", "sei sicuro di eliminare questa riga?"):
             return

        riga_sel = self.box_lista.curselection() 
        if not riga_sel:
            messagebox.showwarning("Attenzione", "selezionare una prenotazione da eliminare")
            return
        self.elenco_prenotazioni.pop(riga_sel[0])
        self.aggiorna_lista()



    def salva_file(self):

        if len(self.elenco_prenotazioni)== 0:
            messagebox.showwarning("Attenzione", "non ci sono prenotazioni")
            return

        file_salvataggio = open("prenotazioni.txt", "w")

        for pren in self.elenco_prenotazioni:

            visite_testo = ", ".join(pren.visite)

            riga_salvare = f"{pren.nome}|{pren.eta}|{pren.telefono}|{visite_testo}|{pren.priorita}\n"

            file_salvataggio.write(riga_salvare)
        file_salvataggio.close()

        messagebox.showinfo("Successo", "Dati salvati correttamente nel file prenotazioni.txt")


    def carica_file(self):
        try:
            with open("prenotazioni.txt", "r") as f:
                righe = f.readlines()
                self.elenco_prenotazioni =[]
                for riga in righe:
                    riga_pulita = riga.strip().split("|")
                    name = riga_pulita[0]
                    age = riga_pulita[1]
                    phone = riga_pulita[2]
                    checks = riga_pulita[3].split(",") 
                    priority = riga_pulita[4]

                    new_check = Prenotazione(name, age, phone, checks, priority)
                    self.elenco_prenotazioni.append(new_check)

                self.aggiorna_lista()
                messagebox.showinfo("Successo", "Dati caricati correttamente!")
        except Exception as e:
            messagebox.showerror("errore", f"Errore durante il caricamento: {e}")


    def pulisci_tutto(self):
        if messagebox.askyesno("conferma", "vuoi pulire l'intera schermata?"):
            self.entry_nome.delete(0, tk.END)
            self.entry_eta.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_cerca.delete(0, tk.END)

            self.var_gen.set(False)
            self.var_cardio.set(False)
            self.var_derma.set(False)
            self.var_orto.set(False)
            self.var_prio.set("Normale")
            
            self.elenco_prenotazioni = []
            self.aggiorna_lista()
    

        



    def elimina_tutto(self):
        if not messagebox.askyesno("Conferma", "sei sicuro di eliminare tutto?"):
             return

        self.elenco_prenotazioni = []
        self.aggiorna_lista()


    def ricerca(self):
        parametro = self.entry_cerca.get()
        self.aggiorna_lista(parametro)



    def aggiorna_lista(self, filtro=""):
        self.box_lista.delete(0, tk.END)

        for pren in self.elenco_prenotazioni:
            
            if filtro.lower() in pren.nome.lower():

                visite_testo = ", ".join(pren.visite)
                testo_riga = f"{pren.nome} - {visite_testo} - {pren.priorita}"
                if pren.priorita == "Normale":
                    colore = "#99FF99"
                elif pren.priorita == "Urgente":
                    colore = "#FCBF82"
                else:
                    colore = "#FF7575"
                
                self.box_lista.insert(tk.END, testo_riga)
                index = self.box_lista.size() - 1
                self.box_lista.itemconfig(index ,bg=colore)

        self.label_totale.config(text=f"Totale prenotazioni: {len(self.elenco_prenotazioni)}")

    

    



def main():
    finestra_principale = tk.Tk()
    applicazione = Gestione_Prenotazioni(finestra_principale)
    finestra_principale.mainloop()

    
if __name__=="__main__":
        main()




    
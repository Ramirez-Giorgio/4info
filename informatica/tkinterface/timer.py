#TIMER di 20 minuti che si avvia in automatico all'apertura della finestra:
import tkinter as tk

TEMPO = 20 * 60 # 1200 secondi
tempo_rimanente = TEMPO

def conto_alla_rovescia():
    global tempo_rimanente
    if tempo_rimanente >= 0:
        ore, resto = divmod(tempo_rimanente, 3600) #divmod = prima divisione // e poi resto %
        minuti, secondi = divmod(resto, 60)
        etichetta_tempo.config(text=f"{ore:02}:{minuti:02}:{secondi:02}")
        tempo_rimanente = tempo_rimanente - 1
        root.after(1000, conto_alla_rovescia) # after(ritardo in ms quindi dopo 1 secondo, funzione da eseguire)
    else:
        etichetta_tempo.config(text="Tempo finito!")

root = tk.Tk()
root.title("Timer")
root.geometry("300x300")

etichetta_tempo = tk.Label(root, text="00:20:00", font=("Cambria", 26))
etichetta_tempo.pack(pady=40)

# Avvio appena si apre la finestra
root.after(100, conto_alla_rovescia) # parte dopo 0.1 secondo
root.mainloop()
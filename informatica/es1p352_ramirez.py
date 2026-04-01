import tkinter as tk 
finestra = tk.Tk()
finestra.title('es1pag352')
finestra.geometry('100x100')

pulsante_ok = tk.Button(finestra,text='Ok',width=30)
pulsante_ok.pack(pady=5)

pulsante_annulla = tk.Button(finestra,text='Annulla',width=30)
pulsante_annulla.pack(pady=5)

finestra.mainloop()
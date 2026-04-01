import tkinter as tk

finestra = tk.Tk()
finestra.title('la mia prima pagina')
finestra.geometry('400x300')

etichetta_istruzioni=tk.Label(finestra,text='inserisci nome: ')
etichetta_istruzioni.pack(pady=5)

pulsante_saluto = tk.Button()

etichetta = tk.Label(finestra,text='Ciao Mondo!',font='Arial',background='red')
etichetta.pack(pady=50)
finestra.mainloop()
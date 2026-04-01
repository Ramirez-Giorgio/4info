import tkinter as tk 
finestra = tk.Tk()
finestra.title('es1pag352')
finestra.geometry('200x200')

nome1 = tk.Label(finestra,text='marco',font='Arial')
nome1.pack(pady=10)

nome2 = tk.Label(finestra,text='mario',font='Arial')
nome2.pack(pady=10)

finestra.mainloop()
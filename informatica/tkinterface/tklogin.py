import tkinter as tk
from tkinter import messagebox

def verifica_login():
    nome_utente = campo_username.get()
    password = campo_password.get()

    if nome_utente == "admin" and password == "1234":
        messagebox.showinfo("Accesso consentito", "Login riuscito!")
    else:
        messagebox.showerror("Accesso negato", "Credenziali errate")

finestra = tk.Tk()
finestra.title("Login")

finestra.geometry("300x150")

tk.Label(finestra, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
campo_username = tk.Entry(finestra)
campo_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(finestra, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
campo_password = tk.Entry(finestra, show="*")
campo_password.grid(row=1, column=1, padx=10, pady=10)

pulsante_login = tk.Button(finestra, text="Accedi", command=verifica_login)
pulsante_login.grid(row=2, column=0, columnspan=2, pady=10)

finestra.mainloop()
import tkinter as tk

compteur = 0

def update():
    global compteur
    compteur += 1
    label.config(text=f"Temps : {compteur} s")
    fenetre.after(1000, update)

fenetre = tk.Tk()

label = tk.Label(fenetre, text="Temps : 0 s", font=("Arial", 20))
label.pack()

update()

fenetre.mainloop()

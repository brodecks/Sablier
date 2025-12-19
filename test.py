import tkinter as tk

def creation():
    global line, sableHaut, sableBas, initialHauteur
    initialHauteur = 100
    line = canvas.create_line(150, 50, 150, 350, fill="gold")
    sableHaut = canvas.create_polygon(100, 50, 200, 50, 150, 50 + initialHauteur, fill="gold")
    sableBas = canvas.create_polygon(100, 350, 200, 350, 150, 350, fill="gold")
    animer(initialHauteur)

def animer(hauteur):
    if hauteur > 0:
        canvas.coords(sableHaut, 100, 50, 200, 50, 150, 50 + hauteur)
        basApex = 350 - (initialHauteur - hauteur)
        canvas.coords(sableBas, 100, 350, 200, 350, 150, basApex)
        fenetre.after(60, lambda: animer(hauteur - 1))
    else:
        canvas.coords(sableHaut, 0, 0, 0, 0, 0, 0)
        canvas.coords(line, 0, 0, 0, 0)

fenetre = tk.Tk()
canvas = tk.Canvas(fenetre, width=300, height=400, bg="white")
canvas.pack()

button1 = tk.Button(fenetre, text="Jouer", command=creation)
button1.pack()

button = tk.Button(fenetre, text="Rejouer", command=creation)
button.pack()

fenetre.mainloop()

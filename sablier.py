import tkinter as tk

def animer():
    global hauteurSable
    if hauteurSable > 0:
        # On réduit le sable en haut
        canvas.coords(sableHaut, 150-50, 50, 150+50, 50, 150, 50 + hauteurSable)
        # On augmente le sable en bas (calculer la hauteur accumulée)
        basApex = 350 - (initialHauteur - hauteurSable)
        canvas.coords(sableBas, 150-50, 350, 150+50, 350, 150, basApex)
        hauteurSable -= 1
        fenetre.after(60, animer)
    else:
        canvas.coords(sableHaut, 0, 0, 0, 0, 0, 0)
        canvas.coords(line, 0, 0, 0, 0)


fenetre = tk.Tk()
canvas = tk.Canvas(fenetre, width=300, height=400, bg="white")
canvas.pack()

# Cadre de l'objet sablier
line = canvas.create_line(150, 50, 150, 350, fill="gold")

# Sable du haut (triangle inversé) — initialisé avec initialHauteur
initialHauteur = 100

sableHaut = canvas.create_polygon(100, 50, 200, 50, 150, 50 + initialHauteur, fill="gold")

# Sable du bas (triangle normal) — commence plat
sableBas = canvas.create_polygon(100, 350, 200, 350, 150, 350, fill="gold")

hauteurSable = initialHauteur

animer()
fenetre.mainloop()

import tkinter as tk
from plyer import notification

minutes = 0
secondes = 0


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
        fenetre.after(transformerTexteEnMS(), lambda: animer(hauteur - 1))
    else:
        canvas.coords(sableHaut, 0, 0, 0, 0, 0, 0)
        canvas.coords(line, 0, 0, 0, 0)
        notification.notify(
            title="Pause!",
            message="Drink water and stretch",
            app_name="Python Notifier",
        )
        lblTimer.pack()
        txtTimer.pack()
        button2.pack()

def transformerTexteEnMS():
    temps = int(txtTimer.get())
    temps2 = temps * 60000
    return int(temps2/100)


def LancerTimer():
    global secondes, minutes
    minutes = int(txtTimer.get())
    secondes = 0

    AffichageSS()


def AffichageSS():
    global secondes, minutes
    if secondes == 0 and minutes == 0:
        lblTimer.configure(text=f"Fin du timer.")
        return
    lblTimer.configure(text=f"{minutes} : {secondes:02d}")
    
    if secondes == 0:
        minutes -= 1
        secondes = 59
    else:
        secondes -= 1
    fenetre.after(1000, AffichageSS)


def reset():
    canvas.coords(sableBas, 100, 350, 200, 350, 150, 350)
    txtTimer.pack_forget()
    LancerTimer()
    creation()


fenetre = tk.Tk()
canvas = tk.Canvas(fenetre, width=300, height=400, bg="white")
canvas.pack()

lblTimer = tk.Label(fenetre, text="Temps(en minutes)")
lblTimer.pack()

txtTimer = tk.Entry(fenetre)
txtTimer.pack()

button1 = tk.Button(fenetre, text="Lancer", command=lambda: (creation(), LancerTimer(), button1.pack_forget(), txtTimer.pack_forget()))
button1.pack()

button2 = tk.Button(fenetre, text="Rejouer", command=lambda: (reset(), button2.pack_forget()))

fenetre.mainloop()

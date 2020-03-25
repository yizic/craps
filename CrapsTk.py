# coding: utf-8
 
from tkinter import * 
from random import *

fenetre = Tk()

# frame 1
FrameLancement = Frame(fenetre, borderwidth=3, relief=GROOVE)
FrameLancement.pack(side=LEFT, padx=30, pady=30)

Label(FrameLancement, text="Bonjour et bienvenu ! Prenez place.").pack(padx=10, pady=10)

Button(fenetre, text ='Prendre Place').pack(side=TOP, padx=5, pady=3)
Button(fenetre, text ='Accès aux documents').pack(side=BOTTOM, padx=5, pady=3)

fenetre.mainloop()
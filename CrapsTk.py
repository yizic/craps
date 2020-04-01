from tkinter import *
from random import *
import subprocess
from File import *


#1er ecran

def debut():

    imphrase = canimgphrase.create_image(340, 55, image=imagePhrase)
    canimgphrase.grid(row=0, columnspan = 4)
    imregle= canregle.create_image(200, 120, image= regle)
    canregle.grid(row=3, column =0, columnspan = 2)
    image_des= cancraps.create_image(165, 118, image= png_des)
    cancraps.grid(row=3, column =2, columnspan = 2)

    question.grid(row=1, column=1, columnspan=2)
    bouton_jouer.grid(row=2, column=1)
    bouton_docs.grid(row=2, column=2)

def voir_doc():

    print("Document")

def jouer():
    #Lancer le jeu du craps
    print("jouer")

    fenetre.destroy
    
    subprocess.call(["start python jeu.py"])

#crétion fenetre

fenetre = Tk()

#taille fenetre + couleur

fenetre.geometry("820x450")
fenetre.configure(background="white")

#positionner la fenetre au mileu et non pas dans un coin de lécran(Vive les tuto)

windowWidth = fenetre.winfo_reqwidth()
windowHeight = fenetre.winfo_reqheight()
positionRight = int(fenetre.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(fenetre.winfo_screenheight()/3 - windowHeight/2)
fenetre.geometry("+{}+{}".format(positionRight, positionDown))

#truc a utiliser et detruire (ou remove)

imagePhrase = PhotoImage(file="image/jeuDuCraps.png")
regle = PhotoImage(file="image/regle.png")
png_des = PhotoImage(file="image/des.png")

question = Label(fenetre, text = "Souhaitez vous jouer ou voir les documents", background = "white")
bouton_jouer = Button(fenetre, text = "jouer", command = jouer)
bouton_docs = Button(fenetre, text = "voir les documents", command = voir_doc)

canimgphrase = Canvas(fenetre, width=660, height=100, background ="white", highlightthickness =  0)
canregle = Canvas(fenetre, width=420, height= 237, background ="white", highlightthickness =  0)
cancraps = Canvas(fenetre, width=330, height= 237, background ="white", highlightthickness =  0)

bouton_quit = Button(fenetre, text="quitter", command= fenetre.destroy)

debut()

#titre fenetre

fenetre.title("Craps")

#fini

fenetre.mainloop()

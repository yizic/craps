from tkinter import *
from random import *
import subprocess
from File import *
from jeu import craps


#1er ecran

class CrapsTk:

    def __init__(self):

        self.fenetre = Tk()

        self.imphrase = None
        self.canimgphrase = None
        self.imregle = None
        self.canregle = None
        self.image_des = None
        self.cancraps = None
        self.question = None
        self.bouton_jouer = None
        self.bouton_docs = None
        self.imagePhrase = None
        self.regle = None
        self.png_des = None

    def debut(self):

        self.imphrase = self.canimgphrase.create_image(340, 55, image = self.imagePhrase)
        self.canimgphrase.grid(row=0, column=0, columnspan=4)
        self.imregle = self.canregle.create_image(200, 120, image = self.regle)
        self.canregle.grid(row=3, column =0, columnspan = 2)
        self.image_des = self.cancraps.create_image(165, 118, image = self.png_des)
        self.cancraps.grid(row=3, column =2, columnspan = 2)

        self.question.grid(row=1, column=1, columnspan=2)
        self.bouton_jouer.grid(row=2, column=1)
        self.bouton_docs.grid(row=2, column=2)

    def voir_jeu(self):
        
        self.fenetre.destroy()
        craps.voir_jeu()

    #crétion fenetre
    def creation_premiere_fenetre(self):

        #taille fenetre + couleur

        self.fenetre.geometry("820x450")
        self.fenetre.configure(background="white")

        #positionner la fenetre au mileu et non pas dans un coin de lécran(Vive les tuto)

        windowWidth = self.fenetre.winfo_reqwidth()
        windowHeight = self.fenetre.winfo_reqheight()
        positionRight = int(self.fenetre.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(self.fenetre.winfo_screenheight()/3 - windowHeight/2)
        self.fenetre.geometry("+{}+{}".format(positionRight, positionDown))

        #truc a utiliser et detruire (ou remove)

        self.imagePhrase = PhotoImage(file="image/jeuDuCraps.png")
        self.regle = PhotoImage(file="image/regle.png")
        self.png_des = PhotoImage(file="image/des.png")

        self.question = Label(self.fenetre, text = "Souhaitez vous jouer ou voir les documents", background = "white")
        self.bouton_jouer = Button(self.fenetre, width=40 , text = "jouer", command = lambda : self.voir_jeu())
        self.bouton_docs = Button(self.fenetre, width=40 , text = "voir les documents", command = File.voir_doc)

        self.canimgphrase = Canvas(self.fenetre, width=660, height=100, background ="white", highlightthickness =  0)
        self.canregle = Canvas(self.fenetre, width=420, height= 237, background ="white", highlightthickness =  0)
        self.cancraps = Canvas(self.fenetre, width=330, height= 237, background ="white", highlightthickness =  0)

        self.bouton_quit = Button(self.fenetre, text="quitter", command= self.fenetre.destroy)

        self.debut()

        """self.debut()"""

        #titre fenetre

        self.fenetre.title("Craps")

        #fini

        self.fenetre.mainloop()

if __name__ == "__main__":
    
    Crapy = CrapsTk()

    Crapy.creation_premiere_fenetre()

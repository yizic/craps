from tkinter import *
from random import *
import subprocess
from File import *
from Jeu import craps


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
        self.canimgphrase.grid(row=0, columnspan = 4)
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

        Crapy.imagePhrase = PhotoImage(file="image/jeuDuCraps.png")
        Crapy.regle = PhotoImage(file="image/regle.png")
        Crapy.png_des = PhotoImage(file="image/des.png")

        Crapy.question = Label(self.fenetre, text = "Souhaitez vous jouer ou voir les documents", background = "white")
        Crapy.bouton_jouer = Button(self.fenetre, text = "jouer", command = lambda : Crapy.voir_jeu())
        Crapy.bouton_docs = Button(self.fenetre, text = "voir les documents", command = File.voir_doc)

        Crapy.canimgphrase = Canvas(self.fenetre, width=660, height=100, background ="white", highlightthickness =  0)
        Crapy.canregle = Canvas(self.fenetre, width=420, height= 237, background ="white", highlightthickness =  0)
        Crapy.cancraps = Canvas(self.fenetre, width=330, height= 237, background ="white", highlightthickness =  0)

        Crapy.bouton_quit = Button(self.fenetre, text="quitter", command= self.fenetre.destroy)

        Crapy.debut()

        """self.debut()"""

        #titre fenetre

        self.fenetre.title("Craps")

        #fini

        self.fenetre.mainloop()

if __name__ == "__main__":
    
    Crapy = CrapsTk()

    Crapy.creation_premiere_fenetre()

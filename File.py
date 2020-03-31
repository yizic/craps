from tkinter import *
from random import *

class File:

    def __init__(self):
        self.questionDoc = None
        self.bouton_CV_Grillot = None
        self.bouton_CV_Cizet = None
        self.bouton_part1_Grillot = None
        self.bouton_part1_Cizet = None
        self.bouton_part2_Cizet = None
        self.bouton_part2_Grillot = None
        self.bouton_part3_Cizet = None
        self.bouton_part3_Grillot = None
        self.bouton_part4_Cizet = None
        self.bouton_part4_Grillot = None
        self.bouton_part5_Cizet = None
        self.bouton_part5_Grillot = None
        self.bouton_part6_Cizet = None
        self.bouton_part6_Grillot = None
        self.imagePhrase = None
        self.canimgphrase = None
        self.imphrase = None
        self.photo =None
        self.canphoto =None
        self.imphoto =None

    def debutDoc(self):
        self.imphrase = self.canimgphrase.create_image(340, 55, image=self.imagePhrase)
        self.canimgphrase.grid(row=0, columnspan = 4)
        self.questionDoc.grid(row=1, column=1, columnspan=2)
        self.bouton_CV_Grillot.grid(row=2, column=1)
        self.bouton_CV_Cizet.grid(row=2, column=2)
        self.bouton_part1_Grillot.grid(row=3, column=1)
        self.bouton_part1_Cizet.grid(row=3, column=2)
        self.bouton_part2_Grillot.grid(row=4, column=1)
        self.bouton_part2_Cizet.grid(row=4, column=2)
        self.bouton_part3_Grillot.grid(row=5, column=1)
        self.bouton_part3_Cizet.grid(row=5, column=2)
        self.bouton_part4_Grillot.grid(row=6, column=1)
        self.bouton_part4_Cizet.grid(row=6, column=2)
        self.bouton_part5_Grillot.grid(row=7, column=1)
        self.bouton_part5_Cizet.grid(row=7, column=2)
        self.bouton_part6_Grillot.grid(row=8, column=1)
        self.bouton_part6_Cizet.grid(row=8, column=2)

    def afficher_doc(self, value):
        popup = Tk()

        self.photo = PhotoImage(master=popup, file=value)
        self.canphoto = Canvas(popup, width=529, height= 750, background ="white", highlightthickness =  0)
        self.imphoto = self.canphoto.create_image(529/2, 750/2, image= self.photo)
        self.canphoto.grid(row=0,column=0)
        popup.mainloop()

    def voir_doc():
        fic = File()
        #crétion fenetreDoc
        fenetreDoc = Toplevel()

        #taille fenetreDoc + couleur

        fenetreDoc.geometry("663x450")
        fenetreDoc.configure(background="white")

        #positionner la fenetreDoc au mileu et non pas dans un coin de lécran(Vive les tuto)

        windowWidth = fenetreDoc.winfo_reqwidth()
        windowHeight = fenetreDoc.winfo_reqheight()
        positionRight = int(fenetreDoc.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(fenetreDoc.winfo_screenheight()/3 - windowHeight/2)
        fenetreDoc.geometry("+{}+{}".format(positionRight, positionDown))

        #truc a utiliser et detruire (ou remove)
        
        fic.imagePhrase = PhotoImage(file="image/leJeuDuMorpion.png")
        
        fic.canimgphrase = Canvas(fenetreDoc, width=660, height=100, background ="white", highlightthickness =  0)

        fic.questionDoc = Label(fenetreDoc, text = "Quel fichier voulez-vous afficher?", background = "white")
        fic.bouton_CV_Grillot = Button(fenetreDoc, text = "CV Grillot Brian", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_CV_Cizet = Button(fenetreDoc, text = "CV Cizet Vincent", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part1_Grillot = Button(fenetreDoc, text = "P1 Grillot Brian", command = lambda:fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part1_Cizet = Button(fenetreDoc, text = "P1 Cizet Vincent", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part2_Grillot = Button(fenetreDoc, text = "P2 Grillot Brian", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part2_Cizet = Button(fenetreDoc, text = "P2 Cizet Vincent", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part3_Grillot = Button(fenetreDoc, text = "P3 Grillot Brian", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part3_Cizet = Button(fenetreDoc, text = "P3 Cizet Vincent", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part4_Grillot = Button(fenetreDoc, text = "P4 Grillot Brian", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part4_Cizet = Button(fenetreDoc, text = "P4 Cizet Vincent", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part5_Grillot = Button(fenetreDoc, text = "P5 Grillot Brian", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part5_Cizet = Button(fenetreDoc, text = "P5 Cizet Vincent", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part6_Grillot = Button(fenetreDoc, text = "P6 Grillot Brian", command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.bouton_part6_Cizet = Button(fenetreDoc, text = "P6 Cizet Vincent", command = lambda: Ffic.afficher_doc("image/CV_Grillot_Brian.png"))
        fic.debutDoc()

        #titre fenetreDoc

        fenetreDoc.title("MORPION2")

        #fini

        fenetreDoc.mainloop()

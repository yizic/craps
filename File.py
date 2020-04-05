from tkinter import *
from random import *

class File:

    def __init__(self):
        self.questionDoc = None
        self.bouton_CV_Grillot = None
        self.bouton_CV_Cizey = None
        self.bouton_part1_Grillot = None
        self.bouton_part1_Cizey = None
        self.bouton_part2_Cizey = None
        self.bouton_part2_Grillot = None
        self.bouton_part3_Cizey = None
        self.bouton_part3_Grillot = None
        self.bouton_part4_Cizey = None
        self.bouton_part4_Grillot = None
        self.bouton_part5_Cizey = None
        self.bouton_part5_Grillot = None
        self.bouton_part6_Cizey = None
        self.bouton_part6_Grillot = None
        self.bouton_part7_Cizey = None
        self.bouton_part7_Grillot = None
        self.bouton_part8_Cizey = None
        self.bouton_part8_Grillot = None
        self.bouton_part9_Cizey = None
        self.bouton_part9_Grillot = None
        self.imagePhrase = None
        self.canimgphrase = None
        self.imphrase = None
        self.photo =None
        self.canphoto =None
        self.imphoto =None
        self.raport=None
        self.raport2=None

    def debutDoc(self):
        self.imphrase = self.canimgphrase.create_image(340, 55, image=self.imagePhrase)
        self.canimgphrase.grid(row=0, columnspan = 4)
        self.questionDoc.grid(row=1, column=1, columnspan=2)
        self.bouton_CV_Grillot.grid(row=2, column=1)
        self.bouton_CV_Cizey.grid(row=2, column=2)
        self.bouton_part1_Grillot.grid(row=3, column=1)
        self.bouton_part1_Cizey.grid(row=3, column=2)
        self.bouton_part2_Grillot.grid(row=4, column=1)
        self.bouton_part2_Cizey.grid(row=4, column=2)
        self.bouton_part3_Grillot.grid(row=5, column=1)
        self.bouton_part3_Cizey.grid(row=5, column=2)
        self.bouton_part4_Grillot.grid(row=6, column=1)
        self.bouton_part4_Cizey.grid(row=6, column=2)
        self.bouton_part5_Grillot.grid(row=7, column=1)
        self.bouton_part5_Cizey.grid(row=7, column=2)
        self.bouton_part6_Grillot.grid(row=8, column=1)
        self.bouton_part6_Cizey.grid(row=8, column=2)
        self.bouton_part7_Grillot.grid(row=9, column=1)
        self.bouton_part7_Cizey.grid(row=9, column=2)
        self.bouton_part8_Grillot.grid(row=10, column=1)
        self.bouton_part8_Cizey.grid(row=10, column=2)
        self.bouton_part9_Grillot.grid(row=11, column=1)
        self.bouton_part9_Cizey.grid(row=11, column=2)

    def afficher_doc(self, value, partie, partiesuiv):
        popup = Tk()

        if "png" in value:

            self.photo = PhotoImage(master=popup, file=value)
            self.canphoto = Canvas(popup, width=529, height= 750, background ="white", highlightthickness =  0)
            self.imphoto = self.canphoto.create_image(529/2, 750/2, image= self.photo)
            self.canphoto.grid(row=0,column=0)
            popup.title("CV")

        else: 
            
            text = ""
            text1 = ""
            fichier = open(value, "r")

            ecrire = False
            line1 = False

            for ligne in fichier:
                if partie in ligne:
                    ecrire = True
                    line1 = True
                elif partiesuiv in ligne:
                    ecrire = False
                if ecrire:
                    if line1:
                        text1 += ligne
                        line1=False
                    else:
                        text += ligne
                        line1 = False
                
            
            fichier.close()
            
            self.raport = Label(popup, text = text1, justify ='center', wraplength = 1000, font=("Arial", 18))
            self.raport.grid(row=0,column=0)
            self.raport2 = Label(popup, text = text, justify ='left', wraplength = 1000, font=("Arial", 12))
            self.raport2.grid(row=1,column=0)
            popup.title(text1)

        
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
        
        fic.imagePhrase = PhotoImage(file="image/jeuDuCraps.png")
        
        fic.canimgphrase = Canvas(fenetreDoc, width=660, height=100, background ="white", highlightthickness =  0)

        fic.questionDoc = Label(fenetreDoc, text = "Quel fichier voulez-vous afficher?", background = "white")
        fic.bouton_CV_Grillot = Button(fenetreDoc, text = "CV Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/CV_Grillot_Brian.png", "", ""))
        fic.bouton_CV_Cizey = Button(fenetreDoc, text = "CV Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/CV_Cizey_Vincent.png", "", ""))
        fic.bouton_part1_Grillot = Button(fenetreDoc, text = "Attentes pro Grillot Brian", width=40 , command = lambda:fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Attentes pro", "Compétences pro"))
        fic.bouton_part1_Cizey = Button(fenetreDoc, text = "Attentes pro Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Attentes pro", "Compétences pro"))
        fic.bouton_part2_Grillot = Button(fenetreDoc, text = "Compétences pro Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Compétences pro", "Traits de personnalité"))
        fic.bouton_part2_Cizey = Button(fenetreDoc, text = "Compétences pro Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Compétences pro", "Traits de personnalité"))
        fic.bouton_part3_Grillot = Button(fenetreDoc, text = "Traits de personnalité Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Traits de personnalité", "Centres d’intérêts"))
        fic.bouton_part3_Cizey = Button(fenetreDoc, text = "Traits de personnalité Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Traits de personnalité", "Centres d’intérêts"))
        fic.bouton_part4_Grillot = Button(fenetreDoc, text = "Centres d’intérêts Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Centres d’intérêts", "Itinéraire pro"))
        fic.bouton_part4_Cizey = Button(fenetreDoc, text = "Centres d’intérêts Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Centres d’intérêts", "Itinéraire pro"))
        fic.bouton_part5_Grillot = Button(fenetreDoc, text = "Itinéraire pro Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Itinéraire pro", "Raison des étapes"))
        fic.bouton_part5_Cizey = Button(fenetreDoc, text = "Itinéraire pro Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Itinéraire pro", "Raison des étapes"))
        fic.bouton_part6_Grillot = Button(fenetreDoc, text = "Raison des étapes Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Raison des étapes", "Influences des choix"))
        fic.bouton_part6_Cizey = Button(fenetreDoc, text = "Raison des étapes Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Raison des étapes", "Influences des choix"))
        fic.bouton_part7_Grillot = Button(fenetreDoc, text = "Influences des choix Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Influences des choix", "Contraintes perso"))
        fic.bouton_part7_Cizey = Button(fenetreDoc, text = "Influences des choix Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Influences des choix", "Contraintes perso"))
        fic.bouton_part8_Grillot = Button(fenetreDoc, text = "Contraintes perso Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Contraintes perso", "Accidents de parcours"))
        fic.bouton_part8_Cizey = Button(fenetreDoc, text = "Contraintes perso Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Contraintes perso", "Accidents de parcours"))
        fic.bouton_part9_Grillot = Button(fenetreDoc, text = "Accidents de parcours Grillot Brian", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Grillot_Brian.docx", "Accidents de parcours", "azertdyfguihcnhbever"))
        fic.bouton_part9_Cizey = Button(fenetreDoc, text = "Accidents de parcours Cizey Vincent", width=40 ,command = lambda: fic.afficher_doc("image/Rapport_Cizey_Vincent.docx", "Accidents de parcours", "gvfsgnsehenifnnxbgdsfongf"))
        fic.debutDoc()

        #titre fenetreDoc

        fenetreDoc.title("Craps")

        #fini

        fenetreDoc.mainloop()
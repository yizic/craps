from tkinter import *
from random import *

class File:

    __slot__ = (
        "questionDoc"
    )

    def __init__(self, questionDoc=None):
        self.questionDoc = questionDoc

    def debutDoc(self):
        self.questionDoc.grid(row=1, column=1, columnspan=2)

    def voir_doc():
        fic = File()
        #crétion fenetreDoc
        fenetreDoc = Tk()

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


        fic.questionDoc = Label(fenetreDoc, text = "Souhaitez vous jouer contre une IA ou contre un ami", background = "white")

        fic.debutDoc()

        #titre fenetreDoc

        fenetreDoc.title("MORPION2")

        #fini

        fenetreDoc.mainloop()

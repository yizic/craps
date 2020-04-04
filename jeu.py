# -*- coding: utf-8 -*-
"""
Craps
-----
Le Craps est un jeu de dés, que nous avons légèrement modifié dans le cadre de ce projet.
L'ordinateur lance les dés, si au premier lancé vous obtenez 7 ou 11, vous doublez votre mise. Si vous obtenez 2, 3 ou 12, vous perdez.
Pour toute autre valeur, vous relancez les dés, jusqu'à obtenir la même valeur de nouveau, ce qui doublera votre mise.
Mais si dans l'intervalle vous obtenez un 7, vous perdez la mise.
En fonction de votre portefeuille, vous obtenez des informations sur les développeurs de ce jeu.
Nous avons choisi un jeu avec mise car il est facilement améliorable (multijoueur, système d'achat avec les gains...),
et pour le côté mise - gains que nous trouvons attractif !"""

from random import randint
from tkinter import *
from tkinter.messagebox import *


class craps:
    def __init__(self, p):

        self.regles = """Le Craps est un jeu de dés, que nous avons légèrement modifié dans le cadre de ce projet.
        L'ordinateur lance les dés, si au premier lancé vous obtenez 7 ou 11, vous doublez votre mise. Si vous obtenez 2, 3 ou 12, vous perdez.
        Pour toute autre valeur, vous relancez les dés, jusqu'à obtenir la même valeur de nouveau, ce qui doublera votre mise.
        Mais si dans l'intervalle vous obtenez un 7, vous perdez la mise.
        En fonction de votre portefeuille, vous obtenez des informations sur les développeurs de ce jeu.
        Nous avons choisi un jeu avec mise car il est facilement améliorable (multijoueur, système d'achat avec les gains...),
        et pour le côté mise - gains que nous trouvons attractif !
        """

        self.portefeuille = p
        self.mise = 0
        self.tour = 1
        self.cible = 0
        self.joue = True

        self.imagePhrase = None
        self.imphrase = None
        self.canimgphrase = None
        self.bouton_popup_infos = None
        self.labelportefeuille = None
        self.labelentrypari = None
        self.entrypari = None
        self.buttonsoumettre = None
        self.labelportefeuille_new = None

    def debut_jeu(self):

        self.imphrase = self.canimgphrase.create_image(340, 55, image=self.imagePhrase)
        self.canimgphrase.grid(row = 0, columnspan = 2)
        self.bouton_popup_infos.place(x = 0, y = 0)
        self.labelportefeuille.grid(row = 1, columnspan = 2)
        self.labelentrypari.grid(row = 2, columnspan = 1)
        self.entrypari.grid(row = 2, columnspan = 2)
        self.buttonsoumettre.grid(row = 3, columnspan = 2)

    def get_regles(self):
        return """Le Craps est un jeu de dés, que nous avons légèrement modifié dans le cadre de ce projet.
        L'ordinateur lance les dés, si au premier lancé vous obtenez 7 ou 11, vous doublez votre mise. Si vous obtenez 2, 3 ou 12, vous perdez.
        Pour toute autre valeur, vous relancez les dés, jusqu'à obtenir la même valeur de nouveau, ce qui doublera votre mise.
        Mais si dans l'intervalle vous obtenez un 7, vous perdez la mise.
        En fonction de votre portefeuille, vous obtenez des informations sur les développeurs de ce jeu.
        Nous avons choisi un jeu avec mise car il est facilement améliorable (multijoueur, système d'achat avec les gains...),
        et pour le côté mise - gains que nous trouvons attractif !
        """

    def getJoue(self):
        return self.joue
    
    def jeuGagne(self):
        print("Vous avez gagné {} ".format(2*self.mise))
        self.portefeuille += 2*self.mise
        self.fin()      

    def jeuPerdu(self):
        print("Vous avez perdu !")      
        self.fin()

    def debut(self):
        self.tour = 1
        self.cible = 0
        self.joue = True

    def fin(self):
        self.joue = False

    def getCible(self):
        return self.cible
    
    def setCible(self, c):
        self.cible = c

    def enCours(self):
        if self.portefeuille > 0:
            return True
        else:
            return False

    def miser(self, mise):
        
        #TODO vérifier qu'on parie pas plus que portefeuille.
        try:
            mise = int(mise)
        except ValueError:
            print("\t\tMerci d'entrer une valeur numérique correcte")
            mise = 0
            return False

        self.mise = mise
        self.portefeuille -= mise

        return True

    def lancer(self):
        return randint(1,6)

    def analyse(self, v1, v2):
        valeur = v1 + v2
        print("\n---> Vous avez tiré : {} et {}, ce qui fait {}".format(v1, v2, valeur))
        if self.tour == 1:
            if valeur==7 or valeur==11:
                self.jeuGagne()
            elif valeur==2 or valeur==3 or valeur==12:
                self.jeuPerdu()
            else:
                self.tour += 1
                self.setCible(valeur)
        else:
            if valeur==7:
                self.jeuPerdu()
            elif valeur == self.getCible():
                self.jeuGagne()

    def lancer_jeu(self, miseEntree, fenetreGame):

        if self.enCours():
            self.debut()
            miseOk = self.miser(miseEntree)

            if miseOk == True:
                while self.getJoue():
                    self.analyse(self.lancer(), self.lancer())
                self.labelportefeuille.destroy()
                self.labelportefeuille_new = Label(fenetreGame, text = self.portefeuille)
                self.labelportefeuille_new.grid(row = 1, columnspan = 2)

                if self.portefeuille <= 0:

                    self.labelportefeuille_new = Label(fenetreGame, text = "plus d'argent !!")
                    self.labelportefeuille_new.grid(row = 1, columnspan = 2)

                    popPerdu = Tk()
                    popPerdu.title("perdu !")

                    ErreurLab = Label(popPerdu, text = "vous avez perdu !", background = "white")
                    ErreurLab.pack(side = "top", fill = "x", pady = 10)
                    BoutonPopPerduMenu = Button(popPerdu, text = "Retour au menu", command = lambda : popPerdu.destroy)
                    BoutonPopPerduMenu.pack()
                    BoutonPopPerduRejouer = Button(popPerdu, text = "Recommencer le jeu", command = lambda : self.recommencer_jeu(fenetreGame, popPerdu))
                    BoutonPopPerduRejouer.pack()
                    popPerdu.mainloop()

            else:
                #TODO pop-up erreur.
                print("erreur")

                popErreur = Toplevel()
                popErreur.title("mauvaise saisie !")

                ErreurLab = Label(popErreur, text = "erreur de saisie !", background = "white")
                ErreurLab.pack(side = "top", fill = "x", pady = 10)
                BoutonPopErreur = Button(popErreur, text = "Ok", command = popErreur.destroy)
                BoutonPopErreur.pack()
                popErreur.mainloop()


 
    def recommencer_jeu(self, fenetreGame, popPerdu):
        
        fenetreGame.destroy()
        popPerdu.destroy()
        craps.voir_jeu()
        
    def retour_menu(self, fenetreGame, popPerdu):
        from CrapsTk import main
        popPerdu.destroy()
        main()   
        fenetreGame.destroy()

    def popInfoRegles():

        #Partie moche pour éviter d'avoir une référence... dsl.
        temp = craps(0)
        to_show = temp.get_regles()

        popRegles = Toplevel()
        popRegles.title("Règles")

        IntroLab = Label(popRegles, text = to_show, background = "white")
        IntroLab.pack(side = "top", fill = "x", pady = 10)
        BoutonPopRegles = Button(popRegles, text = "Ok", command = popRegles.destroy)
        BoutonPopRegles.pack()
        popRegles.mainloop()


    def voir_jeu():

        print("===============")
        print("=  C R A P S  =")
        print("===============")

        game = craps(500)

        fenetreGame = Tk()

        fenetreGame.geometry("820x450")
        fenetreGame.configure(background="white")

        #positionner la fenetreGame au mileu et non pas dans un coin de lécran(Vive les tuto)

        windowWidth = fenetreGame.winfo_reqwidth()
        windowHeight = fenetreGame.winfo_reqheight()
        positionRight = int(fenetreGame.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(fenetreGame.winfo_screenheight()/3 - windowHeight/2)
        fenetreGame.geometry("+{}+{}".format(positionRight, positionDown))

        game.imagePhrase = PhotoImage(file="image/jeuDuCraps.PNG")
        game.canimgphrase = Canvas(fenetreGame, width=660, height=100, background ="white", highlightthickness =  0)
        game.bouton_popup_infos = Button(fenetreGame, width=5, height=2, text = "?", command = lambda : craps.popInfoRegles())
        game.labelportefeuille = Label(fenetreGame, text = game.portefeuille)
        game.labelentrypari = Label(fenetreGame, text = "Voici votre portefeuille :")
        game.entrypari = Entry(fenetreGame, text = "Entrez la valeur à miser ici !")

        game.buttonsoumettre = Button(fenetreGame, text = "Parier !", command = lambda : lancer_recup_mise())

        def lancer_recup_mise():

            int_mise_donnee = game.entrypari.get()
            print("int_mise_donnee")
            print(int_mise_donnee)
            game.lancer_jeu(int_mise_donnee, fenetreGame)


        #game.IntroLab.pack()

        game.debut_jeu()

        #titre fenetreGame

        fenetreGame.title("jeu")

        #fin interface

        fenetreGame.mainloop()


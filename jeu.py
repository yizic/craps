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
        self.labelannonceportefeuille = None
        self.labelannonceentry = None
        self.entrypari = None
        self.buttonsoumettre = None
        self.labelannoncedes1 = None
        self.labelannoncedes2 = None
        self.labeldes1 = None
        self.labeldes2 = None
        self.labeldes1_new = None
        self.labeldes2_new = None
        self.labelcible = None
        self.labelannoncecible = None
        self.labelmessage = None
        self.labelinstruction = None
        self.buttonretourmenu = None

    def debut_jeu(self):

        self.imphrase = self.canimgphrase.create_image(340, 55, image=self.imagePhrase)
        self.canimgphrase.grid(row = 0, column = 1, columnspan = 4)
        self.bouton_popup_infos.place(x = 0, y = 0)
        self.labelportefeuille.grid(row = 1, column = 2)
        self.labelannonceportefeuille.grid(row = 1, column = 1)
        self.labelannonceentry.grid(row = 2, column = 1)
        self.entrypari.grid(row = 2, column = 2)
        self.buttonsoumettre.grid(row = 3, column = 2)
        self.labelannoncedes1.grid(row = 5, column = 1)
        self.labelannoncedes2.grid(row = 5, column = 3)
        self.labelcible.grid(row = 6, column = 2)
        self.labelannoncecible.grid(row = 6, column = 1)
        self.labelmessage.grid(row = 7, column = 2)
        self.labelinstruction.grid(row = 8, column = 2)

        self.labeldes1.grid(row = 5, column = 2)
        self.labeldes2.grid(row = 5, column = 4)

        self.buttonretourmenu.grid(row = 0, column = 0)

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
        self.cible = "pas encore de cible"
        self.joue = True

    def fin(self):
        self.joue = False

    def getCible(self):
        return self.cible
    
    def setCible(self, c):
        self.cible = c

    def enCours(self):
        if int(self.tour) == 1:
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
                self.labelmessage.config(text = "Vous avez gagné {} dès le premier lancer !".format(2*self.mise))
                self.labelinstruction.config(text = "Vous pouvez remiser maintenant !")
                self.buttonsoumettre.config(text = "Parier !")
            elif valeur==2 or valeur==3 or valeur==12:
                self.jeuPerdu()
                self.labelmessage.config(text = "Vous avez perdu votre mise de {}, oh non...".format(self.mise))
                self.labelinstruction.config(text = "Mais vous pouvez remiser maintenant ! Essayez donc !")
                self.buttonsoumettre.config(text = "Parier !")
            else:
                self.tour += 1
                self.setCible(valeur)
                self.buttonsoumettre.config(text = "Lancer les dés !")
                self.labelmessage.config(text = "La valeur cible a été mise à jour !")
                self.labelinstruction.config(text = "Voyons qui gagne ! relancer les dés !")

        else:
            if valeur==7:
                self.jeuPerdu()
                self.labelmessage.config(text = "Vous avez perdu votre mise de {}, on y croyait pourtant...".format(self.mise))
                self.labelinstruction.config(text = "ça donne envie de retenter non ?!")
                self.buttonsoumettre.config(text = "Parier !")

            elif valeur == self.getCible():
                self.jeuGagne()
                self.labelmessage.config(text = "La cible a été atteinte !! Félicitations ! {} en plus !".format(self.mise))
                self.labelinstruction.config(text = "Plus d'argent = plus de paris !!!! oui c'est sain, pourquoi ?")
                self.buttonsoumettre.config(text = "Parier !")
            
            else:
                self.labelmessage.config(text = "Un coup pour rien... Allez on peut mieux faire !")
                self.labelinstruction.config(text = "Faites chauffer les dés ! C'est pas les petits chevaux ici !")
                self.buttonsoumettre.config(text = "Lancer les dés !")

    def lancer_jeu(self, miseEntree, fenetreGame):

        print(self.joue)
        print(self.portefeuille)
        print(self.tour)
        if self.enCours():
            self.debut()
            miseOk = self.miser(miseEntree)
            print("portefeuille : " + str(self.portefeuille))

            if miseOk == False:
                print("erreur")

                popErreur = Toplevel()
                popErreur.title("mauvaise saisie !")

                ErreurLab = Label(popErreur, text = "erreur de saisie !", background = "white")
                ErreurLab.pack(side = "top", fill = "x", pady = 10)
                BoutonPopErreur = Button(popErreur, text = "Ok", command = popErreur.destroy)
                BoutonPopErreur.pack()
                popErreur.mainloop()
                return

        v1 = self.lancer()
        v2 = self.lancer()
        self.labeldes1.destroy()
        self.labeldes2.destroy()
        self.labeldes1_new = Label(fenetreGame, text = v1)
        self.labeldes1_new.grid(row = 5, column = 2)
        self.labeldes2_new = Label(fenetreGame, text = v2)
        self.labeldes2_new.grid(row = 5, column = 4)

        self.analyse(v1, v2)

        self.labelcible.config(text = self.getCible())
        self.labelportefeuille.config(text = self.portefeuille)

        if self.portefeuille <= 0:

            self.labelportefeuille.config(text = "plus d'argent !!")

            popPerdu = Tk()
            popPerdu.title("perdu !")

            ErreurLab = Label(popPerdu, text = "vous avez perdu !", background = "white")
            ErreurLab.pack(side = "top", fill = "x", pady = 10)
            BoutonPopPerduMenu = Button(popPerdu, text = "Retour au menu", command = lambda : self.retour_menu(fenetreGame, popPerdu))
            BoutonPopPerduMenu.pack()
            BoutonPopPerduRejouer = Button(popPerdu, text = "Recommencer le jeu", command = lambda : self.recommencer_jeu(fenetreGame, popPerdu))
            BoutonPopPerduRejouer.pack()
            popPerdu.mainloop()

 
    def recommencer_jeu(self, fenetreGame, popPerdu):
        
        fenetreGame.destroy()
        popPerdu.destroy()
        craps.voir_jeu()
        
    def retour_menu(self, fenetreGame, popPerdu):
        print("retour menu")
        fenetreGame.destroy()
        popPerdu.destroy()
        import CrapsTk
        Crapy = CrapsTk.CrapsTk()
        Crapy.creation_premiere_fenetre()


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


    def quitter(self, fenetreGame):
        popQuitter = Tk()
        popQuitter.title("Vous voulez quitter ?")

        QuitterLab = Label(popQuitter, text = "vous pouvez quitter ou  recommencer une partie.", background = "white")
        QuitterLab.pack(side = "top", fill = "x", pady = 10)
        BoutonpopQuitterMenu = Button(popQuitter, text = "Retour au menu", command = lambda : self.retour_menu(fenetreGame, popQuitter))
        BoutonpopQuitterMenu.pack()
        BoutonpopQuitterRejouer = Button(popQuitter, text = "Recommencer le jeu", command = lambda : self.recommencer_jeu(fenetreGame, popQuitter))
        BoutonpopQuitterRejouer.pack()
        popQuitter.mainloop()


    def voir_jeu():

        print("===============")
        print("=  C R A P S  =")
        print("===============")

        game = craps(500)

        fenetreGame = Tk()

        fenetreGame.geometry("820x450")
        fenetreGame.configure(background="white")

        """fenetreGame.grid_columnconfigure(1, weight = 1)
        fenetreGame.grid_columnconfigure(2, weight = 1)
        fenetreGame.grid_columnconfigure(3, weight = 1)
        fenetreGame.grid_columnconfigure(4, weight = 1)"""

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
        game.labelannonceportefeuille = Label(fenetreGame, text = "Voici votre portefeuille :")

        game.labelannoncedes1 = Label(fenetreGame, text = "dés 1 :")
        game.labelannoncedes2 = Label(fenetreGame, text = "dés 2 :")

        game.labeldes1 = Label(fenetreGame, text = "*****")
        game.labeldes2 = Label(fenetreGame, text = "*****")

        game.labelannonceentry = Label(fenetreGame, text = "entrez le montant à jouer :")
        game.entrypari = Entry(fenetreGame, text = "Entrez la valeur à miser ici !")

        game.labelcible = Label(fenetreGame, text = "pas encore de cible")
        game.labelannoncecible = Label(fenetreGame, text = "cible pour gagner :")

        game.labelmessage = Label(fenetreGame, text = "Vous devez entrer une valeur à miser pour commencer.")
        game.labelinstruction = Label(fenetreGame, text = "Une fois entrée, la valeur ne peut plus être changée jusqu'au résultat.")

        game.buttonretourmenu = Button(fenetreGame, text = "retour au menu", command = lambda : game.quitter(fenetreGame))

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


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
from File import *


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
        self.palier_max_atteind = 500
        self.palier_suivant = 525
        self.doc_non_montre = [("image/Rapport_Grillot_Brian.docx", "Attentes pro", "Compétences pro"),
        ("image/Rapport_Cizey_Vincent.docx", "Attentes pro", "Compétences pro"),
        ("image/Rapport_Grillot_Brian.docx", "Compétences pro", "Traits de personnalité"),
        ("image/Rapport_Cizey_Vincent.docx", "Compétences pro", "Traits de personnalité"),
        ("image/Rapport_Grillot_Brian.docx", "Traits de personnalité", "Centres d’intérêts"),
        ("image/Rapport_Cizey_Vincent.docx", "Traits de personnalité", "Centres d’intérêts"),
        ("image/Rapport_Grillot_Brian.docx", "Centres d’intérêts", "Itinéraire pro"),
        ("image/Rapport_Cizey_Vincent.docx", "Centres d’intérêts", "Itinéraire pro"),
        ("image/Rapport_Grillot_Brian.docx", "Itinéraire pro", "Raison des étapes"),
        ("image/Rapport_Cizey_Vincent.docx", "Itinéraire pro", "Raison des étapes"),
        ("image/Rapport_Grillot_Brian.docx", "Raison des étapes", "Influences des choix"),
        ("image/Rapport_Cizey_Vincent.docx", "Raison des étapes", "Influences des choix"),
        ("image/Rapport_Grillot_Brian.docx", "Influences des choix", "Contraintes perso"),
        ("image/Rapport_Cizey_Vincent.docx", "Influences des choix", "Contraintes perso"),
        ("image/Rapport_Grillot_Brian.docx", "Contraintes perso", "Accidents de parcours"),
        ("image/Rapport_Cizey_Vincent.docx", "Contraintes perso", "Accidents de parcours"),
        ("image/Rapport_Grillot_Brian.docx", "Accidents de parcours", "azertdyfguihcnhbever"),
        ("image/Rapport_Cizey_Vincent.docx", "Accidents de parcours", "gvfsgnsehenifnnxbgdsfongf"),
        ("image/CV_Grillot_Brian.png", "", ""), ("image/CV_Cizey_Vincent.png", "", "")]

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
        self.labelmaxatteind = None
        self.labelannoncemaxatteind = None
        self.annonceresultatdes = None
        self.resultatdes = None
        self.labelannoncepaliersuivant = None
        self.labelpaliersuivant = None

    def debut_jeu(self):

        self.imphrase = self.canimgphrase.create_image(340, 55, image=self.imagePhrase)
        self.canimgphrase.grid(row = 0, column = 1, columnspan = 4)
        self.bouton_popup_infos.place(x = 0, y = 0)
        self.labelportefeuille.grid(row = 1, column = 2, pady = 7)
        self.labelannonceportefeuille.grid(row = 1, column = 1, pady = 7)
        self.labelannonceentry.grid(row = 2, column = 1, pady = 7)
        self.entrypari.grid(row = 2, column = 2, pady = 7)
        self.buttonsoumettre.grid(row = 3, column = 2)
        self.labelannoncedes1.grid(row = 4, column = 1, pady = 7)
        self.labelannoncedes2.grid(row = 4, column = 3, pady = 7)
        self.annonceresultatdes.grid(row = 5, column = 1, pady = 7)
        self.resultatdes.grid(row = 5, column = 2, pady = 7)
        self.labelcible.grid(row = 6, column = 2, pady = 7)
        self.labelannoncecible.grid(row = 6, column = 1, pady = 7)
        self.labelmessage.grid(row = 7, column = 2, pady = 7)
        self.labelinstruction.grid(row = 8, column = 2, pady = 7)
        self.labelmaxatteind.grid(row = 9, column = 3, pady = 7)
        self.labelannoncemaxatteind.grid(row = 9, column = 2, pady = 7)
        self.labelpaliersuivant.grid(row = 10, column = 3, pady = 7)
        self.labelannoncepaliersuivant.grid(row = 10, column = 2, pady = 7)

        self.labeldes1.grid(row = 4, column = 2, pady = 7)
        self.labeldes2.grid(row = 4, column = 4, pady = 7)

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
    
    def jeuGagne(self, fenetreGame):

        self.portefeuille += 2*self.mise
        
        if self.portefeuille > self.palier_max_atteind:
            self.palier_max_atteind = self.portefeuille
        
        self.entrypari.config(state = NORMAL)
        self.labelannonceentry.config(text = "entrez le montant à jouer :")

        self.tour = 1

        self.fin()      

    def jeuPerdu(self, fenetreGame):
        
        if self.portefeuille <= 0 :

            self.labelportefeuille.config(text = "plus d'argent !!")

            popPerdu = Tk()
            popPerdu.title("perdu !")

            ErreurLab = Label(popPerdu, text = "vous avez perdu !", background = "white")
            ErreurLab.pack(side = "top", fill = "x")
            BoutonPopPerduMenu = Button(popPerdu, text = "Retour au menu", command = lambda : self.retour_menu(fenetreGame, popPerdu))
            BoutonPopPerduMenu.pack()
            BoutonPopPerduRejouer = Button(popPerdu, text = "Recommencer le jeu", command = lambda : self.recommencer_jeu(fenetreGame, popPerdu))
            BoutonPopPerduRejouer.pack()
            popPerdu.mainloop()

        self.entrypari.config(state = NORMAL)
        self.labelannonceentry.config(text = "entrez le montant à jouer :")

        self.tour = 1

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
        
        try:
            mise = int(mise)
        except ValueError:
            mise = 0
            return False
            
        if int(mise) > self.portefeuille:
            return False

        self.mise = mise
        self.portefeuille -= mise

        return True

    def lancer(self):
        return randint(1,6)

    def analyse(self, v1, v2, fenetreGame):

        valeur = v1 + v2
        self.resultatdes.config(text = valeur)

        if self.tour == 1:
            if valeur==7 or valeur==11:
                self.jeuGagne(fenetreGame)
                self.labelmessage.config(text = "Vous avez gagné {} dès le premier lancer !".format(2*self.mise))
                self.labelinstruction.config(text = "Vous pouvez remiser maintenant !")
                self.buttonsoumettre.config(text = "Parier !")
                self.afficher_un_doc()
            elif valeur==2 or valeur==3 or valeur==12:
                self.jeuPerdu(fenetreGame)
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
                self.jeuPerdu(fenetreGame)
                self.labelmessage.config(text = "Vous avez perdu votre mise de {}, on y croyait pourtant...".format(self.mise))
                self.labelinstruction.config(text = "ça donne envie de retenter non ?!")
                self.buttonsoumettre.config(text = "Parier !")

            elif valeur == self.getCible():
                self.jeuGagne(fenetreGame)
                self.labelmessage.config(text = "La cible a été atteinte !! Félicitations ! {} en plus !".format(2*self.mise))
                self.labelinstruction.config(text = "Plus d'argent = plus de paris !!!! oui c'est sain, pourquoi ?")
                self.buttonsoumettre.config(text = "Parier !")
                self.afficher_un_doc()
            
            else:
                self.labelmessage.config(text = "Un coup pour rien... Allez on peut mieux faire !")
                self.labelinstruction.config(text = "Faites chauffer les dés ! C'est pas les petits chevaux ici !")
                self.buttonsoumettre.config(text = "Lancer les dés !")

    def lancer_jeu(self, miseEntree, fenetreGame):


        if self.enCours():
            self.debut()
            miseOk = self.miser(miseEntree)

            if miseOk == False:

                popErreur = Toplevel()
                popErreur.title("mauvaise saisie !")

                ErreurLab = Label(popErreur, text = "erreur de saisie !", background = "white")
                ErreurLab.pack(side = "top", fill = "x")
                BoutonPopErreur = Button(popErreur, text = "Ok", command = popErreur.destroy)
                BoutonPopErreur.pack()
                popErreur.mainloop()
                return
        
        self.entrypari.config(state = DISABLED)
        self.labelannonceentry.config(text = "Vous avez misé : ")

        v1 = self.lancer()
        v2 = self.lancer()
        self.labeldes1.destroy()
        self.labeldes2.destroy()
        self.labeldes1_new = Label(fenetreGame, text = v1)
        self.labeldes1_new.grid(row = 4, column = 2)
        self.labeldes2_new = Label(fenetreGame, text = v2)
        self.labeldes2_new.grid(row = 4, column = 4)

        self.analyse(v1, v2, fenetreGame)

        self.labelcible.config(text = self.getCible())
        self.labelportefeuille.config(text = self.portefeuille)
        self.labelmaxatteind.config(text = self.palier_max_atteind)


    def afficher_un_doc(self):

        nbr_affichés = 0
        portefeuilleTemp = self.portefeuille
        while portefeuilleTemp >= self.palier_suivant:
            nbr_affichés += 1
            portefeuilleTemp = portefeuilleTemp - 25

        print("nbr_affichés : " + str(nbr_affichés))
        self.palier_suivant += nbr_affichés * 25

        self.labelpaliersuivant.config(text = self.palier_suivant)
        
        for i in range(0, nbr_affichés):    
            l = len(self.doc_non_montre)
            choix = randint(0,l)
            File_jeu = File()
            File_jeu.afficher_doc(self.doc_non_montre[choix][0], self.doc_non_montre[choix][1], self.doc_non_montre[choix][2])
            self.doc_non_montre.pop(choix)


 
    def recommencer_jeu(self, fenetreGame, popPerdu):
        
        fenetreGame.destroy()
        popPerdu.destroy()
        craps.voir_jeu()
        
    def retour_menu(self, fenetreGame, popPerdu):
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
        IntroLab.pack(side = "top", fill = "x")
        BoutonPopRegles = Button(popRegles, text = "Ok", command = popRegles.destroy)
        BoutonPopRegles.pack()
        popRegles.mainloop()


    def quitter(self, fenetreGame):
        popQuitter = Tk()
        popQuitter.title("Vous voulez quitter ?")

        QuitterLab = Label(popQuitter, text = "Vous pouvez quitter ou  recommencer une partie.", background = "white")
        QuitterLab.pack(side = "top", fill = "x")
        BoutonpopQuitterMenu = Button(popQuitter, text = "Retour au menu", command = lambda : self.retour_menu(fenetreGame, popQuitter))
        BoutonpopQuitterMenu.pack()
        BoutonpopQuitterRejouer = Button(popQuitter, text = "Recommencer le jeu", command = lambda : self.recommencer_jeu(fenetreGame, popQuitter))
        BoutonpopQuitterRejouer.pack()
        popQuitter.mainloop()


    def voir_jeu():

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
        game.entrypari = Entry(fenetreGame)

        game.labelcible = Label(fenetreGame, text = "pas encore de cible")
        game.labelannoncecible = Label(fenetreGame, text = "cible pour gagner :")

        game.labelmessage = Label(fenetreGame, text = "Vous devez entrer une valeur à miser pour commencer.")
        game.labelinstruction = Label(fenetreGame, text = "Une fois entrée, la valeur ne peut plus être changée jusqu'au résultat.")

        game.labelmaxatteind = Label(fenetreGame, text = game.palier_max_atteind)
        game.labelannoncemaxatteind = Label(fenetreGame, text = "Palier maximum atteind : ")

        game.resultatdes = Label(fenetreGame, text = 0)
        game.annonceresultatdes = Label(fenetreGame, text = "Resultat des dés : \n(on fait même ça pour vous !)")

        game.labelpaliersuivant = Label(fenetreGame, text = self.palier_suivant)
        game.labelannoncepaliersuivant = Label(fenetreGame, text = "La prochaine récompense si vous atteignez : ")

        game.buttonretourmenu = Button(fenetreGame, text = "retour au menu", command = lambda : game.quitter(fenetreGame))

        game.buttonsoumettre = Button(fenetreGame, text = "Parier !", command = lambda : lancer_recup_mise())

        def lancer_recup_mise():

            int_mise_donnee = game.entrypari.get()
            game.lancer_jeu(int_mise_donnee, fenetreGame)

        #game.IntroLab.pack()

        game.debut_jeu()

        #titre fenetreGame

        fenetreGame.title("jeu")

        #fin interface

        fenetreGame.mainloop()


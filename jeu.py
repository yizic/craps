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

class craps:
    def __init__(self, p):

        print("===============")
        print("=  C R A P S  =")
        print("===============")

        self.portefeuille = p
        self.mise = 0
        self.tour = 1
        self.cible = 0
        self.joue = True

    def affiche_regles(self):
        print("""Le Craps est un jeu de dés, que nous avons légèrement modifié dans le cadre de ce projet.
        L'ordinateur lance les dés, si au premier lancé vous obtenez 7 ou 11, vous doublez votre mise. Si vous obtenez 2, 3 ou 12, vous perdez.
        Pour toute autre valeur, vous relancez les dés, jusqu'à obtenir la même valeur de nouveau, ce qui doublera votre mise.
        Mais si dans l'intervalle vous obtenez un 7, vous perdez la mise.
        En fonction de votre portefeuille, vous obtenez des informations sur les développeurs de ce jeu.
        Nous avons choisi un jeu avec mise car il est facilement améliorable (multijoueur, système d'achat avec les gains...),
        et pour le côté mise - gains que nous trouvons attractif !
        """)

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

    def miser(self):
        mise = 0
        while(mise<=0 or mise > self.portefeuille):
            mise=input("\nVous avez {} en poche. Combien vous voulez miser ? ==> ".format(self.portefeuille))
            try:
                mise = int(mise)
            except ValueError:
                print("\t\tMerci d'entrer une valeur numérique")
                mise = 0
        self.mise = mise
        self.portefeuille -= mise

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

    def lancer_jeu():

        jeu = craps(500)

        jeu.affiche_regles()

        while jeu.enCours():
            jeu.debut()
            jeu.miser()
            while jeu.getJoue():
                jeu.analyse(jeu.lancer(), jeu.lancer())

        print("\nVous n'avez plus rien à miser ! C'est la fin !")
        
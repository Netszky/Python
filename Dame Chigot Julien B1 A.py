import string
import random
global couleur
ScoreB = 0
ScoreN = 0
def ChoixPlateau():
        global plateau
        print("1. Plateau Aleatoire\n")
        print("2. Plateau Normal\n")
        choixP = input("Quel type de plateau ?\n")
        if choixP == "1":
                plateau = [
                ["█","_","█","_","█","_","█","_","█","_","|0"],
                ["_","█","_","█","_","█","_","█","_","█","|1"],
                ["█","_","█","_","█","_","█","_","█","_","|2"],
                ["_","█","_","█","_","█","_","█","_","█","|3"],
                ["█","_","█","_","█","_","█","_","█","_","|4"],
                ["_","█","_","█","_","█","_","█","_","█","|5"],
                ["█","_","█","_","█","_","█","_","█","_","|6"],
                ["_","█","_","█","_","█","_","█","_","█","|7"],
                ["█","_","█","_","█","_","█","_","█","_","|8"],
                ["_","█","_","█","_","█","_","█","_","█","|9"],
]
                PlateauAleatoire(40)
        elif choixP == "2":
                plateau = [
                ["█","B","█","B","█","B","█","B","█","B","|0"],
                ["B","█","B","█","B","█","B","█","B","█","|1"],
                ["█","B","█","B","█","B","█","B","█","B","|2"],
                ["B","█","B","█","B","█","B","█","B","█","|3"],
                ["█","_","█","_","█","_","█","_","█","_","|4"],
                ["_","█","_","█","_","█","_","█","_","█","|5"],
                ["█","N","█","N","█","N","█","N","█","N","|6"],
                ["N","█","N","█","N","█","N","█","N","█","|7"],
                ["█","N","█","N","█","N","█","N","█","N","|8"],
                ["N","█","N","█","N","█","N","█","N","█","|9"],
                
]

def AffichePlateau():
    print("0","1","2","3","4","5","6", "7", "8", "9")
    for element in plateau:
        print(*element)

def PlateauAleatoire(nbpions):
    global plateau
    global i
    i = 0
    while i < nbpions :
        a = random.randrange(-1, 9, 1)
        b = random.randrange(-1, 10, 1)
        if plateau[b][a] == "_":
                c = random.randrange(1, 3 ,1)
                if c == 1:
                        plateau[b][a] = "B"
                else:
                        plateau[b][a] = "N"
                i += 1
        else: 
                pass

def ChoixDeplacement(couleur):
        global a
        global b
        global Move
        if couleur == 1:
                print("C'est aux Blancs de jouer (B)")
                choix = input("Pions a déplacer\n")
                a = int(choix[0])
                b = int(choix[1])
                while plateau[a][b] != "B":
                        print("Ce n'est pas un de tes pions ")
                        choix = input("Pions a déplacer\n")
                        a = int(choix[0])
                        b = int(choix[1])
        elif couleur == 2:
                print("C'est aux Noirs de jouer (N)")
                choix = input("Pions a déplacer\n")
                a = int(choix[0])
                b = int(choix[1])
                while plateau[a][b] != "N":
                        print("Ce n'est pas un de tes pions")
                        choix = input("Pions a déplacer\n")
                        a = int(choix[0])
                        b = int(choix[1])
        print("1. Haut gauche")
        print("2. Haut Droite")
        print("3. Bas Gauche")
        print("4. Bas Droite")
        print("5. Annuler Deplacement")
        print("6. Abandonner")
        Move = input()
def deplacementB():
        global ScoreB
        global ScoreN
        if Move == "1":
                if plateau[a-1][b-1] == "B":
                        print("Il ya deja un pion")
                        ChoixDeplacement(couleur)
                        deplacementB()
                elif plateau[a-1][b-1] == "_":
                        plateau[a-1][b-1] = "B"
                        plateau[a][b] = "_"
                        print("Vous avez deplacé votre pion")
                elif plateau[a-1][b-1] == "N" and plateau[a-2][b-2] == "_":
                        plateau[a-1][b-1] = "_"
                        plateau[a-2][b-2] = "B"
                        plateau[a][b] = "_"
                        ScoreB += 1
                        print("Vous avez mangez un pion\n")
                        print("Votre score est de",ScoreB,)
                elif plateau[a-1][b-1] == "N" and plateau[a-2][b-2] == "N":
                        print("Vous ne pouvez pas faire cela")
                else :
                        print("Hors limite")
                        ChoixDeplacement(couleur)
                        deplacementB()
        elif Move == "2":
                if plateau[a-1][b+1] == "B":
                        print("Il ya deja un pion")
                        ChoixDeplacement(couleur)
                        deplacementB()
                elif plateau[a-1][b+1] == "_":
                        plateau[a][b] = "_"
                        plateau[a-1][b+1] = "B"
                        print("Vous avez deplacé votre pion")
                elif plateau[a-1][b+1] == "N" and plateau[a-2][b+2] == "_":
                        plateau[a-1][b+1] = "_"
                        plateau[a-2][b+2] = "B"
                        plateau[a][b] = "_"
                        ScoreB += 1
                        print("Vous avez mangez un pion\n")
                        print("Votre score est de",ScoreB,)
                elif plateau[a-1][b+1] == "N" and plateau[a-2][b+2] == "N":
                        print("Vous ne pouvez pas faire cela")
                else :
                        print("Hors limite")
                        ChoixDeplacement(couleur)
                        deplacementB()
        elif Move == "3":
                if plateau[a+1][b-1] == "B":
                        print("Il ya deja un pion")
                        ChoixDeplacement(couleur)
                        deplacementB()
                elif plateau[a+1][b-1] == "_":
                        plateau[a][b] = "_"
                        plateau[a+1][b-1] = "B"
                        print("Vous avez deplacé votre pion")
                elif plateau[a+1][b-1] == "N" and plateau[a+2][b-2] == "_":
                        plateau[a+1][b-1] = "_"
                        plateau[a+2][b-2] = "B"
                        plateau[a][b] = "_"
                        ScoreB += 1
                        print("Vous avez mangez un pion\n")
                        print("Votre score est de",ScoreB,)
                elif plateau[a+1][b-1] == "N" and plateau[a+2][b-2] == "N":
                        print("Vous ne pouvez pas manger ce pion")
                else:
                        print("Hors limite")
                        ChoixDeplacement(couleur)
                        deplacementB()
        elif Move == "4":
                if plateau[a+1][b+1] == "B":
                        print("Il ya deja un pion")
                        ChoixDeplacement(couleur)
                        deplacementB()
                elif plateau[a+1][b+1] == "_":
                        plateau[a][b] = "_"
                        plateau[a+1][b+1] = "B"
                        print("Vous avez deplacé votre pion")
                elif plateau[a+1][b+1] == "N" and plateau[a+2][b+2] == "_":
                        plateau[a+1][b+1] = "_"
                        plateau[a+2][b+2] = "B"
                        plateau[a][b] = "_"
                        ScoreB += 1
                        print("Vous avez mangez un pion\n")
                        print("Votre score est de",ScoreB,)
                elif plateau[a+1][b+1] == "N" and plateau[a+2][b+2] == "N":
                        print("Vous ne pouvez pas manger ce pion")
                else:
                        print("Hors limite")
                        ChoixDeplacement(couleur)
                        deplacementB()
        elif Move =="5":
                ChoixDeplacement(couleur)
                deplacementB()
        elif Move =="6":
                print("Les Noirs ont gagné ! Loser")
                ScoreN = 20

def deplacementN():
        global ScoreB
        global ScoreN
        if Move == "1":
                if plateau[a-1][b-1] == "N":
                        print("Il ya deja un pion")
                        ChoixDeplacement(couleur)
                        deplacementN()
                elif plateau[a-1][b-1] == "_":
                        plateau[a][b] = "_"
                        plateau[a-1][b-1] = "N"
                        print("Vous avez deplacé votre pion")
                elif plateau[a-1][b-1] == "B" and plateau[a-2][b-2] == "_":
                        plateau[a-1][b-1] = "_"
                        plateau[a-2][b-2] = "N"
                        plateau[a][b] = "_"
                        ScoreN += 1
                        print("Vous avez mangez un pion\n")
                        print("Votre score est de",ScoreN,)
                elif plateau[a-1][b-1] == "B" and plateau[a-2][b-2] == "B":
                        print("Vous ne pouvez pas faire cela")
                else:
                        print("Hors limite")
                        ChoixDeplacement(couleur)
                        deplacementN()
        elif Move == "2":
                if plateau[a-1][b+1] == "N":
                        print("Il ya deja un pion")
                        ChoixDeplacement(couleur)
                        deplacementN()
                elif plateau[a-1][b+1] == "_":
                        plateau[a][b] = "_"
                        plateau[a-1][b+1] = "N"
                        print("Vous avez deplacé votre pion")
                elif plateau[a-1][b+1] == "B" and plateau[a-2][b+2] == "_":
                        plateau[a-1][b+1] = "_"
                        plateau[a-2][b+2] = "N"
                        plateau[a][b] = "_"
                        ScoreN += 1
                        print("Vous avez mangez un pion\n")
                        print("Votre score est de",ScoreN,)
                elif plateau[a-1][b+1] == "B" and plateau[a-2][b+2] == "B":
                        print("Vous ne pouvez pas faire cela")
                else:
                        print("Hors limite")
                        ChoixDeplacement(couleur)
                        deplacementN()
        elif Move == "3":
                if plateau[a+1][b-1] == "N":
                        print("Il ya deja un pion")
                        ChoixDeplacement(couleur)
                        deplacementN()
                elif plateau[a+1][b-1] == "_":
                        plateau[a][b] = "_"
                        plateau[a+1][b-1] = "N"
                        print("Vous avez deplacé votre pion")
                elif plateau[a+1][b-1] == "B" and plateau[a+2][b-2] == "_":
                        plateau[a+1][b-1] = "_"
                        plateau[a+2][b-2] = "N"
                        plateau[a][b] = "_"
                        ScoreN += 1
                        print("Vous avez mangez un pion\n")
                        print("Votre score est de",ScoreN,)
                elif plateau[a+1][b-1] == "B" and plateau[a+2][b-2] == "B":
                        print("Vous ne pouvez pas manger ce pion")
                else:
                        print("Hors limite")
                        ChoixDeplacement(couleur)
                        deplacementN()
        elif Move == "4":
                if plateau[a+1][b+1] == "N":
                        print("Il ya deja un pion")
                        ChoixDeplacement(couleur)
                        deplacementN()
                elif plateau[a+1][b+1] == "_":
                        plateau[a+1][b+1] = "N"
                        plateau[a][b] = "_"
                        print("Vous avez deplacé votre pion")
                elif plateau[a+1][b+1] == "B" and plateau[a+2][b+2] == "_":
                        plateau[a+1][b+1] = "_"
                        plateau[a+2][b+2] = "N"
                        plateau[a][b] = "_"
                        ScoreN += 1
                        print("Vous avez mangez un pion\n")
                        print("Votre score est de",ScoreN,)
                elif plateau[a+1][b+1] == "B" and plateau[a+2][b+2] == "B":
                        print("Vous ne pouvez pas manger ce pion")
                else:
                        print("Hors limite")
                        ChoixDeplacement(couleur)
                        deplacementN()
        elif Move =="5":
                ChoixDeplacement(couleur)
                deplacementN()
        elif Move =="6":
                print("Les Blancs ont gagné ! Loser ")
                ScoreB = 20
def ObligationMangerB():
        global ScoreB
        global Tour
        a = 0
        b = 0
        i = 0
        while i < 50:
                if b <= 9 :
                        if plateau[a][b] == "B":
                                i += 1
                                if plateau[a+1][b-1] == "N" and plateau[a+2][b-2] == "_":
                                        c = a+1
                                        d = b-1
                                        print("Le pion",a,b,"Est oblige de manger le pion",c,d,"!")
                                        plateau[a][b] = "_"
                                        plateau[a+1][b-1] = "_"
                                        plateau[a+2][b-2] = "B"
                                        ScoreB += 1
                                        b += 1
                                        Tour = 1
                                elif plateau[a+1][b+1] == "N" and plateau[a+2][b+2] == "_":
                                        c = a+1
                                        d = b+1
                                        print("Le pion",a,b,"Est obligé de manger le pion",c,d,"!")
                                        plateau[a][b] = "_"
                                        plateau[a+1][b+1] = "_"
                                        plateau[a+2][b+2] = "B"
                                        ScoreB += 1
                                        b += 1
                                        Tour = 1
                                else:
                                        b += 1
                                        pass
                        else:
                                i += 1
                                b += 1
                else:
                        b = 0
                        a += 1
def ObligationMangerN():
        global ScoreN
        global Tour
        a = 0
        b = 0
        i = 0
        while i < 50:
                if b <= 9:
                        if plateau[a][b] == "N":
                                i += 1
                                if plateau[a-1][b-1] == "B" and plateau[a-2][b-2] == "_":
                                        c = a-1
                                        d = b-1
                                        print("Le pion",a,b,"Est oblige de manger le pion",c,d,"!")
                                        plateau[a][b] = "_"
                                        plateau[a-1][b-1] = "_"
                                        plateau[a-2][b-2] = "N"
                                        ScoreN += 1
                                        b += 1
                                        Tour = 0
                                elif plateau[a-1][b+1] == "B" and plateau[a-2][b+2] == "_":
                                        c = a-1
                                        d = b+1
                                        print("Le pion",a,b,"Est obligé de manger le pion",c,d,"!")
                                        plateau[a][b] = "_"
                                        plateau[a-1][b+1] = "_"
                                        plateau[a-2][b+2] = "N"
                                        ScoreN += 1
                                        b += 1
                                        Tour = 0
                                else:
                                        b += 1
                                        pass
                        else:
                                i += 1
                                b += 1
                else:
                        b = 0
                        a += 1
ChoixPlateau()
global Tour
Tour = 0
while ScoreB or ScoreN < 20:
        if Tour == 0:
                ObligationMangerB()
                AffichePlateau()
                if Tour == 1:
                        ObligationMangerN()
                else:
                        couleur = 1
                        ChoixDeplacement(couleur)
                        deplacementB()
                        AffichePlateau()
                        Tour = 1
        elif Tour == 1:
                ObligationMangerN()
                AffichePlateau()
                if Tour == 0:
                        ObligationMangerB()
                else:
                        couleur = 2
                        ChoixDeplacement(couleur)
                        deplacementN()
                        AffichePlateau()
                        Tour = 0

from ast import ExceptHandler
import datetime
from logging import exception
#from tkinter.tix import Select
import mysql.connector



class Employe :
    # Definition du constructeur 
    def __init__(self, matricule, nom, prenom, dateNaissance, dateEmbauche, salaireBase):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
        self.dateEmbauche = dateEmbauche
        self.salaireBase = salaireBase

    # Definition des methodes de la classe Employe
    
    def calcul_Age(self):
        from datetime import datetime
        anneeActuelle = datetime.today().year 
        anneeNaissance = datetime.strptime(lireStrNaissance, '%d/%m/%Y').date().year
        age = anneeActuelle - anneeNaissance
        #print(age)
        return age

    def calcul_Anciennete(self):
        from datetime import datetime
        anneeActuelle = datetime.today().year
        anneeEmbauche = datetime.strptime(lireStrEmbauche, '%d/%m/%Y').date().year
        anciennete = anneeActuelle - anneeEmbauche
        return anciennete

    def calcul_Augmentation(self):
        if self.calcul_Anciennete() < 5:
            augmentation = lireSalaireBase * 0.02
            return augmentation
        elif self.calcul_Anciennete() < 10:
            augmentation = lireSalaireBase * 0.05
            return augmentation
        else :
            augmentation = lireSalaireBase * 0.1
            return augmentation

    def afficherEmploye(self):
        print(" ")
        print("*************** INFORMATIONS EMPLOYE *******************")
        print(" ")
        
        print("-    Matricule: " + str(self.matricule))
        print(" ")

        nomComplet = lireNom.upper() + " " + lirePrenom.capitalize()
        print("-    Nom complet: " + nomComplet)
        print(" ")

        print('-    Age:  ' + str(self.calcul_Age()) + '  ans')
        print(" ")

        print('-    Anciennete:  ' + str(self.calcul_Anciennete()) + '  ans')
        print(" ")

        salaire_total = lireSalaireBase + self.calcul_Augmentation()
        print('-    Salaire:  ' + str(salaire_total) + '  Euros/an')
        print(" ")

        print('-    Augmentation annuelle en fonction anciennete: ' + str(self.calcul_Augmentation()) + ' Euros/an')
        print(" ")

MonEntreprise = mysql.connector.connect(
  host="localhost",
  user="dso",
  password="Bisous",
  database="MonEntreprise"
)
mycursor = MonEntreprise.cursor()
sql = "INSERT INTO Employes (Matricule, Nom, Prenom, Age, Anciennete, Salaire) VALUES (%s, %s, %s, %s, %s, %s)"
 
# Lire les donnes employes depuis un fichier

fichierEmployes = open("DB_Employes.txt", "r") # ouvrir le fichier de donnees en lecture

for x in fichierEmployes:
    lineListEmploye = x.split(";") # Récupère une ligne du fichier et la transforme en list 
#   print(lineListEmploye) # affiche chaque ligne du fichier comme une liste
    lireMatr = lineListEmploye[0]
    lireNom = lineListEmploye[1]
    lirePrenom = lineListEmploye[2]
    from datetime import datetime
    lireStrNaissance = lineListEmploye[3]
    lireStrEmbauche = lineListEmploye[4]
    lireSalaireBase = lineListEmploye[5].strip("\n")
    lireSalaireBase = float(lireSalaireBase)

    # Instanciation des Employes
    myEmploye = Employe(lireMatr, lireNom, lirePrenom, lireStrNaissance, lireStrEmbauche, lireSalaireBase) 
    salaireTotal = myEmploye.salaireBase + float(myEmploye.calcul_Augmentation())
    val = (myEmploye.matricule, myEmploye.nom, myEmploye.prenom, myEmploye.calcul_Age(), myEmploye.calcul_Anciennete(), salaireTotal )
    mycursor.execute(sql, val)


MonEntreprise.commit()
  
fichierEmployes.close()










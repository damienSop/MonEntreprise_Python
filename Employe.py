from ast import ExceptHandler
import datetime
from logging import exception


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
        anneeNaissance = datetime.strptime(lireStrNaissance, '%d-%m-%Y').date().year
        age = anneeActuelle - anneeNaissance
        #print(age)
        return age

    def calcul_Anciennete(self):
        from datetime import datetime
        anneeActuelle = datetime.today().year
        anneeEmbauche = datetime.strptime(lireStrEmbauche, '%d-%m-%Y').date().year
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
 
try:     
    # Entrer les donnees Employe
    lireMatr = str(input("Entrez le matricule: "))

    lireNom = str(input("Entrez le nom: "))
    lirePrenom = str(input("Entrez le prenom: ")) 

    from datetime import datetime
    lireStrNaissance = str(input("Entrer date de naissance jj-mm-aaaa: "))
    
    lireStrEmbauche = str(input("Entrer date embauche jj-mm-aaaa: "))

    lireSalaireBase = float(input("Entrez le salaire de base: "))


    # Instanciation de la classe Employe
    myEmploye = Employe(lireMatr, lireNom, lirePrenom, lireStrNaissance, lireStrEmbauche, lireSalaireBase) 
    myEmploye.afficherEmploye()
    

except Exception as ex:
    print(ex)
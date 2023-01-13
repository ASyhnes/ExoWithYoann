#Exercice 1 (clé) :
#1) Créer une classe Voiture composé des attributs suivants :
#- modèle
#- marque
#- prix
#Créer 2 objets à partir de la classe Voiture et afficher le prix de ces objets
#2) Créer une classe Avion composé des attributs suivants :
#- modèle
#- marque
#- nbr _siege
#- distance (nbr kilomètre que peut parcourir l’avion)
#Créer un objet à partir de cette classe puis afficher les attributs de cet obje

class Voiture:
    @staticmethod
    def get_definition():
        #Donne la définition d'une voiture.
        return (
        "on monte dedans, ça a des roue \n"
        "et ça avance."
        )
    def __init__(self,modele,marque,prix):
        self.modele = modele
        self.marque = marque
        self.prix = prix

voiture1 = Voiture('Modus','Renaud',4000)
voiture2 = Voiture('Model S','Tesla',65000)


print(voiture2.modele)
print(Voiture.get_definition())

class Avion:
    @staticmethod
    def get_definition():
        #Donne la définition d'un avion.
        return (
        "on monte dedans, ça a des ailles \n"
        "et ça avance, mais en vollant."
        )
    def __init__(self,modele,marque,nbr_siege,distance):
        self.modele = modele
        self.marque = marque
        self.nbr_siege = nbr_siege
        self.distance = distance

avion1 = Avion('A480','Airbus',40, 50000)
avion2 = Avion('A330','Airbus',67,400000)


print(avion2.distance)
print(avion1.distance)
print(Avion.get_definition())


#1) Créer une classe Humain composé des attributs suivants:
#- age
#- nom
#- prenom
#Créer 2 objets à partir de cette classe et afficher le prénom et l'âge de ces objets.

class Human:
    def __init__(self, age, name, firstname):
        self.name = name
        self.age = age
        self.firstname = firstname

human1 = Human(36, "Charpentier", "Jean")
human2 = Human(33, "leboulag", "Julie")

print(human1.firstname,human1.age)
print(human2.firstname,human1.age)


#2) Modifier cette classe et créer une méthode dans la classe Humain permettant de
#modifier le nom d’un objet et une méthode permettant de modifier le prénom d’un
#objet. Par la suite, tester ces méthodes.

class Human:
    def __init__(self, age, name, firstname):
        self.name = name
        self.age = age
        self.firstname = firstname


    def rename(self, name):
        self.name = name

 # 3) Modifier cette classe et créer une fonction grandir qui augmente l'âge de 1 an
 # d’un objet.
    def plusyear(self):
        self.age = self.age + 1


# Modifier la fonction grandir pour augmenter l'âge d’un objet de la classe Humain
# de la valeur de votre choix.


    def redefinyear(self):
        age = input("entrez le nouvel age: ")
        self.age = age






human1 = Human(36, "Charpentier", "Jean")
print(human1.name,human1.age)
human1.rename("david")
print(human1.name,human1.age)
human1.plusyear()
print(human1.age)
human1.redefinyear()
print(human1.age)


#Exercice 3 (clé) :
#1) Créer une classe Python nommée CompteBancaire qui représente un compte
#bancaire, ayant pour attributs : numeroCompte, nom (nom du propriétaire du
#compte), solde.
#2) Créer une méthode Versement() qui gère les versements.
#3) Créer une méthode Retrait() qui gère les retraits.
#4) Créer une méthode afficher() permettant d’afficher les détails sur le compte.
#5) Tester le bon fonctionnement de la classe CompteBancaire.

#Exercice 3 (clé) :
#1) Créer une classe Python nommée CompteBancaire qui représente un compte
#bancaire, ayant pour attributs : numeroCompte, nom (nom du propriétaire du
#compte), solde.
#2) Créer une méthode Versement() qui gère les versements.
#3) Créer une méthode Retrait() qui gère les retraits.
#4) Créer une méthode afficher() permettant d’afficher les détails sur le compte.
#5) Tester le bon fonctionnement de la classe CompteBancaire.

class CompteBancaire:
    def __init__(self, numerocompte, nom, solde):
        self.numerocompte = numerocompte
        self.nom = nom
        self.solde = solde

    def versement(self):
        self.solde = self.solde + int(input("montant du versement: "))
        print(self.solde)

    def retrait(self):
        self.solde = self.solde - int(input("montant du retrait: "))
        print(self.solde)

    def afficher(self):
        print(self.numerocompte, self.nom, self.solde)

#test du bon fonctionnement
client1 = CompteBancaire(345266728275, "Durant", -450)
print(client1.solde)
client1.versement()
client1.retrait()
client1.afficher()


#Exercice 4 (secondaire) :
#Créer une classe Personne ayant trois attributs définissant certaines caractéristiques
#d’une personne réelle : taille, poids et age.
#Cette classe aura :
#● une méthode imc() qui détermine l’IMC de la personne,
#● une méthode interpretation() qui affiche "Insuffisance pondérale" si l’IMC est
#inférieur ou égale à 18,5 et qui affiche "obésité" si l’IMC est supérieur ou
#égale à 30.
#Rappel : l’IMC (Indice de masse corporelle) est donné par la formule
#poids/taille**2 avec le poids en kg et la taille en m.

class Personne:
    def __init__(self, taille, poids, age):
        self.taille = taille
        self.poids = poids
        self.age = age


    def calc_imc(self):
        imc = self.poids/self.taille**2
        print("l'IMC est de: ", imc)
        return(imc)


    def interp_imc(self):
        # !!!!!!!!avoir pendant la correction: e n'ai pas trés bien saisi comment une méthode peut en appeller une autre:
        #la methode "def calcimc" me permet de calculer l'imc. J'aimerai ne pas avoir à le refaire une deuxiéme fois
        #comme fait pour le moment dans "def interpimc"
        imc = self.poids / self.taille ** 2
        if imc <= 18.5:
            print("Insuffisance pondérale")
        elif imc >= 30:
            print("Obésité")
        else:
            print("IMC normale")





juju = Personne(1.80, 78, 56)
print(juju.poids)
juju.calc_imc()
juju.interp_imc()




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
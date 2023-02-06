#Exercice 5 (secondaire) :
#Soit à développer une application pour la gestion d’un stock. Un article est caractérisé
#par son numéro de référence, son nom, son prix de vente et une quantité en stock. Le
#stock est représenté par une collection d’articles.
#Créer la classe article contenant les éléments suivants :
#● Les attributs/propriétés.
#● Un constructeur d’initialisation.
#● La méthode ToString().>https://www.delftstack.com/fr/howto/python/tostring-equivalent-python/$

#Dans la classe Program créer :
#Le stock sous forme d'une collection d’articles de votre choix. #crer une liste et .append

#Un menu présentant les fonctionnalités suivantes : #choisir les option:1, 2, 3 ect....???
#1. Rechercher un article par référence. #input>ref>imprim propriété
#2. Ajouter un article au stock en vérifiant l’unicité de la référence. #input>nouvel articl> propriété?>verif ref
#3. Supprimer un article par référence. #input ref artic a suprimer> chercher article>suprimer
#4. Modifier un article par référence.
#5. Rechercher un article par nom.
#6. Rechercher un article par  intervalle de prix de vente.
#7. Afficher tous les articles>re'def str

class Article:
    def __init__(self, nbref, nom, prixvente, quantstock):
        self.nbref = nbref
        self.nom = nom
        self.prixvente = prixvente
        self.quantstock = quantstock

    def __repr__(self):
        """Représentation de l'article."""
        return f" {self.nbref, self.nom, self.prixvente, self.quantstock}"


class Programm:
    """Creer le programme."""

    def __init__(self):
        """Initialise le stock d'article."""
        self.stock = []

    def add_artcl(self, artcl):
        """Ajoute un article."""
        y = input("ref 3 nombre \n"), input("nom de l'article \n"), input("prix \n"), input("quantité en stock ? \n")
        self.stock.append(y)

    def remove_artcl(self, artcl):
        """Enleve un article."""
        index = self.stock.index(artcl)
        del self.stock[index]



#debut du programe


Gestionstock = Programm()

choix = ("que souhaitez vous faire:"
      "\n 1: ajouter un article "  # (en verifier qu'il a une ref unique)
      "\n 2: rechercher un article par ref "
      "\n 3: rechercher un article par nom"
      "\n 4: rechercher un article par prix"  # liste de tranche de prix
      "\n 5: afficher tout les articles"
      "\n 6: modifier un article"  # liste choix>modifier
      "\n 7: End")

print(choix)
x = input()
def choix_multiple():
    print(choix)



while x != 7:
    if x == str(1):
        y = Article("","","","")
        Gestionstock.add_artcl(y)
        #debug
        print(y)
        print("debug1")
        print(Gestionstock.stock)


    elif x == str(2):
        print("debug2")


    elif x == str(3):
        print("debug3")


    elif x == str(4):
        print("debug4")


    elif x == str(5):
        print("debug5")


    elif x == str(6):
        print("debug6")


    else:
        print("debug boucle a recommancer")

    choix_multiple()
    x = int(input())

        ###"!!!j'arrétte avec la problématique suivante: mon choix multiple ne fonctionne pas et ma boucle reste boucler sur la fonction initialement choisi dans X
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

    def __str__(self):
        return f'Article:(Ref={self.nbref}, Nom={self.nom}, Prix de vente={self.prixvente}, En stock={self.quantstock})'

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
        for obj in (self.stock):
            if obj[0] == y[0]:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n"
                      "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n"
                      "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n"
                      "Error: 'ref 3 nombre' already exists in another object, retry !! \n"
                      "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n"
                      "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n"
                      "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
                break
        else:
            self.stock.append(y)
            print("The new object has been added to the list")

    def search_ref(self):
        search_ref_param = input("entrez la ref de l'objet à trouver: \n")
        for artcl in (self.stock):
            if artcl[0] == search_ref_param:
                print("objet trouvé:", artcl)
                break
            else:
                print("objet non référencé")

    def search_name(self):
        search_ref_param = input("entrez le nom de l'objet à trouver: \n")
        for artcl in (self.stock):
            if artcl[1] == search_ref_param:
                print("objet trouvé:", artcl)
                break
            else:
                print("objet non référencé")

    def search_prix(self):
        search_ref_param = input("entrez le prix pour afficher les objets: \n")
        for artcl in (self.stock):
            if artcl[2] == search_ref_param:
                print(obj, "objet(s) trouvé(s):", artcl)

            else:
                print("objet non référencé")

    def remove_artcl(self, artcl):
        """Enleve un article."""
        index = self.stock.index(artcl)
        del self.stock[index]

    def print_all_article(self):
        print(Gestionstock.stock)

    def modif_article(self):
        chx = input("entrez la ref de l'objet à modifier : \n")
        for artcl in (self.stock):
            if artcl[0] == chx:
                print("que voulez vous changer? \n"
                      "1 : ref \n"
                      "2 : nom \n"
                      "3 : prix \n"
                      "4 : quantité\n")
                chx2 = str(input())
                 '''if chx2 == str(1):                                        !!!!!!!!!!#bug ici 'unbexpected indent'!!!!!!!
                        print("debug")
                    if chx2 == str(2):
                        print("debug")
                    if chx2 == str(3):
                        print("debug")
                    if chx2 == str(4):
                        print("debug")'''

        else:
            print("mauvaise comande")






#debut du programe


Gestionstock = Programm()

choix = ("que souhaitez vous faire:"
      "\n 1: ajouter un article "  #ok
      "\n 2: rechercher un article par ref " #ok> la methode __str__ ne marche pas bien
      "\n 3: rechercher un article par nom" #ok> la methode __str__ ne marche pas bien
      "\n 4: rechercher un article par prix"  #ok> la methode __str__ ne marche pas bien
      "\n 5: afficher tout les articles" #ok
      "\n 6: modifier un article"  # liste choix>modifier
      "\n 7: End")

def choix_multiple():
    print(choix)

print(choix)
x = str(input())




while x != str(7):

    if x == str(1):  #fonctionne ok
        y = Article("","","","")
        Gestionstock.add_artcl(y)
        #debug
        print(repr(y))
        print("debug1")

    elif x == str(2):
        Gestionstock.search_ref()
        # debug
        print(y)
        print("debug2")


    elif x == str(3):
        Gestionstock.search_name()
        # debug
        print(y)
        print("debug3")


    elif x == str(4):
        Gestionstock.search_prix()
        # debug
        print(y)
        print("debug4")


    elif x == str(5):
        print(Gestionstock.stock)
        print("debug5")



    elif x == str(6):
        Gestionstock.modif_article()
        print("debug6")


    else:
        print("COMMANDE NON VALIDE!!!")

    choix_multiple()
    x = str(input())

        ###"!!!j'arrétte avec la problématique suivante: mon choix multiple ne fonctionne pas et ma boucle reste boucler sur la fonction initialement choisi dans X
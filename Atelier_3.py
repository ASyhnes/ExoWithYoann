'''Exercice 1 (clé) :
Créer une liste contenant les jours de la semaine puis :
- Afficher la liste
- Afficher la première et dernière valeur de la liste
- Afficher la quatrième valeur de la liste semaine.
- Remplacer le jour de la semaine “samedi” par “dimanche”.
- Échanger le premier et le dernier élément de la liste.
- Afficher la liste'''

JSemaine = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

'- Afficher la liste'
print (JSemaine)

'- Afficher la première et dernière valeur de la liste'
print (JSemaine[0],JSemaine[-1])

'- Afficher la quatrième valeur de la liste semaine.'
print (JSemaine[3])

'- Remplacer le jour de la semaine “samedi” par “dimanche”.'
JSemaine = [elem.replace('Samedi', 'Dimanche') for elem in JSemaine]
print (JSemaine)

'- Échanger le premier et le dernier élément de la liste.'

JSemaine[0], JSemaine[-1] = JSemaine[-1], JSemaine[0]
print(JSemaine)


'''Exercice 2 (clé) :
Créer une liste contenant quatre nombres entiers : 10, 20, 30, 40
Par la suite :
- Ajouter un élément entier dans la liste
- Supprimer l’élément à la position 0 de la liste
- Supprimer l’élément 40 de la liste
- Ajouter le nombre de votre choix dans la liste
- Afficher le résultat de l'addition du premier et deuxième élément de la liste
- Créer le test suivant : Si le premier nombre de la liste est plus grand que le dernier
nombre de la liste afficher “Le premier nombre est plus grand que le dernier de la liste”.
'''

NE = [10,20,30,40]

"- Ajouter un élément entier dans la liste"
NE.insert(2,22)
print(NE)

"- Supprimer l’élément à la position 0 de la liste"
NE.pop(0)
print(NE)

"- Supprimer l’élément 40 de la liste"
NE.remove(40)
print(NE)

"- Ajouter le nombre de votre choix dans la liste"
NE.append(662)
print(NE)

"- Afficher le résultat de l'addition du premier et deuxième élément de la liste"
print(NE[0]+NE[1])

''''- Créer le test suivant : Si le premier nombre de la liste est plus grand que le dernier
nombre de la liste afficher “Le premier nombre est plus grand que le dernier de la liste”.'''

if NE[0]>NE[-1]:
    print('Le premier nombre est plus grand que le dernier de la liste')
else:
    print("Le premier nombre n'est pas plus grand que le dernier de la liste")

'''Créer un algorithme qui transforme une ligne en une liste de mots.
Exemple :
“Ceci est un test” => [“Ceci”, “est”, “un”, “test”]
'''

str = "Ceci n'est pas du code"
print(str.split())

'''Exercice 4 (secondaire) :
Un professeur souhaite interroger ses élèves dans un ordre aléatoire. Créer une liste d’élèves
puis écrire un programme qui mélange cette liste aléatoirement.
'''

LE = ['Julien','Madisson','Edwin','Nelson','Lisa','Maya','Chloé']
print(LE)
import random
random.shuffle(LE)
print(LE)


'''Exercice 5 (secondaire) :
=> Partie 1
Créer une liste de nombre entiers qui contient de 0 à n entiers
Par la suite :
- Demander à l’utilisateur de saisir un nombre
- Demander à l’utilisateur de saisir une position
- Ajouter le nombre dans liste à la position saisi par l’utilisateur. Vous devez vérifier que la
position est correcte, en cas d’erreur afficher le message suivant “Position
incorrect”.'''

import random
N = random.sample(range((int(input("choisissez le plus petit nombre entier"))), (int(input("choisissez le plus grand nombre entier que vous voulez")))), (int(input("choisissez le nombre d'éléments que vous voulez voir (plus petit que le dernier nombre rentré SVP)"))))
print(N)


NouveauNombre = int(input("Choisissez un nouveau nombre"))
NouvellePosition = int(input("choisissez une position"))

N.insert(NouvellePosition,NouveauNombre)
print(N)




'''=> Partie 2
Modifier l’algorithme de la partie 1 :
- Au début, demander à l’utilisateur s' il souhaite ajouter ou supprimer un nombre dans la
liste.
- Si l’utilisateur saisit "ajouter”, reprenez l’algorithme développé dans la partie 1 pour
ajouter un nombre dans la liste.
- Si l’utilisateur saisit “supprimer”, demander à l’utilisateur le nombre qu’il souhaite
supprimer, puis supprimer ce nombre.
- Sinon afficher le message suivant “Erreur'''

N = random.sample(range((int(input("choisissez le plus petit nombre entier"))), (int(input("choisissez le plus grand nombre entier que vous voulez")))), (int(input("choisissez le nombre d'éléments que vous voulez voir (plus petit que le dernier nombre rentré SVP)"))))
print(N)

AjtSupr = input('''souhaitez vous "ajouter" ou "suprimer" un nombre dans cette liste ?''' )

if AjtSupr == "ajouter":
    NouveauNombre = int(input("Choisissez un nouveau nombre"))
    NouvellePosition = int(input("choisissez une position"))

    N.insert(NouvellePosition, NouveauNombre)
    print(N)
elif AjtSupr == "suprimer":
    NouveauNombre = int(input("Choisissez un nombre à suprimer"))
    N.remove(NouveauNombre)
    print(N)

else:
    print("Erreur")

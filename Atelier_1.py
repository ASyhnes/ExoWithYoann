'''Exercice 1 (clé) :
    1) Créer un programme qui affiche le message suivant “Hello World”
    2) Utilisez la fonction input() pour demander à l’utilisateur de saisir un mot, puis afficher ce
    mot'''

print("Hello World")
name = input("Rentrez votre nom")

print("bonjour ",name)

'''Exercice 2 (clé) :
Écrire un programme avec deux variables G et D contenant des chiffres différents, puis échanger
les chiffres de ces deux variables (a doit contenir le chiffre de b et inversement). Afficher le
contenu de a et de b.'''

PL = name[0]



G = 3
D = 30
import time

time.sleep(1)
print('G = ',G)
time.sleep(1)
print('D = ',D)
time.sleep(2)
print("inversement G et D:")

time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
G, D = D, G
print('TADAAAAAAAAAAA')
time.sleep(1)
print('G = ',G)
print('D = ',D)


'''Exercice 3 (clé) :
x = 2
Y = Y+1
Afficher le résultat de ce calcul de trois manières différentes (indice : Vous pouvez utiliser la
fonction format() vue en cours).'''


time.sleep(1)
y = 2
x = y+1
print( "y = 2")
print( "x = y+1")
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
print("du coup... faut calculer ce bousin?")
time.sleep(1)
print("bon ben....")
print(x)
time.sleep(1)
txt = "on peux aussi écrire {an:.2f} !"
print(txt.format(an = x))
time.sleep(1)
print("sinon en braille ça s'écrit")
for i in range (x):
      print('.')


print('Exercice 4 (clé) :\n=> Partie 1\nÉcrire un programme, qui définit 3 variables : une variable de type texte, une variable de type\nnombre entier, une variable de type nombre décimal et qui affiche leur type (indice : la fonction\ntype() retourne le type d’un objet).\n=> Partie 2\nModifier ce programme en créant les 3 variables en une seul ligne')


x = 1
y = "deux"
z = 3.00

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

variable = {(x,1),(y,"deux"),(z,3.0)}
print(type(x),type(y),type(z))

print('Exercice 5')
'''Exercice 5 (secondaire) :
entier = 10
chaine = "eleve
"
Reprendre le programme et transformer la variable entier en une chaîne de caractère,
additionner cette variable transformée avec la variable chaine et afficher le résultat.'''
entier = 10
str(entier)
chaine = 'eleves'
type(entier)
Nombre_Eleve = str(entier)
classe = Nombre_Eleve + " " + chaine
print(classe)

'''Exercice 6 (secondaire) :
Écrire un programme qui demande à l’utilisateur de saisir une longueur et une largeur d’un
rectangle (indice : pensez à utiliser la fonction input()), puis affiche l’aire du rectangle.'''

print("Nous allons calculer la superficie d'un rectangle en fonction de sa largeur et de sa longueur.")
L = int(input("Veuillez rentrer une longueur L"))
l = int(input("Veuillez rentrer une largeur l"))

print("l'air du rectangle est de ", L*l,". reste à savoir si c'est des CM² ou autre chose...")
print("FIN DE L'ATTELLIER 1")
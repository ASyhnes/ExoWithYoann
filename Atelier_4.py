#Exercice 1 (clé) :
#=> Partie 1
#- Utiliser une boucle for pour afficher 10 fois le message suivant : “J’aime programmer
#avec Python !”

for i in range(0,10):
    print("J'aime programer avec Python (et ça aurait été pratique pour les punitions! ")

#=> Partie 2
#- Créer une liste d’animaux contenant les éléments suivants : “baleine”, “chien, “chat”,
#“brebis”, “loup”.
#- Utiliser une boucle for pour afficher les animaux (sans utiliser la fonction range()).
#- Utiliser une boucle for pour afficher les animaux de la liste ainsi que leur position au sein
#de la liste (indice : pensez à utiliser la fonction range()).

listeanimaux = ["baleine","chien","chat","brebis","loup"]

for animal in listeanimaux:
    print(animal)
for i in range (0,(len(listeanimaux))):
    print (listeanimaux[i],i)

#Exercice 2 (clé) :
#1) Créer une variable égale à 0.
#2) Utiliser une boucle while pour afficher la valeur de x tant que celle-ci est inférieur ou égal
#à 10. Penser à incrémenter x de 1 dans la boucle.
#3) Créer un algorithme qui demande à un utilisateur de saisir un nombre, tant que ce
#nombre est différent de 10 demander à l’utilisateur de saisir un nombre

x = 0
while x <= 10:
    print(x)
    x+=1

y = (int(input("entrez un nombre")))
while y != 10:
    y = (int(input("entrez un nombre")))

9
#Exercice 3 (clé) :
#1) Créer une variable contenant un nombre de votre choix entre 0 et 100
#2) Créer un algorithme qui demande à l’utilisateur de saisir un nombre puis qui vérifie si le
#nombre saisi est égal à la variable que vous avez créé. Tant que le nombre est différent,
#afficher le message suivant si le nombre contenu dans la variable est plus grand : “Le
#nombre est plus grand”, si le nombre contenu dans la variable est plus petit : “Le nombre
#est plus petit”, puis demander à l’utilisateur de retenter et de saisir à nouveau un
#nombre.

y = 9
print('''il faut trouver "le bon nombre"''')
z = (int(input("entrez un nombre")))
while y != z:
    if y < z:
        print('''votre nombre est plus grand que "le bon nombre"''')
    else:
        print('''votre nombre est plus petit que "le bon nombre"''')
    z = (int(input("entrez un nombre")))
print("parfait, c'est le bon nombre")

#1) Créer un algorithme qui demande à l’utilisateur de saisir une hauteur et une longueur
#puis qui affiche un rectangle constitué d’étoile ‘*’

l = int((input("entrez un nombre pour la longueur")))
h = int((input("entrez un nombre pour la hauteur")))
for i in range(h):
    print ("*"*l)

#2) Modifier l’algorithme pour que celui permette à l’utilisateur de choisir le symbole
#constituant le rectangle. Exemple avec le symbole “h”.

simbol = (input("choisissez un symbol, une lettre, un chiffre..."))
for i in range(h):
    print (simbol*l)

#Exercice 5 (secondaire) :
#En utilisant une boucle for, créer un programme qui affiche un sapin (taille décidé par
#l’utilisateur) comme ci-dessous.

h = int(input("choissisez une hauteur de sapin"))
e = " "
t = "^"


for i in range(h):
    print(e*h,t*i)
    h -= 1
    i += 1





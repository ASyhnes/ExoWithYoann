#Exercice 1 (clé) :
#) Créer une fonction qui prend en argument 2 nombres et retourne leur somme multiplié
#par 2.
#2) Créer une fonction qui retourne la moyenne de 2 nombres.

def deuxnombres(n,m):
    somme = n * m
    print("le nombre multiplié par 2 donne :",somme)

n = int(input("Choisissez un nombre : "))
m = int(input("Choisissez un nombre : "))
deuxnombres(n,m)

def moyennedeuxnombres(n,m):
    moy = (n * m)/2
    print("la moyenne des deux nombres donne :", moy)

moyennedeuxnombres(n,m)

#Exercice 2 (clé) :
#1) Créer une fonction qui prend en entrée 2 nombres et qui retourne le plus grand de ces 2
#nombres.
#2) Créer une fonction qui prend en entrée 2 nombres et qui retourne le plus petit de ces 2
#nombres.
#3) Créer un programme qui demande à l’utilisateur de saisir un premier nombre puis un
#deuxième nombre et qui retourne le plus grand et le plus petit de ces nombres
#4) Modifier le programme pour que celui-ci prenne en compte le cas où les nombres sont
#égaux.

def deuxnombre_A(n1,n2):
    f = "le plus grand nombre est :"
    if n1>n2:
        print(f)
        resulta =  n1
    elif n2>n1:
        print(f)
        resulta =  n2
    else:
        resulta = "les nombres sont égaux"
    return resulta

print(deuxnombre_A(int(input("Choisissez un nombre : ")),int(input("Choisissez un deuxiéme nombre : "))))


#Exercice 3 (clé) :
#1) Créer une fonction permettant de calculer l’aire d’un triangle
#2) Créer une fonction retournant la valeur de l'hypoténuse d’un triangle rectangle en
#prenant en entrée les 2 plus petits côtés du triangle (théorème de pythagore).

def aire_triangle(b,h):
    aire = b * h /2
    return aire

print("la surface du triangle est de :",aire_triangle(int(input("Choisissez un nombre pour la base du triangle : ")), int(input("Choisissez un nombre pour la hauteur du triangle : "))))

def hypot_triangle(a,b):
    hypot = (a ** 2 + b ** 2) ** 0.5 #il existe aussi la fonction sqrt pour les racines6
    return hypot

print("l'hypoténuse du triangle est de :",hypot_triangle(int(input("Choisissez un nombre pour le plus petit coté : ")), int(input("Choisissez un nombre pour le plus grand coté : "))))


#Exercice 4 (clé) :
#1) Créer une fonction qui retourne la plus grande valeur d’une liste d’entiers
#Exemple : [1, 8, 4, 2] => 8

liste = []
n = int(input("combien voulez vous choisir d'entier pour la liste a analiser? "))
for e in range(0,n):
    print("choisissez votre entier numéro ", e + 1)
    z = int(input())
    liste.append(z)

def plus_grand(liste):
    n = (max(liste))
    return (n)

print("l'entier le plus grand est :",(plus_grand(liste)))

#2) Créer une fonction qui retourne la somme des valeurs d’une liste d’entiers
#Exemple : [1, 8, 4, 2] => 15

def somme_valeurs(liste):
    s = sum(liste)
    return s

print("la somme de tout les entiers de la liste est :",(somme_valeurs(liste)))

#3) Créer une fonction qui retourne la valeure moyenne d’une liste d’entiers (pour aller plus
#vite vous avez le droit d’utiliser la fonction de la question 2)
#Exemple : [1, 8, 4, 2] => 3.75
def moyenne_valeurs(liste):
    m = sum(liste)/len(liste)
    return m

print("la moyenne de tout les entiers de la liste est :",(moyenne_valeurs(liste)))

#Exercice 5 (secondaire) :
#1) Créer une fonction qui prend en entrée un nombre et qui retourne un booléen True si ce
#nombre est pair (indice : pour vérifier si un nombre est pair on utilise le modulo :
#nbr % 2 == 0)

n = int(input("entrez un nombre :"))

def nombre_pair(n):
    return (n % 2) == 0

print("votre nombre est pair:", nombre_pair(n))


#2) Créer une fonction qui prend en entrée un nombre et qui retourne un booléen True si ce
#nombre est impair (indice : pour vérifier si un nombre est pair on utilise le modulo :
#nbr % 2 == 1)

def nombre_impair(n):
    return (n % 2) == 1

print("votre nombre est impair:", nombre_impair(n))

#3) Vérifier le bon fonctionnement de ces fonctions

#Exercice 6 (secondaire) :
#1) Créer une fonction qui compte le nombre de caractères d’un mot.

n = str(input("entrez un mot :"))

def nb_chara_mot(n):
    long_mot = len(n)
    return long_mot

print("il y a ", nb_chara_mot(n), " charactéres dans votre mot.")

#2) Créer une fonction qui compte le nombre de mots d’une ligne

ph = str(input("entrez une phrase :"))

def nb_chara_phrase(ph):
    long_phrase = len(ph)
    return long_phrase

print("il y a ", nb_chara_phrase(ph), " charactéres dans votre phrase.")

#Exercice 7 (secondaire) :
#1) Créer un programme qui prend en entrée un nombre et qui retourne une liste de nombre
#entier aléatoire dont l’addition vaut le nombre en entrée.

import random
z = int(input("choisissez un nombre: "))
y = z
listenb = []
def is_list_empty(list):
    return list == []


for i in range(0, z):
    if sum(listenb)<z:
        if is_list_empty(listenb):
            n = (random.randint(1, y))
            listenb.append(n)


        else:
            x = y - listenb[-1]
            n = (random.randint(1, x))
            listenb.append(n)
            y = x

print(listenb)
print("la somme des nombres de cette liste est: ", sum(listenb))


#Exercice 8 (secondaire) :
#Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN valide (valide
#signifie qu'elles ne sont pas vides et sont formées exclusivement d'une combinaison arbitraire
#de "a", "t", "g" ou "c").

#Écrire une fonction valide qui renvoie vrai si la saisie est valide, faux sinon.>il faut qu'il n'est que les 4 lettre, et pas de caractére vide ou autre

#Écrire une fonction saisie qui effectue une saisie valide et renvoie la valeur saisie sous forme
#d'une chaîne de caractères.
# >creer un générateur aléatoire de 4 lettre (hashage?)

#Écrire une fonction proportion qui reçoit deux arguments, la chaîne et la séquence et qui
#retourne la proportion de séquence dans la chaîne (c'est-à-dire son nombre d'occurrences).
#Le programme principal appelle la fonction saisie pour la chaîne et pour la séquence et affiche
#en gros tu ecrit une séquence et l'algorythme doit valider le nombre de fois ou la séquence aparait.

#le résultat.
#Exemple d'affichage :
#chaîne : attgcaatggtggtacatg
#séquence : ca
#Il y a 10.53 % de "ca" dans votre chaîne

#J'ai du mal a saisir l'énnoncé de l'exercice et ne voit pas trop comment le faire. Need Help.

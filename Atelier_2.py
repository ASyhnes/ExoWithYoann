'''Exercice 1 (clé) :
=> Partie 1 :
Écrire un programme qui demande de saisir 2 valeurs et qui affiche la plus petite des 2 valeurs.'''

'''=> Partie 2:
Reprendre et modifier le programme pour que celui-ci affiche également le message suivant
lorsque les 2 valeurs sont égales, “Les deux valeurs sont identiques”.'''

X = input("entrez un nombre")
Y = input("entrez un deuxième nombre")

if X > Y :
    print (X, " est plus grand que " ,X)

elif X < Y :
    print (Y, " est plus grand que " ,X)

else:
    print( "les deux nombres sont egaux")


'''Exercice 2 (clé) :
1) Créer une variable qui contient un mot de passe.
2) Demander à l’utilisateur de saisir un mot de passe.
3) Vérifier que le mot de passe correspond au mot de passe de la variable, le cas échéant
afficher “Mot de passe correct” sinon afficher “Mot de passe incorrect”.'''

MotDePasse = "Azerty"

print ("le mot de passe est", MotDePasse)

Z = input("verifications: quel est le mot de passe?")

if Z == MotDePasse:
    print("Ok")

else:
    print ("Mot de passe incorrect")

'''Exercice 3 (clé) :
=> Partie 1 :
Écrire un programme qui demande de saisir un mois de l’année (str) et qui retourne le numéro
du mois correspondant. Si l’élément saisi n’est pas un mois, le programme doit retourner le
message suivant : “Erreur de saisie”'''

Mois = {
            "janvier": 1,
            "février": 2,
            "mars": 3,
            "avril": 4,
            "mai": 5,
            "juin": 6,
            "juillet": 7,
            "aout": 8,
            "septembre": 9,
            "octobre": 10,
            "novembre": 11,
            "décembre": 12,


}



M = input("Rentrez le nom d'un mois (avec les majuscules et les accents")

'''=> Partie 2 :
Modifier le programme afin qu’il fonctionne avec les variables “Décembre” et “décembre” en
utilisant la fonction lower().
Indice : print(“Décembre”.lower()) => décembre)'''
M = M.lower()

if ( M in Mois ) :
    print ("Ok")


else:
    print ("Consigne pas respéctée")

'''Exercice 4 (secondaire) :
Écrire un programme pour vérifier si un nombre est pair ou impair en utilisant if-else.
'''

A = int(input("Rentrez un nombre entier"))
print(type(A))

if A%2 == 0:
    print("le nombre est pair")
else:
    print("le nombre est impaire")

    '''Exercice 5 (secondaire) :
Écrire un programme qui demande de saisir 2 chaînes de caractères et qui affiche la plus
grande des 2 chaînes (celle qui a le plus de caractères).
Indice : Chercher sur internet une fonction qui retourne le nombre de caractères d’un str'''

P = input("Rentrez une chaine de caractères")
Q = input("Rentrez une chaine de caractères")

if len(P)>len(Q):
    print("la plus grande chaine de caractére est", P, len(P))

elif len(Q)>len(P):
    print("la plus grande chaine de caractére est", Q, len(Q))

else:
    print("Les deux chaine de caractères on le même nombre de caractères")

'''Exercice 6 (secondaire) :
Écrire un programme qui demande à l’utilisateur de saisir un caractère. Le programme doit
afficher le message suivant si le caractère est une voyelle : “Le caractère a est une voyelle”, le
message suivant si le caractères est une consonne : “Le caractère b est une consonne”, sinon
le programme doit afficher le message suivant : “Le caractères ne fait pas partie de l’alphabet”.
Le programme doit pouvoir fonctionner à la fois des caractères majuscules et minuscule'''


P = input("Rentrez un caractère")

voyelles = ["a","e","i","o","u"]
consonne = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
semi_consonne = ['y']

if P.lower() in voyelles :
    print('la lettre rentrée est une voyelle')

elif P.lower() in consonne:
    print('la lettre rentrée est une consonne')

elif P.lower() in semi_consonne:
    print("la lettre rentrée est une semi-consonne")

else:
    print("Le caractères ne fait pas partie de l’alphabet")
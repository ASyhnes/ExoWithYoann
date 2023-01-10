'''"si ma liste est vide:"
    "generer un nombre aléatoire compris entre 0 et  ma base"
    "ajouter se nombre a ma liste"

"sinon:"
    "prendre le dernier nombre de la liste et le sousstraire de ma base"
        "si le resultat est positif"
            " recuperer le resultat et en faire ma nouvelle base""
            "generer un nombre aléatoire compris entre 0 et  ma base"
            "ajouter se nombre a ma liste'''

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
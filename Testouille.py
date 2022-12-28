voyelles = ('aeiou')
consonne = ('bcdfghjklmnpqrstvwxz')
semi_consonne = ('y')
P = input("Rentrez un caractère")

if P.lower() in voyelles :
    print('la lettre rentrée est une voyelle')

elif P.lower() in consonne:
    print('la lettre rentrée est une consonne')

elif P.lower() in semi_consonne:
    print("la lettre rentrée est une semi-consonne")

else:
    print("Le caractères ne fait pas partie de l’alphabet")





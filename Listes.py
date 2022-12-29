liste = ['Python', '5', 'py', '4', 'PHP', '8']
# affichage de la liste
print("liste originale : " + str(liste))
#remplacement
res = [elem.replace('4', '5') for elem in liste]
# print result
print("liste apres replacement : " + str(res))
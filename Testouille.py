import random
N = random.sample(range(1, 100), 3)
print(N)


N = random.sample(range((int(input("choisissez le plus petit nombre entier"))), (int(input("choisissez le plus grand nombre entier que vous voulez")))), (int(input("choisissez le nombre d'éléments que vous voulez voir (plus petit que le dernier nombre rentré SVP)"))))
print(N)

'''N = random.sample(range(int(input("choisissez le plus petit nombre entier"))), (int(input("choisissez le plus grand nombre entier que vous voulez"))), (int(input("choisissez le nombre d'éléments que vous voulez voir (plus petit que le dernier nombre rentré SVP"))))
print(N)'''
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
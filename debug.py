def print_multiforce(n, p):
    for i in range(p):
        for j in range(1, (n * 2) + 1, 2):
            print((j * "^").center(n * 2))

n = int(input("Choisissez la hauteur d'un triangle : "))
p = int(input("Choisissez la hauteur de votre multiforce : "))
print_multiforce(n, p)
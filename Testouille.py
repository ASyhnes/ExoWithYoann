def print_multiforce(n,p):
    step = range(1, ((n * 2) + 1)*p, 2)
    base_total = step[-1]
    for sietri in range(1, p+1):
        for size in range(1, (n*2) + 1, 2):
            print((((size * "^").center(n*2))*sietri).center(base_total))


print("choissisez la hauteur d'un triangle")
n = int(input())
print("choisissez la hauteur de votre multiforce")
p = int(input())

print_multiforce(n, p)
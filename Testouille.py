def print_multiforce(n,p):
    step = range(1, ((n * 2) + 1)*p, 2)
    base_total = step[-1]                   #<=permet d'indexer la valeur de la largeur total du triforce
    for sietri in range(1, p+1):            #<+defini la hauteur du triforce
        for size in range(1, (n*2) + 1, 2):                    #<=defini la hauteur d'un triangle seul
            print((((size * "^").center(n*2))*sietri).center(base_total))        #<=permet de centrer chaque ligne
                                                                                    # du triforce


n = int(input("Choisissez la hauteur d'un triangle : "))
p = int(input("Choisissez la hauteur de votre multiforce : "))

print_multiforce(n, p)
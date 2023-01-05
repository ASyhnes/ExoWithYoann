

'''for i in range(1,3):
    for size in range(1, (n * 2) + 1, 2):
        print((((size * "^").center(n*2))*(i)).center((total_width)))'''


def print_triangle(base):
    for l in range(1,3):
        space = ((base * 2) - 1)
        for i in range(1, (base*2) + 1, 2):
            x = ((space * '.'), ('*' * i), (space  * "."))
            print( x * l)
            space -= 1



print("Choisissez la taille de votre Triangle :")
base = 6
print_triangle(base)
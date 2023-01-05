h = int(input("choissisez une hauteur de sapin"))
e = " "
t = "^"


for i in range(h):
    print(e*h,t*i)
    h -= 1


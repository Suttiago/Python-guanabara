import math

n1 = int(input("Qual o cateto adjascente desse triangulo?"))
n2 = int(input("E o oposto?"))

n3= math.hypot(n1*n2 + n1*n2)

print("A hipotenusa da soma do cateto adjascente {}, e do oposto {}, é {}".format(n1,n2,n3))
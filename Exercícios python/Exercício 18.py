import math

n1 = float(input("Que Ângulo é esse?"))
n2 = math.sin(math.radians(n1))
n3 = math.cos(n1)
n4 = math.tan(n1)



print("O seno dele é {:.2f}, o cosseno dele é {:.2f}, e a tangente {:.2f}".format(n2,n3,n4  ))
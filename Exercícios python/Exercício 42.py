r1 = float(input("Primeiro segmento:"))
r2 = float(input("Segundo segmento:"))
r3 = float(input("Terceiro segmento:"))

if r1< r2 + r3 and r2< r1 +r3 and r3< r1 + r2:
    print("Os segmentos formam um triangulo")
    if r1 == r2 ==r3:
       print("Triangulo equilátero")
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print("Triangulo isósceles")
    elif r1 != r2 != r3:
        print("Triangulo escaleno")
else:
    print("Os segmentos não formam um triangulo")

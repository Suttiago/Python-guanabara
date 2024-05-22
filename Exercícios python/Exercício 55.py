maior = 0
menor = 0

for kg in range(1,6):
    peso = float(input("O peso da {}° pessoa ".format(kg)))
    if kg == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print("O maior peso lido foi {}kg".format(maior))
print("o menor peso liquido foi de {}kg".format(menor))
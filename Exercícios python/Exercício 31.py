dist = float(input("Qual a distância da sua viagem?"))
print("Você está prestes a começar a sua viagem de {}km".format(dist))

curta = dist*0.50
longa = dist*0.45

if dist <= 200:
    print("O preço da sua passagem será de ${}".format(curta))
else:
    print("o preço da sua passagem será {}".format(longa))
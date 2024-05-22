dias = int(input("Por quantos dias voce alugou esse carro?"))
km = int(input("Quantos quilometros voce percorreu?"))

s = (dias*60) + (km*0.15)
print("O valor do seu aluguel do carro foi {}R$".format(s))

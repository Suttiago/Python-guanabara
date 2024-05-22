vel = int(input("Qual a velocidade atual do carro?"))
multa = (vel-80)*7
if vel <= 80:
    print("Tenha um bom dia e dirija com segurança")
else:
    print("VOCÊ FOI MULTADO! Você excedeu o limite de 80km por hora e deverá pagar uma multa de {} reais".format(multa) )

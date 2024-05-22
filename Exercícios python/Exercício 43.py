peso = float(input("Qual seu peso?(kg): "))
altura = float(input("Qual a sua altura?(m): "))
imc=   peso/altura**2

print("O imc da pessoa é {:.2f}".format(imc))
if imc <= 18.5:
    print("Você está abaixo do peso, cuidado!!")
elif 18.5 < imc <=25:
    print("Você está no peso ideal, continue assim!!")
elif 25< imc <= 30:
    print("Sobrepeso, cuidado!!")
elif 30 < imc <= 40:
    print("Obesidade, cuidado!!")
elif 40 < imc:
    print("OBESIDADE MÓRBIDA, tome muito cuidado!!")
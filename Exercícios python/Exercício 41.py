from datetime import date

atual = date.today().year
nasc = int(input("Ano de nascimento:"))
idade = atual - nasc

if idade <= 9:
    print("O atleta tem {} anos".format(idade))
    print("Classificação: junior")
elif 9< idade <= 14:
    print("O atleta tem {} anos".format(idade))
    print("Classificação: infantil")
elif 14 < idade <= 19:
    print("O atleta tem {} anos".format(idade))
    print("Classificação:Júnior")
elif 19 < idade <= 25:
    print("O atleta tem {} anos".format(idade))
    print("Classifficação: Sênior")
else 25<= idade:
    print("O atleta tem {} anos".format(idade))
    print("Classificação: Master")
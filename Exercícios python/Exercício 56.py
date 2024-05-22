média = 0
soma = 0
velho = 0
totalm = 0
nomevel = " "
for p in range(1,5):
    print( "----- {}° pessoa -----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int (input("Idade: "))
    sexo = str(input("SEXO [M/F]: ")).strip()
    soma += idade
    if p == 1 and sexo in "M,m":
        velho = idade
        nomevel = nome
    if sexo in "M,m" and idade > velho:
        velho == idade
        nomevel == nome
    if sexo in "Ff" and idade< 20:
        totalm += 1




média = soma/4

print("O nome do homem mais velho é {} e a idade é {}".format(velho,nomevel))
print("A média soma das idades é {} e a média entre elas é {}".format(soma, média))
print("O número de mulheres com menos de 20 anos é {}".format(totalm))
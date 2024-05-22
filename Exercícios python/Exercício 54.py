from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pes in range (1,8):
    nasc= int(input("Em que ano a {} pessoa nasceu: ".format(pes)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("Ao todo tivemos {} pessoas maiores de idade \n e {} menores de idade".format(maior,menor))

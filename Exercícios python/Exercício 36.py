casa = float(input("Valor da casa:"))
sal = float(input("Salário do comprador:"))
fin = int(input("Quantos anos para o financiamento:"))
prestação = casa / (fin * 12)
mei = (sal*30)/100

if mei >= prestação:
   resul = print("EMPÉSTIMO ACEITO!!")
elif mei <prestação:
   resul = print("EMPRÉSTIMO NEGADO!!")

print("Para pagar a casa de {} em {} anos a prestação será de {} por Mês".format(casa,fin,prestação))
print(resul)


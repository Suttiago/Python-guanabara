preço = float(input("Preço das compras: R$"))

print("""Formas de pagamento:
(1) À vista dinheiro/cheque
(2) À vista cartão
(3) 2X no cartão        
(4) 3x no cartão""")
forma = int(input("Qual opção?"))

if forma == 1:
    total = preço - (preço* 10 / 100)
elif forma == 2:
    total = preço - (preço* 5 / 100)
elif forma == 3:
    total = preço
    parcela = total / 2 
    print("Sua compra será parcelada em 2x de R${}".format(parcela))
elif forma == 4:
    total = preço + (preço * 20 / 100)
    total_parc = int(input("Quantas parcelas?"))
    parcela = total / total_parc
    print("Sua compra será parcelada em {} de R${} com juros".format(total_parc, parcela))
else:
    total = 0
    print("Opção invalida")
print("A sua compra de R${} vai custar R${} no final".format(preço,total))
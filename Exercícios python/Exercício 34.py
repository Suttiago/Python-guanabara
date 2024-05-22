sal = float(input("Qual o salário do funcionário?"))

if 1250.00 < sal:
    aument = ((sal*10)/100)+ sal

else:
    aument = ((sal*15)/100) + sal

print("O salário que antes era {}, passa a ser {}".format(sal, aument))
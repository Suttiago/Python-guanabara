num = int(input("Digite um número: "))
tot = 0
for c in range (1,num+1):
    if num % c == 0:
        print("\033[34m", end= " ")
        tot += 1
    else:
        print("\033[m", end=" ")
    print("{}".format(c))
print("O número {} foi divisível {} vezes".format(num,tot))
if tot == 2:
    print("É primo")
else:
    print("Não é primo")
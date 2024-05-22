num =int (input("Digite um número inteiro:"))
print("""Escolha uma opção:
"(1) converter para binário
 (2) converter para octal
 (3) converter para hexadecimal""")

opção = int (input("Sua opção"))

if opção == 1:
 print  ("o número {} convertido em binário é {}".format(num, bin(num)))
elif opção == 2:
 print  ("o número {} convertido em octal é {}".format(num, oct(num)))
elif opção == 3:
 print  ("o número {} convertido em hexadecimal é {}".format(num, hex(num)))
else:
 print("Opção inválida") 
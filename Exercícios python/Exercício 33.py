a = int(input("Primeiro valor:"))
b = int(input("Segundo valor:"))
c = int(input("Terceiro valor:"))

if a<c and a<b:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print("O menor valor foi {}".format(menor))

if a>c and a>b:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("O maior valor foi {}".format(maior))
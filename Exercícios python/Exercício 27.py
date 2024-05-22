nome = str(input("Qual o seu nome completo?")).strip().split()

print("Prazer em te conhecer")
print("O seu primeiro nome é: {}".format(nome[0]))
print("Seu ultimo nome é {}".format(nome[len(nome)-1]))  
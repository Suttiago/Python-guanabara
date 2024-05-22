import random


a1 = str(input("Qual o nome desse aluno?"))
a2 = str(input("E desse?"))
a3 = str(input("Esse aqui?"))
a4 = str(input("Mais esse"))
sorteio =  [a1, a2, a3, a4]
random.shuffle(sorteio)

print("Os alunos escolhidos em ordem são {} ".format(sorteio))

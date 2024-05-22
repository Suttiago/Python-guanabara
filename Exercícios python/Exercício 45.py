from random import randint
from time import sleep
itens  = ("Pedra" , "Papel" , "Tesoura")
computador = randint(0, 2) 
print(""" Suas opções:
 [0] Pedra 
 [1] Papel    
 [2] Tesoura""")
escolha = int(input("Qual sua jogada"))


print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)

print( "-=-"*10)
print("Você jogou {}".format(itens[escolha]))
print("O computador jogou {}".format(itens[computador]))
print( "-=-"*10)



if computador == 0:
    if escolha == 0:
      print("EMPATE!!")
    elif escolha == 1:
       print("Você ganhou o computador é burro")
    elif escolha ==2:
       print("Você perdeu, lerdão")
    else: 
       print("Jogada inválida")

if computador == 1:
    if escolha == 0:
        print("Você perdeu, lerdão")
    elif escolha == 1:
        print("EMPATE!!")
    elif escolha == 2:
        print("Você ganhou o computador é burro")
    else:
       print("Jogada inválida")

if computador == 2:
    if escolha == 0:
        print("Você perdeu, lerdão")
    elif escolha == 1:
        print("Você ganhou, o computador é burro")
    elif escolha == 2:
        print("EMPATE!!")
    else:
       print("Jogada inválida")




      
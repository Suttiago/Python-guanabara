from random import randint
pc = randint( 0,5  )

print("Vou pensar em um número entre 0 e 5, tente adivinhar")
vc = int(input("Em que número pensei?"))

if pc==vc:
    print("Parabéns, você ganhou o jogo")
else:
    print("Errou, o numero que pensei foi {} e não {}".format(pc,vc))
num1 = float(input("Primeira nota:"))
num2 = float(input("Segunda nota:"))
med =  (num1 + num2)/2

if med < 5.0:
    print("O aluno com as notas {} e {} atingiu a média {}, REPROVADO!!".format(num1,num2,med))
elif  5.0 < med < 6.9:
    print("O aluno com as notas {} e {} atingiu a média {}, RECUPERAÇÃO!!".format(num1,num2,med))
elif 7.0 < med:
    print("O aluno com as notas {} e {} atingiu a média {}, APROVADO!!".format(num1,num2,med))



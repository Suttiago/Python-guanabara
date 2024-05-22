from datetime import date

atual = date.today().year
nasc = int(input("Em que ano você nasceu?"))
idade = atual - nasc

if idade < 18:
    print("Quem nasceu no ano de {} tem {} anos, por isso não pode se alistar".format(nasc,idade))
elif idade == 18:
    print("Quem nasceu no ano de {} e tem {} anos pode se alistar".format(nasc, idade))
elif idade > 18:
    print("Quem nasceu no ano de {} e tem {} anos por isso não pode se alistar".format(nasc, idade))


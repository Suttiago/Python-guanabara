Nome = str(input("Qual o seu nome?")).strip() 

print("O seu nome em maiúsculas é {}".format(Nome.upper())) 
print("O seu nome em minúsculas é {}".format(Nome.lower()))
print("O seu tem ao todo {} letras".format(len(Nome) - Nome.count(' '))) 
print("O seu primeiro nome tem {} letras ".format(Nome.find(" ")) ) 



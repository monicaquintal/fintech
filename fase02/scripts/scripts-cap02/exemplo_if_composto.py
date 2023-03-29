rm = input("Insira seu RM: ")
idade = input("Digite sua idade: ")
nome = input("Digite seu nome: ")

if int(idade) >= 18:
    print("{}, sua participação foi autorizada, seu RM é {}.".format(nome, rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    print("{}, sua participação não foi autorizada devido à sua idade.".format(nome))
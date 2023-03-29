rm = input("Insira seu RM: ")
nome = input("Digite seu nome: ")
idade = input("Insira sua idade: ")

if int(idade) >= 18:
    print("{}, sua participação foi autorizada, seu RM é {}!".format(nome, rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado.")
else:
    autorizado = input("Você possui autorização dos responsáveis? S-SIM ou N-NÃO: ")
    if autorizado == 'S':
        print("{}, sua participação foi autorizada, aluno de RM {}!".format(nome, rm))
        print("Mais informações serão enviadas para o email dos responsáveis.")
    else:
        print("Sua participação não foi autorizada devido à sua idade.")
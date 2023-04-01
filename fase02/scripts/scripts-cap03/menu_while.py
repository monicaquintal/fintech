# variável que servirá para receber a opção do usuário
op = 0

# enquanto o usuário não digitar a opção de saída
while op != 4:
    # exibição das opções do menu
    print("SUPER PROGRAMA MARAVILHOSO")
    print("1 - Rodar código 1")
    print("2 - Rodar código 2")
    print("3 - Rodar código 3")
    print("4 - Sair do programa")
    op = int(input("Informe sua opção: "))

    # verificação das opções disponíveis
    if op == 1:
        # O que ocorrerá se a opção 1 for selecionada
        print("CÓDIGO 1 RODANDO!")
    elif op == 2:
        # O que ocorrerá se a opção 2 for selecionada
        print("CÓDIGO 2 RODANDO!")
    elif op == 3:
        # O que ocorrerá se a opção 3 for selecionada
        print("CÓDIGO 3 RODANDO!")

# Quando o looping terminar de rodar, exibir essa mensagem
print("OK! O programa está encerrado...")
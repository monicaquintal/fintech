#criando um dicionário vazio
dicionario = {}

#incluindo dados no dicionário
dicionario["André David"] = "Professor"

#Pedindo para o usuário incluir dados no dicionário
nova_chave = input("Informe o nome do colaborador da FIAP: ")
novo_valor = input("Informe a função do colaborador da FIAP: ")

dicionario[nova_chave] = novo_valor

#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O  colaborador  {}  desempenha  a  função  de {}".format(chave, valor))
print("---")

#alterando dados no dicionário
dicionario["André David"] = "Coordenador"

#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O  colaborador  {}  desempenha  a  função  de {}".format(chave, valor))
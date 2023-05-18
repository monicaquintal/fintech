#criando um dicionário com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}

#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}.".format(chave, valor))
print("---")

#removendo o item cuja chave é R2-D2
dicionario.pop("R2-D2")

#exibindo o dicionário completo após a remoção
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}.".format(chave, valor))
print("---")

#removendo o último item
dicionario.popitem()

#exibindo o dicionário completo após a remoção
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
print("---")

#removendo todos os itens do dicionário
dicionario.clear()

#exibindo o dicionário completo após a remoção
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
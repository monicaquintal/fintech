#criando um dicionário vazio
dicionario_vazio = {}

#exibindo o tipo do dicionário
print("O objeto dicionario_vazio é do tipo {}!".format(type(dicionario_vazio)))
print("Seu conteúdo é: {}.".format(dicionario_vazio))
print("---")

#criando um dicionário com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
print(dicionario)
print("---")
print(dicionario["R2-D2"])
print("---")

#exibindo todos os valores em um dicionário
for valor in dicionario.values():
    print(valor)
print("---")

#exibindo todas as chaves em um dicionário
for chave in dicionario.keys():
    print(chave)
print("---")

#exibindo o dicionário completo
for chave, valor in dicionario.items():
  print("O personagem {} é da categoria {}.".format(chave, valor))
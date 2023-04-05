# Criando uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

# Exibindo a lista com um print
print(jedi)
print("--------------------------------------")

# Exibindo um valor específico da lista
print(jedi[2])
print("--------------------------------------")

# Incluindo um valor no final da lista
jedi.append("Mace Windu")

# Incluindo um valor em uma posição específica da lista
jedi.insert(2, "Luminara")

# Exibindo a lista completa
# A variável assumirá cada um dos valores da lista
for nome in jedi:
    # Para cada volta do loop, exibir o valor assumido
    print(nome)

print("--------------------------------------")
#Removendo o último valor inserido na lista
jedi.pop()
print(jedi)

print("--------------------------------------")
# Removendo um item em posição específica
jedi.pop(2)
print(jedi)

print("--------------------------------------")
# Removendo um valor específico da lista
jedi.remove("Yoda")
print(jedi)
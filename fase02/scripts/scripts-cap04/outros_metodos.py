# Valores fora de ordem:
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]

# Exibição da lista:
print("A lista foi criada assim: {}.".format(valores))

# Realizando a contagem de elementos:
contagem = valores.count(7)
print("Nessa lista o número 7 aparece {} vezes.".format(contagem))

# Invertendo a lista
valores.reverse()
print("A lista agora está invertida: {}.".format(valores))

# Ordenando a lista
valores.sort()
print("A lista agora está ordenada: {}.".format(valores))

# Tamanho da lista

tamanho = len(valores)
print("A lista tem {} elementos.".format(tamanho))

# Soma dos elementos
soma = sum(valores)
print("A soma dos elementos é {}.".format(soma))
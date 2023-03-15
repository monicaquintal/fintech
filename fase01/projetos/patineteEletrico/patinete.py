print("Este programa calcula a velocidade média de um patinete elético!")

distancia = input("Informe a distância percorrida pelo patinete (em metros): ")
tempo = input("Quantos minutos demorou para percorrer essa distância? ")

velocidade_media = float(distancia) / float(tempo)

# print("O patinete atingiu uma velocidade média de {} m/min".format(velocidade_media))

# para limitar a quantidade de casas decimais da variável velocidade_media:
# para exibir 2 casas, indicar {0:.2f}, para exibir 1 casa {0:.1f}, etc

print("O patinete atingiu uma velocidade de {0:.2f} m/min".format(velocidade_media))

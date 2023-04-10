# Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):

    # calcular a velocidade média
    velocidade_media = distancia/tempo
    # exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))

# Aqui começa o programa principal
distancia = float(input("Digite a distância percorrida (em quilômetros): "))
tempo = float(input("Digite o tempo da viagem (em horas): "))

# Chamando a função com valores definidos pelo usuario
calcularVelocidadeMedia(distancia, tempo)

# Caso queira chamar a função com valores definidos pelo programador
# calcularVelocidadeMedia(15,2)

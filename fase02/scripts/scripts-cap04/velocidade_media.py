# Função que calcula a velocidade média

def calcularVelocidadeMedia():
    # solicitar distância e tempo
    distancia = float(input("Digite a distância percorrida"))
    tempo = float(input("Digite o tempo da viagem"))
    # calcular a velocidade média
    velocidade_media = distancia/tempo
    #e xibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))

# Aqui começa o programa principal
calcularVelocidadeMedia()
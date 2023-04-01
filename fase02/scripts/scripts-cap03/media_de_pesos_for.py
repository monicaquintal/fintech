# Variavel para armazenar o peso total das caixas
peso_total = 0.0

# Loop para repetir por 10 vezes a solicitação de peso
for x in range(1,11):
    # Para cada volta do loop, solicitar o peso da caixa
    peso_atual = float(input("Informe o peso da caixa atual: "))
    # Para cada peso solicitado, somar ao peso total
    peso_total = peso_total + peso_atual

# Ao final do loop, calcular a média aritmética
media = peso_total/10

# Exibição dos resultados!
print("O peso total de caixas é {}. "
      "A média de peso é {}".format(peso_total, media))
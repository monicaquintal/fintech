# Criar um algoritmo que receba:
# - tipo de assinatura do cliente
# - faturamento anual dele
# - e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.

# Tabela de porcentagem de acordo com cada nível de assinatura:
# Nível | Porcentagem sobre o faturamento
# Basic | 30%
# Silver | 20%
# Gold | 10%
# Platinum | 5%

tipo_assinatura = input("Informe o seu tipo de assinatura: ")

if tipo_assinatura.upper() == "BASIC":
    faturamento_anual = float(input("Informe o seu faturamento anual: "))
    bonus_a_ser_pago = faturamento_anual * 0.3
    print("O valor do bônus a ser pago será de R${}.".format(bonus_a_ser_pago))
elif tipo_assinatura.upper() == "SILVER":
    faturamento_anual = float(input("Informe o seu faturamento anual: "))
    bonus_a_ser_pago = faturamento_anual * 0.2
    print("O valor do bônus a ser pago será de R${}.".format(bonus_a_ser_pago))
elif tipo_assinatura.upper() == "GOLD":
    faturamento_anual = float(input("Informe o seu faturamento anual: "))
    bonus_a_ser_pago = faturamento_anual * 0.1
    print("O valor do bônus a ser pago será de R${}.".format(bonus_a_ser_pago))
elif tipo_assinatura.upper() == "PLATINUM":
    faturamento_anual = float(input("Informe o seu faturamento anual: "))
    bonus_a_ser_pago = faturamento_anual * 0.05
    print("O valor do bônus a ser pago será de R${}.".format(bonus_a_ser_pago))
else:
    print("Por favor, informe um tipo de assinatura válido.")

# Optei por incluir a variável faturamento_anual dentro da estrutura if-composto,
# com objetivo de que o usuário informe seu faturamento apenas em caso de incluir
# um tipo de assinatura válido no primeiro input.
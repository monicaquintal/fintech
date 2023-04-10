# Definindo a função que coma dois valores
def somar(a, b):
    soma = a + b
    return(soma)


# Fora da função:
valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))

print("A soma dos valores é igual a {}.".format(somar(valor1, valor2)))
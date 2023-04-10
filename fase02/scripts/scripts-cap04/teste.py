# Importação do módulo calc.py
import calc

# importação de funções específica do módulo calc.py
# from calc import somar, subtrair

# importação de funções específica do módulo calc.py
# from calc import *

# Solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

# Armazenando a soma
soma = calc.somar(valor1, valor2)

# Exibindo a soma
print("A soma é {}".format(soma))
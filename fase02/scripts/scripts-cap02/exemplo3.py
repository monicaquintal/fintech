# Importando a classe math:
import math

# Solicitando os valores de A, B e C
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

# Cálculo do delta
delta = b * b - (4 * a * c)

# Verificação das condições com elif:
if delta > 0.0:
    # cálculo de 2 valores para x
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos as eguintes raízes: x1 = {} e x2 = {}.".format(a,b,c,x1,x2))

elif delta == 0:
    # cálculo de 1 valor para x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {}.".format(a,b,c,x))
else:
    # exibição da mensagem
    print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x.".format(a, b, c))
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario < 0:
    salario = salario * -1
    print("O salário informado é negativo.")

print ("O salário do funcionário {} é {}.".format(nome, salario))
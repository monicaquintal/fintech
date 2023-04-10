import funcoes_calculadora

# Fora da função
op = -1

while op!= 5:
    print("1 - Somar dois valores.")
    print("2 - Subtrair dois valores.")
    print("3 - Multiplicar dois valores.")
    print("4 - Dividir dois valores.")
    print("5 - Sair.")
    op = int(input("Digite a opção desejada: "))
    if(op == 1):
        print(funcoes_calculadora.somar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif(op==2):
        print(funcoes_calculadora.subtrair(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif(op==3):
        print(funcoes_calculadora.multiplicar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif(op==4):
        print(funcoes_calculadora.dividir(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    print("---------------------------")
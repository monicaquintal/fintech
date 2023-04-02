# Ao analisar o código do programa, você descobre que a senha é composta pela palavra
# “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento
# da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120).
# Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária
# para desbloqueio.

minutos = int(input("Informe os minutos atuais: "))
fatorial = 1
contador = 1

while contador <= minutos:
    fatorial *= contador
    contador += 1

print("A senha para desbloqueio é: LIBERDADE{}.".format(fatorial))


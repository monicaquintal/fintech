# Os alunos da sua turma fizeram uma votação para escolher o dia da semana para realização das lives.
# Desenvolva um programa em que :
# - o usuário informe a quantidade de votos que cada um dos 5 dias da semana (2ªa 6ª) obtiveram
# - verifique e exiba qual dia foi o escolhido.

quantidade_alunos = int(input("Por favor, informe a quantidade de alunos da turma: "))
segunda_feira = 0
terca_feira = 0
quarta_feira = 0
quinta_feira = 0
sexta_feira = 0

for votos in range (1, quantidade_alunos + 1, 1):
    dia_favorito = int(input("Aluno {}, \ninforme o seu dia da semana preferido para assistir às lives, sendo: \n"
                         "1 - segunda; \n2 - terça; \n3 - quarta; \n4 - quinta; \n5 - sexta. ".format(votos)))
    if dia_favorito == 1:
        segunda_feira = segunda_feira + 1
    elif dia_favorito == 2:
        terca_feira = terca_feira + 1
    elif dia_favorito == 3:
        quarta_feira = quarta_feira + 1
    elif dia_favorito == 4:
        quinta_feira = quinta_feira + 1
    elif dia_favorito == 5:
        sexta_feira = sexta_feira + 1

print("----------------------------------------------------")

if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
    print("O dia escolhido para a realização das lives foi a segunda-feira!")
elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira:
    print("O dia escolhido para a realização das lives foi a terça-feira!")
elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira:
    print("O dia escolhido para a realização das lives foi a quarta-feira!")
elif quinta_feira > segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira:
    print("O dia escolhido para a realização das lives foi a quinta-feira!")
elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira:
    print("O dia escolhido para a realização das lives foi a sexta-feira!")
else:
    print("Houve um empate!")


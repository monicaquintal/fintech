# turmas compostas por 50 alunos.
# criar um sistema capaz de atender ao seguinte requisito:
# - o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49)
# - e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50).
# - o sistema deve calcular e exibir a média de cada uma das metades da sala e
# - informar, ao final, qual delas teve a maior nota.
# pedido especial do mantenedor: ao digitar cada uma das notas, deve ser exibida uma mensagem no seguinte padrão:
# "VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso)."
# "POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x."

nota_total_impar = 0
nota_total_par = 0

for turma_impar in range(1,50,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    nota_impar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(turma_impar)))
    nota_total_impar = nota_total_impar + nota_impar

print("----------------------------------------------------")

for turma_par in range(2,51,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    nota_par = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(turma_par)))
    nota_total_par = nota_total_par + nota_par

print("----------------------------------------------------")

media_turma_impar = nota_total_impar/25
print("A MÉDIA DA TURMA ÍMPAR FOI IGUAL A {}.".format(media_turma_impar))
media_turma_par = nota_total_par/25
print("A MÉDIA DA TURMA PAR FOI IGUAL A {}.".format(media_turma_par))

if media_turma_impar > media_turma_par:
    print("A TURMA ÍMPAR OBTEVE A MAIOR NOTA.")
elif media_turma_par > media_turma_impar:
    print("A TURMA PAR OBTEVE A MAIOR NOTA.")
else:
    print("HOUVE UM EMPATE!")
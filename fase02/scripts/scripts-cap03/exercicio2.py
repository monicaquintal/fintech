quantidade_transacoes = int(input("Informe a quantidade de transações realizadas: "))
total_transacoes = 0

for n_transacoes in range(1, quantidade_transacoes + 1, 1):
    valor_transacao = float(input("Informe o valor da transação de número {}: ".format(n_transacoes)))
    total_transacoes = total_transacoes + valor_transacao

media = total_transacoes / quantidade_transacoes
print("Neste dia, foi gasto um total de R${}, com uma média de R${} por transação.".format(total_transacoes, media))
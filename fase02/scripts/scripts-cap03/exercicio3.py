# solicitar ao usuário que digite um número
numero_usuario = int(input("Por favor, informe um número inteiro: "))

# representam os 2 valores anteriores, a serem somados na lógica
anterior1 = 1
anterior2 = 0

for n_elemento in range(1, numero_usuario + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual

    if numero_usuario == atual:
        print("Ação bem-sucedida! :)")
        break
    elif numero_usuario < atual:
        print("Ação falhou... :(")
        break
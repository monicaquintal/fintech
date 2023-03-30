print("VERIFICADOR DE FREQUÊNCIA CARDÍACA")

idade = int(input("Digite sua idade: "))
bpm = int(input("Informe a sua frequência cardíaca: "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequência cardíaca adequada! :)")
    else:
        print("Frequência cardíaca inadequada... :(")

elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequência cardíaca adequada! :)")
    else:
        print("Frequência cardíaca inadequada... :(")

elif idade >= 18 and idade < 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequência cardíaca adequada! :)")
    else:
        print("Frequência cardíaca inadequada... :(")

elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Frequência cardíaca adequada! :)")
    else:
        print("Frequência cardíaca inadequada... :(")

else:
    print("Não existem dados para a idade indicada.")
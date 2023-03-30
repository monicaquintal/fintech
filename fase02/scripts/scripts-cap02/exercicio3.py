voto1 = input("Colaborador 1, informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ")
voto2 = input("Colaborador 2, informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ")
voto3 = input("Colaborador 3, informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ")
voto4 = input("Colaborador 4, informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ")
voto5 = input("Colaborador 5, informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 1 digitou um console inexistente, e seu voto será desconsiderado.")

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 2 digitou um console inexistente, e seu voto será desconsiderado.")

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 3 digitou um console inexistente, e seu voto será desconsiderado.")

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 4 digitou um console inexistente, e seu voto será desconsiderado.")

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 5 digitou um console inexistente, e seu voto será desconsiderado.")

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi o Playstation!")
elif xbox > nintendo and xbox > playstation:
    print("O console escolhido foi o Xbox!")
elif nintendo > xbox and nintendo > playstation:
    print("O console escolhido foi o Nintendo!")
else:
    print("Houve um empate, favor entrar em contato com a direção!")
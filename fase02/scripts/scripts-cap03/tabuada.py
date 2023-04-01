n = int(input("Qual tabuada você gostaria de conferir?"))
i = 1

while i <= 10:
    print("{} x {} = {}".format(n, i, i * n))
    i = i + 1
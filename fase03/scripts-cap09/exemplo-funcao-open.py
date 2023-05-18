#usando a função open para abrir um objeto do tipo arquivo já existente
arquivo = open("C:\\Users\\monic\\OneDrive\\Cursos\\FIAP\\fintech\\fase03\\scripts-cap09\\arquivo.txt")

#printando o conteúdo do objeto arquivo
print(arquivo.read())
print("---")

#printando uma linha do arquivo
print(arquivo.readline())
print(arquivo.readline())
print("---")

#Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)
print("---")

""""""""""""""""""""""""""""""""

#Passando o conteúdo do arquivo para uma lista
linhas_do_arquivo = arquivo.readlines()

#comprovando o tipo do objeto linhas_do_arquivo
print("Ei! Eu consegui transformar meu arquivo em uma {}!".format(type(linhas_do_arquivo)))

#colocando a lista em ordem alfabética
linhas_do_arquivo.sort()

#Exibindo nossa lista, agora em ordem alfabética4
print(linhas_do_arquivo)

#verificando o tipo do objeto arquivo
print(type(arquivo))

#fechamento do arquivo
arquivo.close()
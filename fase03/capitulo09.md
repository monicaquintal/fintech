<div id="fase03" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 09: Quem arquiva amigo é. 🗃️</h2>
</div>

<div align="center">
<h2>1. QUEM ARQUIVA AMIGO É</h2>
</div>

## 1.1 Saindo do temporário

- quando os scripts são encerrados, os dados preenchidos nas estruturas são perdidos (se encontram na memória RAM).
- o Python será um aliado na manipulação de arquivos e na escrita no formato JSON.

## 1.2 Arquivos? Que tipo de arquivos?

- o computador representa tudo por meio de bits (0 e 1) que, quando aglomeramos, formam bytes. Uma letra do alfabeto pode ser representada por meio de 1 byte (8 bits) no sistema ASCII.
- o que as linguagens de programação permitem é gravar bytes.

### 1.2.1 A `função open`

- função nativa do Python.
- retorna para dentro do script um objeto do tipo arquivo.
  - pode ser um arquivo já existente ou um novo arquivo que estamos criando.
- podemos printar seu conteúdo através da `função read`.
- também podemos analisar o arquivo linha a linha, através do `método readline()`.
- podemos criar um loop que passe por todas as linhas; o `método readlines()` faz a leitura de todas as linhas de um arquivo e retorna uma lista das linhas, separando-as umas das outras com vírgulas.
- lembrar de fechar o arquivo que foi aberto.
  - se não fizermos, e o arquivo continuar aberto enquanto o script roda, poderão ocorrer falhas que levarão os dados a serem corrompidos.
  - para realizar o fechamento, utilizar o `método close()`.
- se passar o parâmetro `encoding="UTF-8"` na função open, o Python interpretará que o arquivo está nessa codificação.

> exemplos em [exemplo-funcao-open.py](./scripts-cap09/exemplo-funcao-open.py). 

### 1.2.2 Usando a função open para... salvar?

- ao utilizar a função open, além do caminho do arquivo, podemos e devemos indicar a forma como esse arquivo será manipulado pelo nosso script:
  - indicar um segundo parâmetro, após o local do arquivo, e ele pode assumir os seguintes valores:

<div align="center">

Valor | Significado
------|-------------
r | abrir a leitura (modo padrão).
w | abrir a escrita, sobrescrevendo o conteúdo.
x | abrir para a criação de arquivo, gerando uma falha se existir um arquivo de mesmo nome.
a | abrindo para escrita, anexando o novo conteúdo ao final do conteúdo já existente no arquivo.
b | abrir em modo binário.
t | abrir em modo de texto (modo padrão).
&#43; | abrir para atualização (escrita e leitura). 

</div>

- por padrão, a função open() abre qualquer arquivo no modo r, que significa read. Para alterar esse modo, fazemos como no exemplo abaixo:

~~~python
# criando um novo arquivo:
arquivo = open("c:\\arquivos\\novo_arquivo.txt", "w", encoding="UTF-8")
~~~

- se mudarmos a forma de abertura do arquivo, de w(que cria e substitui o conteúdo antigo) para a (que cria um arquivo e anexa o novo conteúdo no final), a cada execução do script o novo conteúdo será anexado ao final do conteúdo antigo.

### 1.2.3 Descrições dos principais métodos que podemos utilizar com arquivos no Python

<div align="center">

Método | Descrição | Exemplo
-------|-----------|-------
close() | Fecha o arquivo. | arquivo.close()
flush() | Libera o buffer interno. | arquivo.flush()
read() | Faz a leitura do arquivo inteiro e retorna uma string. | arquivo.read()
readline() | Faz a leitura e retorna uma linha de um arquivo. | arquivo.readline()
readlines() | Faz a leitura do arquivo inteiro e retorna uma lista com cada linha. | arquivo.readlines()
seek() | Permite controlar a posição do cursor no arquivo. | arquivo.seek(coluna, posição)
tell() | Retorna a posição atual do cursor no arquivo. | arquivo.tell()
truncate() | Redimensiona (trunca) o arquivo para o tamanho especificado. | arquivo.truncate(tamanho)
writable() | Retorna o valor True se pudermos escrever no arquivo. | arquivo.writable()
write() | Grava no arquivo. | arquivo.write(string)
writelines() | Grava cada elemento de uma lista de strings no arquivo. | arquivo.writelines(lista_string)

</div>

## 1.3 O formato JSON

- padrão legível criado para trocar dados entre aplicações e computadores, baseado no ormato atributo-valor. Exemplo:

~~~json
{
  "Clark Kent": {
    "Celular":"123456",
    "Email":"super@krypton.com"
  },
  "Bruce Wayne": {
    "Celular":"654321",
    "Email":"bat@caverna.com.br"
  }
 }
~~~

- há vários formatos possíveis para dados no padrão JSON, que podem ser encontrados [aqui](http://json.org/json-pt.html).

### 1.3.1 Dicionário para JSON

- o módulo json (no Python) conta com inúmeros métodos úteis e o primeiro deles é o `método dumps()`, que converte um objeto para o formato json.

> exemplo em [exemplo-json.py](./scripts-cap09/exemplo-json.py). 

- podemos garantir o espaçamento correto dos dados adicionando o parâmetro indent ao método dumps.
- se quiser ter certeza de que o JSON gerado esteja correto, copiar o resultado e utilizar uma das diversas ferramentas on-line disponíveis para isso.

> A página <http://jsonviewer.stack.hu/> permite colar um JSON e visualizar os dados que ele contém.

### 1.3.2 JSON para dicionário

- `método loads` converte uma string em dicionário (converte o conteúdo desse arquivo para um dicionário), de forma que seja possível manipular seus dados dentro do programa.

> exemplo em [exemplo-json.py](./scripts-cap09/exemplo-json.py). 

## 1.4 Um pequeno extra

- o `comando with` é usado para garantir que um recurso que foi aberto seja finalizado.
  - não precisa se preocupar com o close ao final da manipulação de um arquivo.

> O with usará o open para abrir o arquivo indicado, dentro do objeto arquivo, e fará sozinho o encerramento do acesso quando a última linha de código, dentro dele, for executada.

Exemplo:

~~~python
with open("c:\\arquivos\\arquivo_de_texto.txt", "w") as arquivo:
  # aqui devemos escrever todos os códigos que usam o arquivo aberto, 
  # pois após a última linha de código dentro dessa estrutura, o arquivo será automaticamente encerrado
  arquivo.write("May the force be with you")
~~~

---

## FAST TEST

### 1. Escolha a alternativa que apresenta o método para converter um objeto para o formato JSON.
> dumps()

### 2. Qual alternativa apresenta o comando para exibição de todo o conteúdo de um arquivo de texto no Python?
> print(arquivo.read())

### 3. Em relação à manipulação de arquivos no Python, escolha a alternativa que apresemta a funcionalidade do comando with.
> É usado para garantir que um recurso que foi aberto seja finalizado.

### 4. Com base no conteúdo estudado sobre a manipulação de arquivos JSON no Python, selecione a alternativa que apresenta a funcionalidade do método loads().
> Converte uma string em um dicionário.

### 5. Selecione a alternativa que contém o comando no Python para abrir um arquivo para escrita, anexando o novo conteúdo ao final do conteúdo já existente no arquivo.
> arquivo = open("c:\\arquivos\novo_arquivo.txt", "a").

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)
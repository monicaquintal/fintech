<div id="fase03" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 09: Quem arquiva amigo é. 🗃️</h2>
</div>

<div align="center">
<h2>1. QUEM ARQUIVA AMIGO É</h2>
</div>

## 1.1 Saindo do temporário

- quandoos scritps são encerrados, os dados preenchi nas estruturas são perdidos (se encontram na memória RAM).
- neste capítulo vamos, o Python será um aliado na manipulação de arquivos e na escrita no formato JSON.

## 1.2 Arquivos? Que tipo de arquivos?

- o computador representa tudo por meio de bits (0 e 1) que, quando aglomeramos, formam bytes. Uma letra do alfabeto pode ser representada por meio de 1 byte (8 bits) no sistema ASCII.
- o que as linguagens de programação permitem é gravar bytes.

### 1.2.1 A `função open`

- função nativa do Python.
- retorna para dentro do script um objeto do tipo arquivo.
  - pode ser um arquivo já existente ou um novo arquivo que estamos criando.
- podemos printar seu conteúdo atravbés da `fnção read`.
- também podemos analisar o arquivo linha a linha, através do `método readline()`.
- podemos criar um loop que passe por todas as linhas; o método readlines() faz a leitura de todas as linhas de um arquivo e retorna uma lista das linhas, separando-as umas das outras com vírgulas.
- lembrar de fechar o arquivo que foi aberto.
  - se não fizermos, e o arquivo continuar aberto enquanto o script roda, poderão ocorrer falhas que levarão os dados a serem corrompidos.
  - pararealizar o fechamento, utilizar o `método close()`.

> exemplos em [exemplo-funcao-open.py](./scripts-cap09/exemplo-funcao-open.py). 

### 1.2.2 Usando a função open para... salvar?

- ao utilizar a função open, além do caminho do arquivo, podemos e devemos indicar a forma como esse arquivo será manipulado pelo nosso script:
  - indicar um segundo parâmetro, após o local do arquivo, e ele pode assumir os seguintes valores:

Valor | Significado
------|-------------
r | abrir a leitura (modo padrão).
w | abrir a escrita, sobrescrevendo o conteúdo.
x | abrir para a criação de arquivo, gerando uma falha se existir um arquivo de mesmo nome.
a | abrindo para escrita, anexando o novo conteúdo ao final do conteúdo já existente no arquivo.
b | abrir em modo binário.
t | abrir em modo de texto (modo padrão).
+ | abrir para atualização (escrita e leitura). 
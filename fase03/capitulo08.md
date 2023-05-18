<div id="fase03" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 08: Salvo pelo dicionário! 📙</h2>
</div>

<div align="center">
<h2>1. Por que as listas não são o suficiente?</h2>
</div>

> Usando o módulo sys do Python (que é instalado por padrão), podemos verificar o tamanho de qualquer objeto por meio do método getsizeof().

- uma lista, ainda que vazia, ocupa um espaço na memória, conforme script encontrado em:

> pasta fase03 > projects > [exemplo-getsizeof.py](./scripts/exemplo-getsizeof.py).

- incluir, reordenar e remover novos elementos têm um custo que se traduz em espaço em memória RAM.
- neste capítulo, aprenderemos que há outras estruturas mais adequadas do que a lista, cada uma voltada para uma situação específica.

## Trabalho em tupla

- tuplas ou tuples:
  - são estruturas da linguagem Python parecidas com listas, mas com a característica de serem **imutáveis**. 
  - todos os dados que armazenarmos dentro de uma tupla permanecerão idênticos e na mesma posição ao longo de toda a execução do programa.
- `enquanto listas são criadas com colchetes, tuplas são criadas com parênteses!`

> diretorio fase03 > projects > [exemplo-tupla.py](./scripts/exemplo-tupla.py).

- índices e loops também podem ser usados nas tuplas, seguindo a mesma lógica das listas.

### Vantagens da tupla:
- a tupla é imutável, ocupa menos espaço na memória RAM e custa menos processamento.
- economia de espaço e processamento.

## Quando a tupla é boa prática

<em>"Imagine que você esteja fazendo um software para o DETRAN do seu estado. Com você é um estudante atento e já aprendeu a modularizar seus programas, cria um módulo apenas para lidar com as carteiras de habilitação."</em>

> diretorio fase03 > projects > [exemplo-detran.py](./scripts/exemplo-detran.py).

## Principais métodos e funções

Com as tuplas, é possível utilizar alguns métodos,como:
- count() – retorna a quantidade de vezes que um valor aparece na tupla.
- index() – procura na tupla um valor e retorna o númerodo índice da primeira ocorrência desse valor.

> diretorio fase03 > projects > [exemplo-metodos-tupla.py](./scripts/exemplo-metodos-tupla.py).

Além dos métodos, podemos utilizar com as tuplas algumas funções embutidas no Python:
- all() – retorna True se todos os elementos de um objeto iterável (lista, tupla, dicionário, set etc) forem True ou também se o objeto estiver vazio.
- any() – retorna False se todos os elementos de um objeto iterável forem False ou 0 (zero). Também retorna False se o objeto estiver vazio.
- enumerate() – recebe uma coleção e a retorna como um objeto enumerado.
- len() – retorna a quantidade de elementos em uma coleção.
- max() – retorna o maior valor entre os elementos de um objeto.
- min() – retorna o menor valor entre os elementos de um objeto.
- sum() – realiza a soma dos elementos presentes em um objeto.
- tuple() – converte um objeto em uma tupla.

---

<div align="center">
<h2>2. O que está no dicionário?</h2>
</div>

> `Dicionários de dados` são estruturas em Python que funcionam seguindo a lógica de chave e valor; ou seja, podemos associar dois dados, fazendo com que um desses dados seja uma chave única que identificará um valor.

## A criação de um dicionário

- utiliza-se o símbolo de chaves.
- para criar um dicionário que contenha dados, precisamos organizá-los: primeiro escrever o dado chave, colocar o símbolo de dois pontos, e então escrever o dado valor.
- exemplo em [exemplo-dicionario.py](./scripts/exemplo-dicionario.py).

## Exibindo o conteúdo de um dicionário

- ao exibir o conteúdo, podemos associar o dicionário à chave, como em:

~~~python
print(dicionario["chave1"])
~~~

- podemos também exibir todos os valores presentes em um dicionário, por meio de um loop associado ao método values:

~~~python
for valor in dicionario.values():
  print(valor)
~~~

- é possível também exibir todas as chaves, associando um loop ao método Keys:

~~~python
for chave in dicionario.keys():
  print(chave)
~~~

- para exibir tanto as chaves quanto os valores, utilizar loop for, com duas variáveis para navegar dentro do dicionário com o método items.

~~~python
for chave, valor in dicionario.items():
  print("O personagem {} é da categoria {}.".format(chave, valor))
~~~

> exemplos em [exemplo-dicionario.py](./scripts/exemplo-dicionario.py).

## Inserindo novos dados em um dicionário

- estrutura:

~~~python
nome_do_dicionario[chave_a_ser_incluida] = valor_a_ser_incluido
~~~

> exemplos em [exemplo-inclusao-dicionario.py](./scripts/exemplo-inclusao-dicionario.py).

- a mesma estrutur utilizada para incluir novos itens serve para ***substituir*** itens que já estavam lá. Portanto, se indicarmos uma chave pré-existente, seu valor será substituído.

## Excluindo dados de um dicionário

- há 3 formas: 
  - remover um item específico por meio de sua chave,
  - remover o último item inserido ou 
  - apagar o dicionário inteiro.

> exemplos em [exemplo-exclusao-dicionario.py](./scripts/exemplo-exclusao-dicionario.py).

- `método pop()`:
  - para remover um item específico, utilizar o método pop, indicando entre parênteses a chave do item em questão.

- `mpetodo popitem()`:
  - usado para remover apenas o último item inserido.
  - em versões antigas do Python, esse método removia um item aleatório.

- `metodo clear()`:
  - limpa totalmente o dicionário.

## Dicionários dentro de dicionários

- `nested dictionaries ou dicionários aninhados` (trata-se de inserir um dicionário dentro de outro).
- exemplo: lista de contatos smartphone.
  - nome do contato como chave.
  - o valor dessa chave será outro dicionário, no qual cada chave será o nome da forma de contato e cada valor será a forma de contato em si.

> exemplo em [lista-contatos.py](./scripts/lista-contatos.py).

- para navegar nessa estrutura, é possível criar dois loops: 
  - um para o dicionário mais externo, com o nome dos contatos, 
  - e outro para o dicionário mais interno, com as formas de contato.

---

## FAST TEST

### 1. Selecione a alternativa que contém o comando correto para exibir apenas os valores de um dicionário no Python. dicionario = {"a":10, "b":20, "c":30, "d":40}
> print(dicionario.values())

### 2. Escolha a alternativa que contém o comando correto para a criação de um objeto do tipo dicionário no Python.
> dicionario = {"a":10, "b":20, "c":30, "d":40}

### 3. Qual alternativa apresenta o método para exclusão de um item específico de um dicionário? dicionario = {"a":10, "b":20, "c":30, "d":40}
> dicionario.pop("a")

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)
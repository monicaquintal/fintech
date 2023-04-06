<div id="fase02" align="center">
<h1>FASE 2 - PROTOTYPING</h1>
<h2>Capítulo 04: Quem tem o nome na lista? 📋</h2>
</div>

<div align="center">

## `Listas`

</div>

Trata-se de uma estrutura de ***conteúdo mutável*** (podemos alterar os valores ao longo do código) ***e tamanho variável*** (podemos incluir novos ou excluir valores antigos) que ***pode armazenar diversos valores***.

> Exemplo em [exemplo_array_star_wars.py](./scripts/scripts-cap04/exemplo_array_star_wars.py).

Sintaxe:

~~~python
# Criação de uma lista
lista = ["Item 1", "Item 2", "Item 3", "Item 4"]
~~~

Há duas formas principais de exibir os valores de uma lista:

### 1. Exibindo um valor específico:
- utilizar seu índice! 
- cada valor que está presente na lista pode ser identificado por um número inteiro (índice), que ***inicia por 0***.

~~~python
print(item[2])
~~~

### 2. Exibindo a lista completa:
- utilizar o loop for. 
- informar a lista, e não a função range, como os valores que a variável pode assumir.

~~~python
for item in lista:
  # Para cada volta do loop, exibir o valor assumido
  print(item)
~~~

## Adicionando valores à lista

### 1. Método `append()`:
- é a solução mais simples.
- permite que um valor seja inserido ao final da lista.

~~~python
lista.append("novo item")
~~~

- se quisermos que o usuário digite o valor que será colocado no fim da lista, basta substituir o valor que está entre parênteses por um comando de input.

~~~python
lista.append(input("Digite um novo item: "))
~~~

### 2. Método `insert()`:
- permite incluir um valor em uma posição específica de sua lista.
- exige que o programador informe o índice em que o valor deve ser inserido.

~~~python
lista.insert(1, "novo item")
~~~

- ou seja, ao utilizar esse método, os índices dos outros valores são modificados para que a sequência se mantenha.
- para permitir que o usuário digite o valor, seguimos a mesma lógica acima.

~~~python
lista.insert(2, input("Digite um novo item: "))
~~~

## Removendo itens da lista

### Método `pop()`:
- remove o último valor inserido.

~~~python
lista.pop()
~~~

- para remover um item de uma ***posição específica***, indicar um índice entre parênteses.

~~~python
lista.pop(3)
~~~

### Método `remove()`:
- permite que indiquemos qual valor deve ser localizado e removido de qualquer posição da lista.

~~~python
lista.remove("item")
~~~

## Outros métodos importantes:

> arquivos [outros_metodos.py](./scripts/scripts-cap04/outros_metodos.py) e [media_notas.py](./scripts/scripts-cap04/media_notas.py).

### 1. `count()`:
- retorna a quantidade de vezes que um elemento aparece na lista.

### 2. `sort()`:
- organiza a lista em ordem crescente/alfabética.

### 3. `reverse()`:
- inverte a ordem dos elementos de uma lista.

Há, ainda, algumas ***funções*** importantes, como:

### 1. len:
- retorna o tamanho de um objeto.

### 2. sum:
- realiza a soma dos elementos presentes em um objeto.

---

## Funções

> arquivo [velocidade_media.py](./scripts/scripts-cap04/velocidade_media.py).

- podem ser consideradas “microprogramas”, que têm uma única função específica e podem ser convocadas quando necessárias.
- para indicar ao Python que uma nova função está sendo criada, utilizar a ***palavra reservada*** `def`, seguida do nome da função.
- uma função só entra em funcionamento quando ela é convocada.

~~~python
def nomeDaFuncao():
~~~

paginas 7 e 16
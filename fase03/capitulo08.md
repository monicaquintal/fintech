<div id="fase03" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 08: Salvo pelo dicionário! 📙</h2>
</div>

<div align="center">
<h2>Por que as listas não são o suficiente?</h2>
</div>

> Usando o módulo sys do Python (que é instalado por padrão), podemos verificar o tamanho de qualquer objeto por meio do método getsizeof().

- uma lista, ainda que vazia, ocupa um espaço na memória, conforme script encontrado em:

> pasta fase03 > projects > exemplo-getsizeof.py.
- incluir, reordenar e remover novos elementos têm um custo que se traduz em espaço em memória RAM.
- neste capítulo, aprenderemos que há outras estruturas mais adequadas do que a lista, cada uma voltada para uma situação específica.

<div align="center">
<h2>Trabalho em tupla</h2>
</div>

- tuplas ou tuples:
  - são estruturas da linguagem Python parecidas com listas, mas com a característica de serem **imutáveis**. 
  - todos os dados que armazenarmos dentro de uma tupla permanecerão idênticos e na mesma posição ao longo de toda a execução do programa.
- `enquanto listas são criadas com colchetes, tuplas são criadas com parênteses!`

> diretorio fase03 > projects > exemplo-tupla.py

- índices e loops também podem ser usados nas tuplas, seguindo a mesma lógica das listas.

### Vantagens da tupla:
- a tupla é imutável, ocupa menos espaço na memória RAM e custa menos processamento.
- economia de espaço e processamento.

<div align="center">
<h2>Quando a tupla é boa prática</h2>
</div>

<em>"Imagine que você esteja fazendo um software para o DETRAN do seu estado. Com você é um estudante atento e já aprendeu a modularizar seus programas, cria um módulo apenas para lidar com as carteiras de habilitação."</em>

> diretorio fase03 > projects > exemplo-detran.py

<div align="center">
<h2>Principais mpetodos e funções</h2>
</div>


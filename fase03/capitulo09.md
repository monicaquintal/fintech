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

## QUIZ - MODELING

1. Ao analisar a combinação de notas que são sacadas nos caixas eletrônicos instalados nos vários bairros da cidade de São Paulo, um analista de sistemas chegou à conclusão de que seria mais interessante abastecer os caixas eletrônicos instalados no bairro Pinheiros apenas com cédulas de R$ 100. No contexto de dados versus informações, tal conclusão representa um(a): 

> Informação

2. Considere as seguintes afirmações:

I – Um Banco de Dados representa algum aspecto do mundo real, às vezes chamado de minimundo. As mudanças no minimundo são refletidas no Banco de Dados.<br>
II - Um Banco de Dados é uma coleção logicamente coerente de dados com algum significado inerente.<br>
III – Um Banco de Dados é projetado, construído e populado com dados para uma finalidade específica.<br>
Em relação às afirmações acima, assinale a alternativa correta:

> Todas as afirmativas estão corretas

3. Assinale a alternativa que complete corretamente a frase a seguir: "Na modelagem de dados, são utilizados três tipos de modelos de dados, que são os modelos _____________, _____________ e _____________.".

> conceitual, lógico e físico.

4. Para identificar uma entidade, deve-se focar no problema em pauta e perguntar-se: “Quais são as ‘coisas’ neste problema?”. Assim, uma competição, como uma corrida de Fórmula 1, por exemplo, representa uma entidade do tipo:

> Incidente

5. O endereço completo de uma pessoa é um exemplo de atributo:

> Multivalorado

6. Um objeto que existe no mundo real com uma identificação distinta e com um significado próprio é chamado de:

> Entidade

7. Em relação ao relacionamento Um-para-Muitos (1:n), assinale a alternativa correta:

> Para cada registro da primeira tabela, pode existir um ou mais correspondentes na segunda tabela, e para cada registro na segunda tabela existe apenas um registro correspondente na primeira tabela.

8. Em relação ao Modelo Entidade-Relacionamento, um atributo que pode possuir várias ocorrências é chamado de atributo:

> Multivalorado

9. Considere a seguinte situação da vida real: “Um médico atende muitos pacientes, e um paciente pode realizar consultas com vários médicos (várias especialidades médicas).” Assim, na modelagem de um banco de dados, para melhor descrever o relacionamento entre médico e paciente, podemos incluir a consulta como um atributo do relacionamento entre eles. Esta situação representa um exemplo de:

> agregação.

10. A herança de atributos é uma consequência do processo de:

> Especialização/generalização

11. As formas normais são as técnicas que evitam: 

> Redundância de dados

12. Em relação à normalização de dados, considere as seguintes afirmações:
I – Normalizar o banco diminui ou elimina as anomalias dos dados.<br>
II – Geralmente, aumenta o número de tabelas do banco de dados.<br>
III – É baseada em 5 etapas, conhecidas como Formas Normais.<br>
Em relação às afirmações acima, assinale a alternativa correta:

> Apenas as afirmações I e III estão corretas.

13. A frase “É uma subdivisão da linguagem SQL utilizada para definir as estruturas de dados.”, refere-se à linguagem:

> DDL (Data Definition Language)

14. Todas as tabelas devem possuir uma:

> Chave primária

15. Assinale a alternativa que apresenta corretamente funções utilizadas com tuplas em Python:

> min() / max() / len()

16. Os dicionários de dados são estruturas em Python que funcionam seguindo a lógica de chave e:

> Valor

17. Em Python, para remover um item específico de um dicionário, utilizamos o método:

> pop.

18. Os arquivos, que contêm coleções de caracteres ou coleções de bytes são classificados em:

> Arquivo texto e arquivo binário.

19. A função open(), utilizada em Python para abrir um arquivo, além do nome do arquivo, pode ser utilizada com um segundo parâmetro para especificar a forma como o arquivo em questão será manipulado. Para abrir um arquivo para anexação de informações, devemos utilizar o parâmetro:

> 'a'

20. Para garantir que um arquivo que foi aberto seja finalizado sem ter que se preocupar com o close() ao final da manipulação de um arquivo, utilizamos o comando:

> with

---

## CHALLENGE BRQ

### DESAFIO
<br>
No início de 2023 a BRQ Digital Solutions fez seu primeiro investimento do ano, a companhia injetou R$ 1,3 milhão na Easy Carros, que ajuda pequenas e médias locadoras a serem mais competitivas e digitais.
<br>
O investimento foi feito por meio do Innovation Hub, centro de inovação da BRQ criado em 2016 para acelerar a inovação de clientes e áreas de negócios a partir de aportes, parcerias e intraempreendedorismo. O foco do centro de inovação está em empresas B2B e software as a service (SaaS) que já têm clientes, mas estão no estágio seed, com uma atenção especial para as fintechs e insurtechs. Mais detalhes em https://startups.com.br/noticias/brq-investe-r-13-mi-em-plataforma-para-locadoras-de-carros/.
<br>
Com isso, a BRQ desafia os alunos do curso de Análise e Desenvolvimento de Sistemas a criar uma solução com o objetivo de reconstruir projetos para o mercado de locadoras de veículos.
<br>

### Primeiro Semestre

- Definições: Identificar os requisitos funcionais e não funcionais da plataforma.
- Protótipo: Criar um protótipo da plataforma e apresentar como será a arquitetura do sistema.
- Conceitualização: Apresentar uma descrição detalhada do sistema, incluindo a tecnologia utilizada, o modelo de negócios, o público-alvo, a proposta de valor, o fluxo de trabalho etc.
- Modelagem: Modelagem das entidades e relacionamentos da plataforma.

### ENTREGA

Uma pasta compactada com:
<br>

- Apresentação (ppt ou pdf).
- Requisitos funcionais e não funcionais.
- Descrição detalhada do sistema, tecnologia utilizada, o modelo de negócios, o público-alvo, a proposta de valor, o fluxo de trabalho etc.
- Pasta Compactada com o protótipo da solução (Figma ou outra ferramenta).
- PDF ou imagem com do modelo de dados (MER).

Importante: Por se tratar de uma entrega referente ao Challenge, não será possível fazer a entrega posterior com o prazo de três dias valendo 70% da nota.
<br>
A equipe será configurada na plataforma no momento de entrega do projeto.

---

## GLOBAL SOLUTION 1º SEMESTRE

### IAs generativas, Inovação e Tecnologia ajudando a solucionar os problemas da Fome mundial e da escassez de alimentos, promovendo a agricultura sustentável. 

A fome mundial e a escassez de alimentos são problemas complexos e urgentes que afetam milhões de pessoas em todo o mundo. A ONU, em seu conjunto de Objetivos de Desenvolvimento Sustentável (ODS), inclui o ODS 2, Fome Zero e Agricultura Sustentável como metas para erradicar a fome e promover sistemas agrícolas sustentáveis até 2030.
<br>
Fatos sobre a Fome:
<br>

- Em 2020, entre 720 milhões e 811 milhões de pessoas em todo o mundo estavam sofrendo de fome, cerca de 161 milhões a mais do que em 2019.
- Também em 2020 impressionantes 2,4 bilhões de pessoas, ou mais de 30% da população mundial, estavam moderada ou severamente inseguras alimentarmente, isto é, sem acesso regular a alimentos adequados.
- Globalmente, 149,2 milhões de crianças com menos de 5 anos de idade, ou 22,0% do total, estavam sofrendo de retardo de crescimento (nanismo - baixa estatura para a idade) em 2020.
- Para alcançar a meta de uma redução de 5% no número de crianças com retardo de crescimento até 2025, a taxa atual de declínio anual - 2,1% - deve dobrar para 3,9%.
- Em 2020, a caquexia (baixo peso para a estatura) afetou 45,4 milhões ou 6,7% das crianças com menos de 5 anos de idade.
- A parcela de países sobrecarregados por preços elevados de alimentos, que havia sido relativamente estável desde 2016, aumentou drasticamente de 16% em 2019 para 47% em 2020.
<br>
As metas da ODS2 são:
<br>

- Até 2030 acabar com a fome e garantir o acesso de todas as pessoas, em particular os pobres e pessoas em situações vulneráveis, incluindo crianças, a alimentos seguros, nutritivos e suficientes durante todo o ano.
- Até 2030 acabar com todas as formas de má-nutrição, incluindo atingir até 2025 as metas acordadas internacionalmente sobre nanismo e caquexia em crianças menores de cinco anos de idade, e atender às necessidades nutricionais dos adolescentes, mulheres grávidas e lactantes e pessoas idosas.
- Até 2030 dobrar a produtividade agrícola e a renda dos pequenos produtores de alimentos, particularmente das mulheres, povos indígenas, agricultores familiares, pastores e pescadores, inclusive por meio de acesso seguro e igual à terra, outros recursos produtivos e insumos, conhecimento, serviços financeiros, mercados e oportunidades de agregação de valor e de emprego não agrícola.
- Até 2030 garantir sistemas sustentáveis de produção de alimentos e implementar práticas agrícolas resilientes, que aumentem a produtividade e a produção, que ajudem a manter os ecossistemas, que fortaleçam a capacidade de adaptação às mudanças climáticas, às condições meteorológicas extremas, secas, inundações e outros desastres, e que melhorem progressivamente a qualidade da terra e do solo.
- Até 2030, manter a diversidade genética de sementes, plantas cultivadas, animais de criação e domesticados e suas respectivas espécies selvagens, inclusive por meio de bancos de sementes e plantas diversificados e bem geridos em nível nacional, regional e internacional, e garantir o acesso e a repartição justa e equitativa dos benefícios decorrentes da utilização dos recursos genéticos e conhecimentos tradicionais associados, como acordado internacionalmente.
<br>
As IAs generativas são tecnologias promissoras que podem ajudar a solucionar esses problemas. Essas IAs são capazes de gerar imagens, texto e até mesmo som de forma autônoma, com base em um conjunto de dados de entrada.
<br>
Na agricultura, as IAs generativas podem ser utilizadas para criar modelos de cultivo mais eficientes e sustentáveis, permitindo o cultivo de alimentos em áreas antes consideradas inadequadas para a agricultura. Por exemplo, as IAs podem ser usadas para prever condições climáticas e de solo, a fim de melhorar o manejo do cultivo e reduzir o desperdício de água e outros recursos naturais.
<br>
Além disso, as IAs generativas também podem ser usadas para ajudar a resolver problemas de segurança alimentar em regiões remotas ou de difícil acesso, por meio da criação de modelos de agricultura vertical, aquaponia e hidroponia, que podem ser utilizados para cultivar alimentos em ambientes fechados e controlados, com eficiência e produtividade.
<br>
A tecnologia e a inovação também podem ajudar a melhorar a distribuição de alimentos, desde a colheita até a entrega aos consumidores. As IAs generativas podem ser usadas para criar modelos de logística eficientes, reduzindo o desperdício de alimentos e os custos de transporte.
<br>
As IAs generativas têm um enorme potencial para ajudar a solucionar os problemas da fome mundial e da escassez de alimentos, promovendo a agricultura sustentável. Combinadas com outras tecnologias e inovações, podem ajudar a alcançar o ODS 2 da ONU e garantir um futuro alimentar sustentável para todos.
<br>
A FIAP uniu-se a Kraft Heinz, Microsoft e a Ong Caça-Fome para, por meio da tecnologia, promover ações para reduzir a fome global, a escassez de alimentos e promover a agricultura sustentável.
<br>

### Desafio: A tecnologia e a inovação têm um papel fundamental a desempenhar no combate à fome mundial e à escassez de alimentos. Você e seu time tem o desafio de desenvolver uma solução em software que interaja com uma IA generativa. Analise as metas da ODS2 e encontre uma solução inovadora e que permita alcançar alguma meta.
<br>
Tarefas: Estruture uma apresentação com os itens abaixo e grave um pitch de 3 minutos:
<br>

- Qual o problema será resolvido pela solução?
- Explique como funciona a solução.
- Apresente um protótipo da solução.
- Modelagem de dados da solução. 
- Como será a interação com a IA generativa.
<br>
Na apresentação insira o nome completo de cada aluno e o rm.
<br>
ENTREGA: UMA PASTA COM A APRESENTAÇÃO E O VÍDEO.
<br>

### DICAS PARA O PITCH
<br>
SEJA CLARO E OBJETIVO
<br>
Adotar uma linguagem objetiva é chave para o sucesso de um pitch. Afinal, é importante lembrar que você conta com pouco tempo para passar uma quantidade razoável de informações. Dito isso, de nada adianta preencher o tempo com dados complexos, já que isso vai dificultar a assimilação por parte da audiência.
<br>
A dica é focar exclusivamente o que seu público mais precisa entender para que você alcance seu objetivo.
<br>

### EXPLIQUE O PROBLEMA E SUA SOLUÇÃO
<br>
Por mais curta e objetiva que seja a apresentação, é fundamental encontrar espaço para explicar o problema que sua empresa busca resolver e como ela pretende fazer isso. Nesse momento, é crucial que você tenha conhecimento sobre o assunto, já que, sem isso, será difícil passar a confiança tão buscada por investidores.

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)
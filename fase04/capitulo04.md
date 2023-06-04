<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 04: Aplicando algum estilo. 💁‍♀️</h2>
</div>

<div align="center">
<h2>1. APLICANDO ALGUM ESTILO</h2>
</div>

### `CSS`:
- Cascading Style Sheets (Folhas de Estilo em Cascata).
- permite formatar qualquer tipo de conteúdo existente na página, aplicando formatação às tags HTML.
- é possível criar um conjunto de formatações para um simples elemento, uma página inteira ou até um site completo.
- por boa prática, as regras CSS (qual elemento será formatado, o que queremos estilizar e como ele deverá ficar) devem ficar em um arquivo com extensão .css, chamado de folha de estilos.

## 1.1 Tipos de CSS

- há três formas diferentes: CSS inline, CSS interno ou CSS externo.

### 1.1.1 CSS Inline 

- inserção de código CSS dentro do elemento HTML que desejamos formatar. 
- é possível através da utilização do atributo style.

> exemplo [aqui](./projetos/projeto3/pages/index.html)!

~~~
- sempre utilizar dois pontos (:) para separar propriedade e valor. 
- após o valor, ponto e vírgula (;) indica que aquela estilização foi finalizada.
~~~

- ***utilização de CSS inline não é uma boa prática.***
  - causa mistura das camadas de conteúdo e formatação.
  - devemos estilizar linha por linha, tornando a tarefa inviável.

### 1.1.2 CSS Interno

- criação das regras dentro da seção &lt;head&gt; da página. 
- melhor que CSS inline, mas também possui restrições que podem indisponibilizar seu uso:
  - As regras criadas afetarão apenas a página em que ela estiver inserida.
  - Conteúdo da página misturado com formatação, pois embora em seções diferentes, estarão no mesmo arquivo.
  - Aumento no tempo de carregamento da página.
  - Em caso de manutenção em um site que foi montando dessa forma, será necessário fazer as mesmas alterações em várias páginas (retrabalho).
- uma declaração de regra CSS interna deve possuir: um seletor, uma propriedade e um valor.
  - ou seja, igual ao CSS inline, porém ocorrerá na seção head da página!
- utilizar a `tag <style>`!
  - e como boa prática, usar o **atributo type**, que indicará o tipo de mídia de Internet que será usado.
    - valor padrão é **text/css**.

> Os estilos criados serão aplicados a todos os elementos declarados.

CSS Interno é melhor que CSS Inline, mas ainda não é o ideal.

### 1.1.3 CSS Externo

- criação de regras dentro de um novo arquivo que será a folha de estilos. 
  - esse arquivo deverá ser salvo com o nome desejado seguido da extensão .css.
  - um nome muito comumente usado é `style.css`.
  - também é boa prática tem uma pasta para receber as folhas de estilo!
- ***vantagens do CSS interno***:
  - separação das camadas de conteúdo e de formatação.
  - facilidade de manutenção do código.
  - a mesma folha de estilos pode formatar várias páginas ao mesmo tempo.
  - os arquivos ficam mais leves, aumentando a performance da página.

***Importante***:
- fazer um link do HTML com o CSS.
- deve ocorrer na seção &lt;head&gt;, com uso da tag &lt;link&gt;. 
- incluir o **atributo rel**, que define que o link é relativo a uma folha de estilos.
- outro obrigatório é o **atributo href**, que deve conter o endereço e nome do arquivo CSS a ser linkado.

> exemplo [aqui](./projetos/projeto3/css/style.css) e [aqui](./projetos/projeto3/pages/index.html).

- as regras CSS são declaradas dentro do arquivo style.css, e irão formatar todas as páginas do projeto que possuírem o seu link!

## 1.2 Especificidade

- define qual seletor é mais específico, ou seja, determina qual regra deve ser aplicada.

> CSS INLINE (1º) > CSS INTERNO (2º) > CSS EXTERNO (3º)

## 1.3 Herança

- quando nenhuma propriedade CSS for declarada, o elemento HTML herdará as propriedades do seu elemento pai.
- exemplo: se houver estilização para body e h1, caso hajam elementos p no código, seguirão a formatação do body (elemento pai).

## 1.4 Padrão de Cores na Web

1. Nome da cor:
- nome correspondente à cor desejada: blue, white, black, red, etc. 
- caso queira trabalhar com tonalidades diferentes de uma cor, será necessário lembrar do nome correto para que a cor seja aplicada. 
- evitar!!!

2. Padrão hexadecimal:
- sequência de 6 caracteres (letras e números) que variam de 0 a 9 e de A a F, precedidos de um hashtag (#).
- o primeiro e segundo caracter representam a intensidade da cor vermelha, o terceiro e quarto a intensidade de da cor verde e o quinto e sexto a intensidade da cor azul. 
- o menor valor possível será o #000000 (representa a cor preta), e o maior valor será o #FFFFFF (representa a cor branca). 
- é uma das formas mais comuns de declarar uma cor.

3. Padrão RGB:
- sequência de três valores que variam de 0 a 255, representando a intensidade dos tons de vermelho (R), verde (G) e azul (B). 
- parecido com o hexadecimal, porém com uma escala numérica maior: para declarar a cor preta usamos rgb(0, 0, 0), cor branca rgb(255, 255, 255).
- sequência de valores mais lógica do que a hexadecimal.

4. Padrão RGBA: 
- mesmo conceito e valores do RGB acrescido de um canal Alpha (opacidade/transparência). 
- 0.0 para transparente e 1.0 para opaco.
- caso queira uma cor vermelha mais transparente pode usar: rgba(194, 46, 46, 0.5), por exemplo (o maior valor foi usado para a cor vermelha, sendo assim ela será a cor predominante).

5. Padrão HSL:
- com esse padrão definimos o tom da cor (H), sua saturação (S)e sua luminosidade(L). 
- o valor da cor é definido em graus variando de 0° a 360°, e as cores são observadas no que é chamado de roda de cores. 
- a saturação tem seu valor definido em porcentagem: 0% ficará em tom de cinza e 100% na saturação máxima.
- a luminosidade será definida em porcentagem: 0% ficará na cor preta e 100% na cor branca.
- este padrão está sendo bem utilizado, principalmente na criação de paletas de cores.

## 1.5 Formatação de textos

### 1.5.1 Font-family

- define a família de fontes que será usada pelos elementos.
- podemos declarar uma ou mais fontes na mesma regra: 
  - caso uma fonte não esteja disponível no dispositivo que o usuário está fazendo acesso, ele tentará usar a outra fonte declarada.
  - se nenhuma fonte estiver disponível, será usado o padrão do navegador, na maioria das vezes Times New Roman.

### 1.5.2 Usando o Google Fonts

- um dos melhores servidores de fontes é o [Google Fonts](https://fonts.google.com/).
- para utilizar:
  - abra a fonte desejada clicando no nome dela. 
  - há vários estilos, selecionar aqueles que serão  usados no projeto.
  - no painel Review, teremos as fontes e os respectivos estilos.
  - logo abaixo encontramos as opções para usar as fontes pela Web, e possui duas opções: 
    - link, que deve ter seu conteúdo copiado e colado na seção &lt;head&gt; da página.
    - opção import, que deve ter seu conteúdo copiado e colado na primeira linha do arquivo CSS.
    - qual das opções escolher? A opção link fará um carregamento mais rápido, mas como deve ser inserida no HTML, todas as páginas do projeto deverão possuir as linhas de link para usar as fontes selecionadas. Já a opção import ficará dentro do arquivo CSS, e como esse arquivo é linkado no HTML, a referência da fonte será feita automaticamente em um único arquivo.
    - o prof recomenda usar o link!
  - inserir a regra que define a família de fontes que será usada em sua página web.
  - selecionar as regras definidas e colar nos seletores CSS onde as fontes serão usadas.

### 1.5.3 Font-size

- define o tamanho da fonte dos elementos HTML.
- pode fazer uso de várias unidades de medida.
  - o pixel (px) é a mais comum para essa propriedade.

### 1.5.4 Font-weight

- define a espessura da fonte dos elementos HTML. 
- podemos declarar valores entre 100 (mais fina) e 900 (mais grossa).
- também é possível fazer a declaração através de palavras-chave: bold, bolder lighter e normal.

### 1.5.5 Font-style

- define o estilo da fonte.
- pode receber os valores: italic, oblique e normal.

### 1.5.6 Text-align

- define o alinhamento do texto.
- pode receber os valores: left, right, center e justify.

### 1.5.7 Text-decoration

- consiste em uma linha que poderá ficar acima (overline), abaixo (underline) ou no meio (line-through) do conteúdo. 
- é comum nos links, tag &lt;a&gt;. 
- usando o valor none, retiramos a decoração.

### 1.5.8 Text-transform

- define se os textos ficarão em letras maiúsculas (uppercase), minúsculas (lowercase) ou se apenas a primeira letra de cada palavra ficará maiúscula (capitalize).

### 1.5.9 Word-spacing

- define o espaçamento entre as palavras.

### 1.5.10 Letter-spacing

- define o espaçamento entre as letras de um texto.

### 3.5.11 Line-height

- altera a altura das linhas de um elemento. 
- nos textos com fonte pequena, usamos essa propriedade para aumentar a distância entre uma linha e outra, facilitando a leitura.
- nos textos com letras muito grandes, podemos diminuir a altura da linha para agrupar o conteúdo.

## 1.6 Formatação de listas

### 1.6.1 Formatando listas ordenadas

- podemos mudar o número inicial utilizando a propriedade list-style, que pode receber os seguintes valores:

<div align="center">

Valor | O que será inserido
------|---------------------
None | Retira o marcador da lista
Decimal | Números iniciando em 1
Lower-alpha | Letras minúsculas do alfabeto
Upper-alpha | Letras maiúsculas do alfabeto
Lower-roman | Números romanos minúsculos
Upper-roman | Números romanos maiúsculos

</div>

### 1.6.2 Formatando listas não ordenadas

- podemos utilizar a propriedade list-style para fazer a mudança do marcador que indica o item da lista:

<div align="center">

Valor | O que será inserido
------|---------------------
None | Retira o marcador da lista
Disc | 🔴
Circle | ⭕
Square | 🟥

</div>

- podemos também usar a propriedade list-style-image para inserir uma imagem como se fosse um marcador. 

~~~css
ul { 
  list-style-image: url(../images/code.png);
}
~~~

## 1.7 Imagens: alterando o tamanho e arredondando os cantos

- propriedades width (largura) e height (altura).
- outra pripriedade comum é a border-radius, que torna os cantos da imagem arredondados.

## 1.8 Imagens: aplicando filtros

- propriedade filter aplica efeitos visuais às imagens.

### 1.8.1 Blur

- aplica um desfoque na imagem.
- o valor inicial é 0 (imagem sem nenhum tipo de alteração); quanto maior o valor, mais desfocada.

### 1.8.2 Brightness

- controla o brilho da imagem. 
- valores abaixo de 100% deixarão a imagem mais escura, enquanto valores acima de 100% deixarão a imagem mais clara.

### 1.8.3 Opacity

- aplica transparência às imagens. 
- 0% deixa a imagem transparente, enquanto 100% deixará a opacidade inalterada.

### 1.8.4 Saturate

- definirá a pureza ou a intensidade de uma cor. 
- quanto menor for o valor, mais próximo estará da cor cinza; quanto maior for o valor definido, mais intensa ficará.

### 1.8.5 Contrast

- define contraste das imagens. 
- para diminuir o contraste, valores abaixo de 100%; para aumentarmos, valores acima de 100%.
- se uma imagem receber o valor 0, ela ficará cinza.

### 1.8.6 Drop-shadow

- cria uma sombra em volta do elemento.
- para defini-la devemos usar quatro valores:
  - primeiro valor define a distância do eixo X. 
    - valores negativos deixam a sombra à esquerda da imagem. 
    - valores positivos deixam a sombra à direita.
  - segundo valor define a distância do eixo Y.
    - valores negativos deixam a sombra acima da imagem.
    - valores positivos deixam a sombra abaixo da imagem.
  - terceiro valor definirá o desfoque da sombra.
    - quanto maior o valor, maior será o desfoque.
  - quarto valor definirá a cor da sombra.

### 1.8.7 Grayscale

- deixa a imagem com um padrão de cores em escala de cinza. 
- 0% deixará a imagem com a cor inicial; conforme o valor for aumentado, a escala de cinza começará a ser visualizada até chegar o valor final de 100%.

---

### [Laboratório CSS](./projetos/projeto2/assets/css/style.css)

---

## FAST TEST

### 1. Sobre a linguagem CSS, qual das afirmações é FALSA:
> A maneira mais simples de se aplicar CSS em um documento HTML é utilizando o atributo global style na tag que se deseja formatar.

### 2. Um estilo será definido utilizando o seguinte padrão; identifique a afirmação FALSA:
~~~css
seletor {
  propriedade: valor;
  propriedade: valor;
}
~~~
>Ponto e vírgula: inserir o ponto e vírgula na instrução CSS é opcional.

### 3. A propriedade display permite controlar a visualização de um elemento, mostrando e escondendo elementos na tela de forma dinâmica. Identifique o valor FALSO:
> inline-block: será exibido como um elemento de tabela, comportando-se como uma linha, coluna, célula, tabela, entre outros, dependendo da opção selecionada.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)
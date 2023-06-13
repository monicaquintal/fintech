<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 08: Design Responsivo. 📱💻</h2>
</div>

<div align="center">
<h2>1. DESIGN RESPONSIVO</h2>
</div>

- através de um conjunto de regras CSS, define como o layout de uma página vai se comportar em telas de tamanhos diferentes.
- o termo `design responsivo` foi criado em 2010, e publicado [neste artigo](https://alistapart.com/article/responsive-webdesign/).
- sites responsivos devem:
  - exibir seus conteúdos da mesma forma, independente do tipo de dispositivo usado.
  - responder a mudanças de orientação do dispositivo: retrato (vertical) ou paisagem (horizontal).

## 1.1 Antes do design responsivo

### 1.1.1 Layout fixo

- caracterizado por possuir um tamanho fixo para o container.
  - ou seja, nunca mudará, independente do tipo de dispositivo que use para acessá-lo: notebook, tablet ou smartphone.
- para definir o tamanhofixo, utiliza-se como unidade de medida o pixel(px).
- o usuário terá uma péssima experiência com a página.

### 1.1.2 Layout fluído

- se ajusta ao tamanho da tela, aumentando ou diminuindo sem alterar a sua estrutura. 
- utiliza unidades de medida relativas, e a mais comum é a porcentagem (%). 
- com layout fluído, o conteúdo pode não se ajustar de forma agradável, principalmente em telas grandes (página e conteúdo ficarão esticados) ou pequenas (o conteúdo pode ficar aglomerado em pequenas faixas). 
- não garante uma boa experiência ao usuário.

### 1.1.3 Layout adaptativo

- utiliza códigos específicos para diferentes dispositivos. 
- trata-se um site com várias versões de CSS.
- assim que for detectada a resolução do dispositivo, é enviada a versão do código correspondente para aquela resolução.
- pode utilizar medidas fixas ou flexíveis.
- se pensar no grande número de dispositivos e resoluções que existem no mercado, dará muito trabalho manter essas versões atualizadas.
- já foi muito utilizado; atualmente, o design responsivo se mostra melhor solução.

## 1.2 Viewport

- por meio da `meta tag viewport` (dentro da seção &lt;head&gt;), o browser detecta o tamanho da área de exibição de conteúdo do dispositivo que está sendo usado.
- esse tamanho pode variar de dispositivo para dispositivo, sendo menor em um smartphone e maior em um notebook. 
- essa meta tag recebe dois atributos: 
  - `content`: define que a largura da página deve seguir a largura da tela do dispositivo.
  - `initial-scale=1.0`: define que o nível de zoom inicial da página será de 100%.
- ***Conceito design responsivo:*** assim que o viewport for detectado, a CSS é consultada para verificar se há alguma regra que para aquele tamanho de dispositivo; caso exista, essa regra será aplicada, fazendo com que o layout responda automaticamente ao tamanho da tela detectada.

## 1.3 Pilares do design responsivo

### 1.3.1 Layout fluído

- permitirá que os elementos se redimensionem conforme o tamanho da tela do usuário (projetado para utilizar porcentagem (%) como medida relativa). 
- a porcentagem garante tamanmhos proporcionais para os containers, auxiliando no redimentionamento e exibição do conteúdo.

### 1.3.2 Imagens Flexíveis

- precisamos que as imagens fiquem no tamanho compatível com o container e não percam a resolução.
- podemos usar a `propriedade max-width`, tendo como valor 100%: dessa forma, a imagem ocupará a largura total do elemento onde foi inserida. 
- em CSS há uma regra para seletor de tag img: ela define que a largura máxima das imagens será de 100% (as imagens não ultrapassam o tamanho máximo dos containers onde foram inseridas).

### 1.3.2 Media Queries

- são pontos de quebra do layout (`breakpoints`). 
- permitem definir como o conteúdo da página será visualizado em dispositivos com tamanhos de telas diferentes.
- representam uma faixa específica de pixels que definem como o layout da sua página deve responder a um tamanho de tela específico, dentro de regras CSS. 
- funcionamento:
  - browser detecta o viewport do dispositivo que está fazendo acesso.
  - browser consulta arquivo CSS para ver se existe  alguma regra definida para aquele viewport (breakpoint).
  - encontrando a regra, faz a renderização conforme a declaração. 
  - caso não encontre, executará a renderização padrão.

> Podemos testar como a página será exibida em diferentes dispositivos, basta acessar o navegador, clique direito na página para abrir o menu suspenso, clique na opção “inspecionar”. Um painel lateral será visualizado, então clicar no botão que tem um ícone representando um celular e um tablet, e escolher um dos dispositivos apresentados na opção "Dimensions Responsive".

- utilizar propriedades CSS `min-width e max-width`, definindo regras para uma escala de valores nos quais diferentes dispositivos se encaixam.
- para ter uma ideia das resoluções mais comuns entre os usuários, há alguns sites que oferecem informações sobre análise de tráfego na Internet, um deles é o [Statcounter](https://gs.statcounter.com/screen-resolution-stats).
- para definir uma media querie:

~~~css
@media(breakpoint) { 
  Regras que serão aplicadas
}
~~~

- cuidado para não confundir max-width com min-width: 
  - com max-width, você declara a resolução máxima a ser atingida.
  - com o min-width, você declara a resolução mínima a ser atingida.

## 1.4 Mobile First: começando do menor para o maior

- Mobile First é uma forma de pensar no desenvolvimento de páginas web.
- o foco inicial é direcionado para os dispositivos móveis e somente depois para dispositivos maiores.
- a ideia surgiu em 2009, e é considerada uma das boas práticas para desenvolvimento Web.
- ***vantagens***:
  - ajuda a hierarquizar os elementos que serão prioridade para o usuário, pois há pouco espaço nos smartphones.
  - o conteúdo deverá estar posicionado de forma clara, fácil de localizar e visualmente bonito. 

> Dê ao usuário a experiência que ele merece, independe do dispositivo que ele usa!

## 1.5 Criando um exemplo responsivo
### 1.5.1 [Código HTML](./projetos/projeto10/pages/exemplo-aula.html)
### 1.5.2 [Código CSS](./projetos/projeto10/css/exemplo-aula.css)

---

## Laboratório Design Responsivo: [HTML](./projetos/projeto10/pages/projeto10.html) e [CSS](./projetos/projeto10/css/projeto10.css).

---

## FAST TEST

### 1. Assinale a alternativa que completa corretamente a frase a seguir: "O _____________ define a abrangência das variáveis, ou seja, onde elas podem ser acessadas."
> escopo.

### 2. Os nomes das variáveis devem iniciar com:
> dois hífens (--).

### 3. Ícones são muito comuns em qualquer página Web, eles podem ajudar no visual, deixando a informação mais clara ao usuário. Uma das coleções de ícones mais utilizadas do mundo é a biblioteca:
> Font Awesome.

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)
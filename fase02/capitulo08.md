<div id="fase02" align="center">
<h1>FASE 2 - PROTOTYPING</h1>
<h2>Capítulo 08: Quem vê interface, vê coração. ❤️</h2>
</div>

<div align="center">

## Design de Interfaces

</div>

- faz parte da User Experience.
- trata da criação das telas e componentes de um produto digital, com foco em seu visual e estilo.
- o profissional de UI (`User Interface`) geralmente tem background de design gráfico.

<div align="center">

## Conceitos básicos de design gráfico

</div>

## Gestalt
- palavra de origem germânica, que significa "forma" ou "figura".
- o termo em teve seu significado ampliado para o "todo unificado". 
- trata-se da ***percepção da unidade de vários elementos***, ou seja: o inteiro é interpretado diferente que a soma de suas partes.
- há algumas leis que a compõem, listadas a seguir.

### 1. Semelhança

- a lei da semelhança faz com que nossa mente identifique elementos semelhantes e os agrupe entre si.

### 2. Proximidade

### 3. Continuidade

- nossa mente vê os pontos conectados por uma linha reta ou curva como uma linha só.

### 4. Pregnância

- na lei da simplicidade ou pregnância, assimilamos os objetos da forma mais simples possível. 

### 5. Fechamento

- de acordo com essa lei, vemos um objeto completo mesmo quando não há um.

> Essas regrinhas básicas vão fazer toda a diferença na hora de desenvolver a interface!

## Responsivo, adaptativo e versão mobile: qual escolher?

- ao criarmos uma interface web, é essencial definir logo no início a abordagem, desde o layout estático até a construção dos elementos em código.

### A) Design Responsivo:
- é o mais fluido.
- o conteúdo ***responde*** ao tamanho da tela atual.
- geralmente os designers começam pelo design do mobile (`mobile-first`).
  - posteriormente vão definindo comportamentos de elementos específicos quando em resoluções maiores ou menores.
- ***vantagens***:
  - é a mais fácil.
  - exige menos tempo de implementação.
  - traz benefícios para o SEO do site (Search Engine Optimization, ou otimização de mecanismos de busca).
- ***desvantagens:***
  - possibilita menos controle sobre o design da sua página e imagens fixas, como banners e afins
  - dependendo da resolução, o tempo de carregamento da página mobile pode sofrer um pouco.

### B) Design Adaptativo:
- detecta tamanhos de tela predefinidos, e demonstra o layout criado especificamente para a dimensão atual.
  - os tamanhos de tela mais comuns são: 320, 480, 760, 960, 1200 e 1600 pixels de largura.
- ***vantagens:***
  - possibilita um controle maior sobre o design do seu produto digital.
  - e, na teoria, proporciona uma experiência melhor para cada resolução definida, pois cada resolução possui uma composição de elementos personalizada e mais relevante ao contexto de uso.
- ***desvantagens:***
  - esforço de design necessário para elaborar cada versão e na otimização do SEO da página, pois os mecanismos de busca identificam conteúdos duplicados no código.

### C) Versão específica para o mobile:
- pode ser acessada por uma url diferente (geralmente m.urldoseusite.com).
- apesar dos benefícios ao tempo de carregamento da página, essa abordagem ***acabou caindo em desuso***, pois exige maior manutenção (precisaria alterar pelo menos dois códigos diferentes em caso de alterações: uma na versão desktop e outra na versão mobile).

--- 

<div align="center">

## Mãos à obra!

</div>

- utilizado [Figma](https://www.figma.com/).
  - on-line e possibilita compartilhamento com outros usuários.
- abordagem responsiva.

## Criar um novo arquivo

1. Criar uma conta grátis no Figma.
2. Tela inicial > menu lateral > clicar no ícone de adicionar um novo arquivo **ou** botão de mais junto à Drafts **ou** no botão “New design file”.
3. Clicar no título do arquivo ("Untitled" ou "Sem título") > renomear para "Fintech".

## Estrutura da ferramenta

1. Na barra superior, à esquerda, há o acesso ao menu do site, ferramentas para criar e inserir elementos às suas telas e a possibilidade de inserir comentários nas telas já criadas (interessante ao lidarmos com um projeto em equipe ou para fazer anotações pessoais).

2. No lado direito do cabeçalho, podemos ver quem está visualizando o arquivo naquele momento e compartilhar o arquivo completo ou uma tela específica com alguém. Consegue também ver suas criações em forma de protótipo ao clicar no ícone "Play" da barra e, por fim, alterar o zoom da tela.

3. Na coluna esquerda aparecem listadas as camadas e componentes criados. No centro ficam as telas do app ou site, e a coluna da direita demonstra os atributos que você pode alterar nos elementos, assim como configurações de prototipação e o inspetor de códigos CSS, criados automaticamente pelo Figma.

## Inserir um frame

1. Na barra de ferramentas, selecionar a opção de inserir um frame.
2. Na coluna da direita, vão aparecer diversas opções de tamanhos de tela, referentes a dispositivos existentes no mercado.
3. Selecione o tamanho do iPhone SE, que possui 320 pixels de largura.
4. Para renomear o frame, basta clicar sobre o item na lista de layers (camadas) da coluna esquerda.

## Inserir e ajustar elementos

1. Clique no ícone quadrado da barra superior de ferramentas. Ali, você encontra várias opções de elementos para inserir em sua tela.
2. Selecione a opção de retângulo e crie um no seu frame. 
3. Com o retângulo selecionado, na coluna da direita aparecerão atributos que você pode alterar no elemento. 
    - Para certificar-se de que o tamanho ficará exatamente como queremos, insira no campo W (de width, ou largura) o número 320. Já no campo H (de height, ou altura, em inglês), insira 64.
4. Nos campos X e Y você consegue alterar a posição do elemento em seus eixos horizontal e vertical.
    - No campo X, insira o número 0.
5. Com a tecla SHIFT do seu teclado pressionada, arraste o retângulo até a parte inferior do frame.
6. Selecione a ferramenta que possui a letra T como ícone, clique em qualquer lugar do seu frame e digite "Adicionar Serviço".
    - Nas configurações que aparecerão na coluna da direita, altere o tamanhodo texto para 20 pontos e deixe-o centralizado.
    - Arraste o texto para cima do retângulo, de forma que ele fique centralizado tanto vertical quanto horizontalmente. 
    - Atenção: verifique se a camada do texto está em cima da camada do retângulo, na lista de layers da coluna esquerda. Caso contrário, o texto vai desaparecer da tela.
7. Se quiser ter certeza de que os elementos estão alinhados, selecione as duas camadas na coluna esquerda e clique nas opções de alinhamento localizadas na coluna da direita.

## Componentes

- é a possibilidade de criar um  elemento padrão a ser replicado em locais diferentes e de forma inteligente: se alterar em um lugar, todas as áreas que contêm aquele componente sofrerão a mesma alteração!

1. Selecione as duas layers criadas: o texto "Adicionar Serviço" e o retângulo. 
2. Em seguida, navegue até o ícone do menu principal, acesse o submenu Object e clique em Create Component.
    - o componente vai ficar listado sempre na coluna esquerda, na aba "Assets" (ativos, em inglês). 
    - para todas as próximas telas que quiser que tenham o botão de adição de serviço, basta arrastar o item da lista e inseri-lo onde deseja!

---

<div align="center">

## Criar a tela

</div>

> O modelo estudado pode ser visualizado [aqui](https://www.figma.com/file/A5ohuwoYD8WDboz2j0APsy/Capitulo08?node-id=0-1&t=Gzxsyw6PFaJMLwBj-0).

## Ícone de informação

1. Criar uma coluna de ação para a tela, com ícone de informação e texto "INFO".
2. É possível criar específicos para cada ícone e inseri-los no componente principal das ações (um dentro do outro).

## Componentes replicados

- quanto aos componentes, é possível replicá-los e evitar retrabalho em caso de alterações, além de editar conteúdos e estilo de itens replicados, como texto, cor e estilo de texto.
- se fizer uma alteração em um componente inserido a partir do original, essa mudança ficará visível apenas onde a fizer. Mas, se o ajuste ocorrer no elemento original, a alteração será replicada em todos os demais.

## Elementos responsivos

- ferramenta Constraints, ou restrições, em inglês.
- funciona com base em eixos de posição, considerando vertical e horizontal. 
  - você define limites de posicionamento para aquele elemento e por onde seu eixo deverá se guiar. 
  - opera com os mesmos princípios do atributo Position, da linguagem CSS.
- principais resoluções:
  - 480 x 730, 780 x 1024, 1280 x 720, 1600 x 1000.

## Visualizando no protótipo

- selecionar o frame desejado e clicar no ícone de “Play”, o botão ”Present”, localizado no canto superior direto do cabeçalho.

---

## FAST TEST

### 1. Selecione a alternativa que contém a definição de "Design Responsivo":
> Essa forma é a mais fluida, pois o conteúso responde ao tamanho de tela atual. Os elementos da interface se moverão para se encaixarem dinamicamente ao formato escolhido.

### 2. Sobre o conceito de "mobile-first", selecione a afirmação correta:
> Os designers começam pelo layout mobile para depois aumentarem para resoluções maiores.

### 3. Esta afirmação "Nossa mente vê os pontos conectados" se refere a qual lei?
> Lei de continuidade.

---

## Atividade para nota:

"Muito bem, fizemos a primeira tela juntos, agora é sua vez! Com toda sua criatividade e respeitando as boas práticas do design de interface, crie as demais telas da Fintech e envie para nós na área de atividades!<br>
Mas atenção para as regras:<br>
- Envie suas telas em um formato .pdf
- Você deverá criar no mínimo 4 telas e no máximo 6.
- Utilize a sua criatividade e os recursos que você aprendeu da ferramenta."

> Minha resolução para a atividade pode ser visualizada [aqui](https://www.figma.com/file/aqY65Gf6OafWQ0t3Ctmaut/Fintech?node-id=0%3A1&t=hiZK35mYFXi6CQQe-1).

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)
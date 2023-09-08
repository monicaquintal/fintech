<div id="fase05" align="center">
<h1>FASE 5 - OOP</h1>
<h2>Capítulo 10: O que são os Chatbots?</h2>
</div>

<div align="center">
<h2>1. O QUE SÃO OS CHATBOTS?</h2>
</div>

- chatbots surgiram como ferramentas que revolucionam a forma como humanos interagem com sistemas de computador.
- esses agentes de conversação inteligentes simulam conversas semelhantes às humanas, fornecendo uma interface perfeita e eficiente entre os usuários e a tecnologia.

> `Chatbot` consiste em um programa de computador projetado para simular conversas com usuários humanos, especialmente pela internet.

### Conceitos importantes: 

1. no coração dos chatbots está o `Processamento de Linguagem Natural` (Natural Language Processing, ou NLP), um campo da Inteligência Artificial que permite que as máquinas entendam e processem a linguagem humana.
  - ao empregar técnicas como tokenização, marcação de parte da fala, reconhecimento de entidade, análise de sentimento e reconhecimento de intenção, os chatbots podem compreender as mensagens do usuário e extrair significado delas.

2. `gerenciamento de diálogo`: envolve manter o contexto das conversas, rastrear o estado atual e decidir as respostas apropriadas.
  - os chatbots se beneficiam dos ciclos de feedback do usuário, aprendendo e melhorando continuamente com base nas informações que recebem.

3. `técnicas de Machine Learning`: desempenham papel vital no desenvolvimento do chatbot. 
- o **aprendizado supervisionado** utiliza dados rotulados para treinar chatbots, permitindo que eles entendam e gerem respostas apropriadas.
- o **aprendizado não supervisionado** permite que os chatbots extraiam padrões e estruturas de dados não rotulados, aprimorando suas habilidades de conversação.
- o **aprendizado por reforço** capacita os chatbots a otimizar seu comportamento por meio de tentativa e erro, conduzido por algoritmos de aprendizado baseados em recompensas.
- a **transferência de aprendizado** aproveita o conhecimento pré-existente ou modelos pré-treinados para melhorar o desempenho do chatbot em domínios específicos.

4. `técnicas de geração de respostas`: 
- **sistemas baseados em regras** utilizam regras e padrões predefinidos para analisar a mensagem e gerar uma resposta para o usuário.
- **modelos baseados em recuperação** selecionam respostas predefinidas apropriadas de um banco de dados, com base na entrada e no contexto.
- **modelos generativos** selecionam respostas empregando técnicas de geração de linguagem natural e modelos de aprendizado profundo, como redes neurais recorrentes (RNNs) ou transformadores, geram respostas do zero, resultando em conversas mais dinâmicas e criativas.

### Propósito dos chatbots:

- se destacam no suporte e assistência ao cliente, fornecendo um serviço rápido e consistente.
- podem recuperar informações, oferecer recomendações, automatizar tarefas, integrar-se a sistemas e APIs e até iniciar vendas.
- atuam como assistentes virtuais, ajudam no aprendizado de idiomas, coletam e analisam dados valiosos do usuário e entretêm os usuários por meio de experiências interativas.

> Considerações éticas são de suma importância ao projetar e implantar chatbots. O viés nos dados de treinamento, as preocupações com a privacidade, a transparência e a responsabilidade devem ser cuidadosamente tratadas para garantir interações justas e responsáveis.

## 1.1 Chatbots e assistentes virtuais

- `chatbots` e `assistentes virtuais` envolvem a interação com os usuários por meio de conversas, PORÉM atendem a propósitos distintos e têm recursos diferentes!

<div align="center">

Tópico | Chatbots | Assistentes Virtuais
:-------:|---------|-----------
**Escopo e funcionalidade** | - projetados para realizar tarefas específicas ou fornecer informações dentro de um domínio ou contexto predefinido.<br>- normalmente têm foco estreito e são programados para responder a consultas ou comandos do usuário com base em regras ou algoritmos predefinidos.<br>- costumam ser usados para automatizar o suporte ao cliente, fornecer informações básicas ou auxiliar em tarefas específicas. | - são mais abrangentes em suas funcionalidades.<br>- são projetados para auxiliar os usuários em uma ampla gama de tarefas e fornecer experiências personalizadas.<br>- são capazes de entender as entradas de linguagem natural, interpretar o contexto e executar ações complexas.<br>- podem executar tarefas como definir lembretes, marcar compromissos, fornecer recomendações, realizar pesquisas na Web e integrar-se a vários aplicativos e serviços.
**Interatividade e habilidades de conversação** | - se envolvem principalmente em conversas baseadas em texto e geralmente são implementados em plataformas de mensagens, sites ou aplicativos móveis.<br>- se concentram em fornecer respostas rápidas e eficientes às consultas dos usuários. | - projetados para se envolver em conversas mais interativas e dinâmicas.<br>- podem lidar com entradas de linguagem natural, entender a intenção do usuário e responder de maneira conversacional. <br>- geralmente possuem recursos de reconhecimento e síntese de fala, permitindo que os usuários interajam com eles por meio de comandos de voz.
**Contexto e personalização** | - geralmente operam dentro de um contexto ou domínio específico.<br>- são treinados / programados para responder a tipos específicos de consultas ou comandos.<br>- suas respostas geralmente são baseadas em regras ou padrões predefinidos. | - focam na compreensão e adaptação ao contexto do usuário.<br>- podem se lembrar de interações anteriores, manter o contexto durante uma conversa e fornecer respostas personalizadas com base nas preferências e no histórico do usuário.<br>- utilizam algoritmos de Machine Learning e dados do usuário para melhorar continuamente sua compreensão e capacidade de fornecer experiências personalizadas.
**Integração e suporte de plataforma** | - geralmente são integrados a plataformas ou aplicativos específicos, como aplicativos de mensagens, sites ou sistemas de suporte ao cliente.<br>- geralmente são projetados para lidar com casos de uso ou tarefas específicas nessas plataformas. | - projetados para serem mais versáteis e podem ser integrados em várias plataformas e dispositivos.<br>- podem ser acessados por meio de dispositivos ativados por voz, aplicativos móveis, alto-falantes inteligentes ou até mesmo incorporados a outros aplicativos.<br>- visam fornecer uma experiência unificada e consistente em diferentes canais e plataformas.

</div>

> Em resumo, chatbots são orientados a tarefas, operam dentro de um escopo definido e fornecem respostas rápidas às consultas do usuário. Os assistentes virtuais oferecem funcionalidades mais amplas, são capazes de se envolver em conversas interativas e fornecer experiências personalizadas em várias plataformas e dispositivos.

## 1.2 Mercado brasileiro de chatbots

- chatbots de suporte ao cliente lidam com um grande volume de consultas, reduzindo tempos de resposta e fornecendo assistência 24h/dia, o que leva a maior satisfação e retenção do cliente.
- também desempenham papel crucial em vendas e marketing. Ao se integrar com sistemas de back-end e APIs externas, automatizam tarefas como geração de leads, recomendações de produtos e até mesmo iniciam transações de vendas. Isso aumenta o engajamento do usuário e as taxas de conversão.

## 1.3 Como funciona um chatbot?

- chatbot é um programa de computador inteligente projetado para interagir com os usuários por meio de conversas, simulando a comunicação humana.
- nos bastidores, chatbots utilizam uma variedade de tecnologias e algoritmos para entender efetivamente as entradas do usuário, gerar respostas apropriadas e manter o fluxo da conversa.

1. Usuário interage com chatbot:
- a entrada (texto ou voz) é recebida e processada.
- o processamento inicial envolve tarefas como tokenização, que divide a entrada em unidades significativas, como palavras ou caracteres, e normalização de texto para padronizar a entrada.

2. Compreensão de Linguagem Natural (Natural Language Understanding, ou NLU).
- emprega técnicas como reconhecimento de entidade nomeada, marcação de parte da fala e análise de sentimento para extrair informações relevantes da mensagem do usuário.

3. gerenciamento de diálogo:
- crucial para manter contexto e gerenciar conversa.
- envolve rastrear o histórico da conversa, entender o estado atual da interação e lidar com a troca de turnos entre o chatbot e o usuário.
- políticas de diálogo definem o comportamento e as respostas do chatbot com base no contexto, na entrada do usuário e nos recursos do sistema.

4. depois que a entrada do usuário é compreendida e a intenção é identificada, o chatbot gera uma resposta.=, o que pode ser feito através de diferentes abordagens.
- sistemas baseados em regras usam regras e padrões predefinidos para corresponder às mensagens do usuário e fornecer respostas correspondentes.
- modelos baseados em recuperação acessam respostas pré-existentes de um banco de dados, selecionando a mais adequada com base na entrada e no contexto.
- modelos generativos, muitas vezes aproveitando técnicas de aprendizado profundo, geram respostas do zero, produzindo respostas dinâmicas e sensíveis ao contexto.

5. a resposta gerada é formatada e entregue ao usuário, geralmente em formato de texto, podendo ter recursos de viz e conveter a resposta em fala.

### Importante:

- chatbots também podem aprender e melhorar com o tempo.
- sobre o feedback do usuário:
  - ***feedback explícito***: inclui avaliações ou comentários diretos do usuário. 
  - ***feedback implícito***: derivado do comportamento do usuário e dos padrões de engajamento. 
- algoritmos de Machine Learning podem ser empregados para treinar o chatbot usando dados rotulados ou para reforçar seu comportamento por meio de aprendizado baseado em recompensa.

## 1.4 Tipos de chatbot

- podem ter respostas pré-programadas, utilizar Inteligência Artificial ou os dois.
- há pelo menos quatro tipos de chatbot: chatbot com base em botões, chatbot com base em reconhecimento de palavra-chave, chatbot contextual e voicebot.

1. `chatbots baseados em botões`:
- considerados os mais simples. 
- nesse modelo, não há a necessidade de treinar a IA, pois em vez de abrir espaço para que o usuário digite uma frase ou dúvida, o chatbot disponibiliza uma lista de opções e o usuário clica em uma das disponíveis.
- o usuário é conduzido pelas opções que o chatbot lhe fornecerá.

2. `chatbots baseados em reconhecimento de palavra-chave`:
- há possibilidade de o usuário escrever uma mensagem para a máquina. 
- esse tipo utiliza uma IA que busca identificar as palavras-chave para entender a mensagem do usuário e responder apropriadamente.
- mesmo atendendo bem algumas demandas, esse tipo de chatbot pode encontrar certos problemas de redundância em razão do uso das mesmas palavras-chave para mais de uma resposta diferente. 
- portanto, é comum que as empresas utilizem um chatbot híbrido, que une um chatbot com botões com um chatbot que utiliza reconhecimento de palavras-chave, ou que construam um chatbot contextual.

3. `chatbot que trabalha no modelo contextual`:
- é o mais avançado dos três.
- conta com o uso de Inteligência Artificial, com Machine Learning (ML), para treinar um modelo de conversação que busca sempre o seu aperfeiçoamento à medida que vai interagindo com mais usuários. 
- uma de suas características é permitir ter uma resposta diferente para a mesma pergunta em momentos diversos da conversa (contexto).

4. `voicebot`:
- permite explorar ainda mais o modelo contextual,mas com toda a interação sendo realizada por voz, como é o caso da Siri.

## 1.5 Grande Modelos de Linguagem (Large Language Models, ou LLM):

- são um tipo de modelo de IA que pode entender e gerar texto semelhante ao humano com base em padrões e exemplos de grandes quantidades de dados de treinamento.
- esses modelos revolucionaram as tarefas de processamento de linguagem natural, incluindo o desenvolvimento de chatbots, fornecendo uma ferramenta poderosa para gerar respostas contextualmente relevantes e coerentes.
- exemplo: GPT-3 da OpenAI.
- são projetados para entender semântica, sintaxe e contexto do texto, permitindo que gerem texto altamente semelhante ao conteúdo gerado por humanos.
- esses modelos são treinados em diversos conjuntos de dados da Internet, incluindo livros, artigos, sites e outras fontes textuais. Ao aprender padrões a partir dos dados, podem prever a probabilidade de uma palavra ou frase, dado o contexto em volta, permitindo-lhes gerar respostas contextualmente apropriadas.
- os `chatbots podem se beneficiar dos LLMs de várias maneiras`:

1. ***geração de resposta***: 
- LLMs se destacam na geração de texto; podem gerar respostas dinâmicas e sensíveis ao contexto, melhorando as habilidades de conversação dos chatbots.
- LLMs podem receber mensagens do usuário, entender sua intenção e gerar respostas coerentes e relevantes que imitam a conversa humana.

2. ***compreensão da linguagem natural***: 
- LLMs podem auxiliar nas tarefas de Compreensão da Linguagem Natural (NLU), extraindo informações e compreendendo o significado das mensagens do usuário.
- ao treinar em grandes quantidades de dados de texto, os LLMs podem desenvolver uma compreensão profunda dos padrões de linguagem e usar esse conhecimento para interpretar as entradas do usuário com precisão.

3. ***expansão de conteúdo***:
- LLMs podem aprimorar a base de conhecimento dos chatbots, fornecendo informações adicionais ou detalhes sobre tópicos específicos.
- podem recuperar e resumir informações de grandes quantidades de texto, permitindo que os chatbots forneçam respostas mais abrangentes às consultas dos usuários.

4. ***personalização da geração de linguagem***: 
- LLMs podem ser ajustados ou condicionados em conjuntos de dados ou domínios específicos para adaptar seus recursos de geração de linguagem.
- permite que os desenvolvedores do chatbot adaptem as respostas geradas pelos LLMs para corresponder ao estilo, tom ou requisitos específicos do domínio.

5. ***suporte multi-idiomas***:
- LLMs são treinados em diversas fontes de texto, tornando-os capazes de lidar com vários idiomas. 

### Importante:

- LLMs ofereçam benefícios significativos, porém possuem `limitações`:
  - podem gerar respostas plausíveis, mas incorretas ou tendenciosas, se os dados de treinamento contiverem vieses ou imprecisões. 
  - podem produzir respostas muito detalhadas, repetitivas ou sem coerência.
  - integração cuidadosa e ajuste fino são necessários para mitigar essas limitações e garantir que o desempenho do chatbot esteja alinhado com as expectativas do usuário.

## 1.6 Mitos e verdades

### 1.6.1 Chatbots irão destruir empregos

- (pior que é verdade) chatbots podem se tornar a primeira linha de atendimento ao cliente, seja por texto ou voz.
- porém nem sempre um chatbot vai resolver 100% o problema do cliente.
- dessa forma, é comum ter uma segunda e uma terceira linha de atendimento, que são feitas por profissionais da área de atendimento.
- ou seja, o conhecimento e as habilidades não são perdidos, eles são aproveitados em novas funções (como trinar os chatbots).

### 1.6.2 Chatbots podem entender e responder a qualquer pessoa de forma precisa

- falso, há casos em que podem ter problemas com entradas de usuário ambíguas ou contextualmente complexas.
- chatbots exigem treinamento e aprimoramento contínuos para aprimorar sua compreensão e precisão de resposta.

### 1.6.3 Chatbots são apenas apropriados para grandes empresas

- falso, a tecnologia de chatbot tornou-se mais acessível e empresas de todos os tamanhos podem se beneficiar.
- há várias plataformas, estruturas e ferramentas de desenvolvimento de chatbot disponíveis que atendem a diferentes orçamentos e requisitos.

### 1.6.4 Chatbots são caros e complexos para desenvolver

- falso, há soluções de chatbot mais simples, que são econômicas e fáceis de usar.
- há diversas plataformas que fornecem estruturas de desenvolvimento de chatbot, modelos pré-construídos e interfaces intuitivas que simplificam o processo.

### 1.6.5 Chatbots são apenas úteis no suporte ao cliente

- falso, chatbots podem ser empregados para geração de leads, vendas e marketing, acesso às informações, assistentes pessoais, aprendizado de idiomas, entretenimento etc.

### 1.6.6 Chatbot não pode ser o produto principal

- falso, em vez de criar um novo site ou aplicativo, as empresas podem criar um chatbot. 
- atualmente, qualquer profissional consegue criar o seu próprio chatbot e disponibilizar um MVP (Minimum Viable Product, ou Produto Mínimo Viável) sem muitos custos, podendo chegar a custo zero nos primeiros meses de operação.
- o mais importante é estar disponível onde os usuários já estão, como no caso do WhatsApp, instalado em 99% dos smartphones em operação no Brasil, segundo a Mobile Time.

### 1.6.7 Todos os chatbots utilizam IA

- falso, nem todos os projetos precisam de um chatbot que permita ao usuário digitar qualquer frase ou texto. 
- se estiver trabalhando em um chatbot que funciona como um formulário, é possível usar um modelo híbrido, com perguntas de múltipla escolha (chatbot baseado em botões) e abrir o campo de texto somente para pedir um dado mais específico, como número do CPF ou CEP,por exemplo. 

### 1.6.8 Todos os chatbots aprendem sozinhos

- falso, o chatbot necessita de uma pessoa ou de um time para fazer a curadoria do conteúdo, para que seja mais assertivo em suas respostas.

### 1.6.9 Todos os chatbots são os mesmos?

- falso, cada chatbot tem um escopo e um objetivo diferente,o que já os torna diferentes um do outro. 
- quando você define um público-alvo, canais de comunicação (como WhatsApp e Instagram) e cria uma brand persona (uma pessoa fictícia que representa a marca), o chatbot se torna único no mercado. 

## 1.7 Experiência do cliente, métricas e dados

- `Customer Experience` (ou Experiência do Cliente): conjunto de percepções e impressões que o cliente tem sobre a experiência de uma empresa. 
- é importante que sejam coletados dados, e que exista um profissional para analisar as métricas (Cientista de Dados).

## 1.8 Profissionais no mercado de chatbot

### 1.8.1 UX Writer (User Experience Writer)

- profissional responsável por elaborar o conteúdo conversacional e a experiência do usuário do chatbot.
- especializados no uso eficaz da linguagem para criar interações envolventes e significativas entre usuários e chatbots.
- desempenham papel crucial na formação da personalidade, tom e experiência geral do usuário.
- deve garantir que a linguagem do chatbot alinhe-se com a voz da marca e às expectativas do usuário.
- benefícios que um escritor de UX traz para o produto chatbot:
  - comunicação clara e concisa.
  - elaborando conversas envolventes.
  - estabelecendo a voz e a personalidade da marca.
  - empatia e abordagem centrada no usuário.
  - aprimorando o envolvimento e a retenção do usuário.
  - personalização e localização da linguagem.

### 1.8.2 UX Designer (User eXperience Designer)

- nas interfaces conversacionais (chatbots), o profissional tem o papel de desenhar o fluxo da conversa, seguindo dois caminhos diferentes: o caminho previsto e o caminho imprevisto.
  - caminho previsto: acontece quando o chatbot afunila as opções do usuário e costuma guiá-lo até atingir um determinado objetivo.
  - caminho imprevisto: acontece nos momentos em que se inicia a conversa com um campo aberto, o usuário pode digitar o que quiser.
- além de desenhar fluxos de conversas, também deve minimizar o impacto negativo quando um assunto não suportado é abordado, seja porque não pertence ao escopo do chatbot ou porque a ferramenta ainda não foi treinada para essa versão.

### 1.8.3 VUI Designer (Voice User Interface)

- especializado na criação de um design de interação de voz perfeito e intuitivo para aplicativos de chatbot.
- foco em otimizar a experiência do usuário por meio de interações de voz, permitindo que os usuários interajam com o chatbot usando linguagem natural e comandos de voz.
- principais aspectos e benefícios:
  - projetando interações de linguagem natural.
  - reconhecimento e compreensão de fala.
  - persona de voz e branding.
  - integração de design multimodal.
  - tratamento de erros e feedback.
  - síntese e entrega de fala.
  - teste e iteração do usuário.
  - considerações de acessibilidade.

### 1.8.4 Desenvolvedor

- dá vida ao chatbot, construindo e implementando sua tecnologia e funcionalidade. 
- são especializados em desenvolver e programar a infraestrutura de back-end do chatbot, integrando APIs e plataformas e garantindo operações suaves e eficientes.
- principais aspectos e benefícios:
  - desenvolvimento de back-end.
  - integração com APIs e plataformas.
  - IA e Machine Learning.
  - melhoria e manutenção contínuas.
  - escalabilidade e otimização de performance.
  - segurança e privacidade de dados.
  - colaboração com outras funções.
  - integração de terceiros.

### 1.8.5 Cientista de dados

- resonsável pelo aproveitamento de dados para melhorar desempenho, inteligência e experiência do usuário do chatbot.
- são especializados em extrair informações valiosas dos dados, aplicando análises estatísticas e técnicas de Machine Learning e usando modelagem preditiva para aprimorar os recursos do chatbot.
- principais aspectos de sua função e benefícios:
  - análise e pré-processamento de dados.
  - processamento de linguagem natural (NLP).
  - reconhecimento de intenção e extração de entidade.
  - modelagem de IA e Machine Learning.
  - personalização e criação de perfil de usuário.
  - aprendizado e melhoria contínua.
  - métricas e análises de desempenho.
  - colaboração com outras funções.

> Além dos perfis dos profissionais citados, existem outros papéis presentes em projetos de chatbot, mas com menos participação direta no desenho e na construção: Product Owner, Project Manager, UX Research, entre outros.

## 1.9 A tendência e a oportunidade

- o mercado de chatbots é dinâmico e em evolução, com várias tendências emergentes moldando sua trajetória nos próximos anos.
- tendências importantes a serem observadas:
  - IA conversacional.
  - chatbots habilitados para voz (voicebots).
  - chatbots multi-idiomas e multimodais.
  - personalização e reconhecimento de contexto.
  - integração com sistemas de negócios.
  - abordagem híbrida.
  - chatbots em aplicativos específicos do setor.
  - IA ética e responsável.
  - chatbots como assistentes virtuais.
  - aprendizado contínuo e autoaperfeiçoamento.

---

## FAST TEST

### 1. No cenário em rápida evolução da IA conversacional, dois termos que surgem com frequência são chatbots e assistentes virtuais. Embora ambos envolvam a interação com os usuários por meio de conversas, eles atendem a propósitos distintos e têm recursos diferentes. É essencial compreender as nuances dessas tecnologias para aproveitá-las efetivamente em vários contextos. Indique a alternativa que diz respeito à atuação dos assistentes Virtuais:
> Focam na compreensão e adaptação ao contexto do usuário. Eles podem se lembrar de interações anteriores, manter o contexto durante uma conversa e fornecer respostas personalizadas com base nas preferências e no histórico do usuário.

### 2. Identifique a alternativa que está incorreta em relação ao VUI designer:
> Se o caso de uso tiver o foco no uso em locais públicos, como durante o transporte em um ônibus ou metrô, o VUI pode ser adequado.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)
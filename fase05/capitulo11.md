<div id="fase05" align="center">
<h1>FASE 5 - OOP</h1>
<h2>Capítulo 11: Plataforma de Chatbots.</h2>
</div>

<div align="center">
<h2>1. PLATAFORMA DE CHATBOTS</h2>
</div>

- plataformas de chatbot são ferramentas de software ou frameworks que fornecem aos desenvolvedores as ferramentas, recursos e infraestrutura necessários para criar, implementar e gerenciar chatbots.
- as plataformas oferecem diversas funcionalidades, como processamento de linguagem natural (NLP), suporte para múltiplos canais de comunicação, análises e integrações, simplificando o processo de desenvolvimento e aprimorando o desempenho dos chatbots. 
- com interfaces fáceis de usar, modelos pré-construídos e funcionalidade de arrastar e soltar, as plataformas de chatbot permitem que os desenvolvedores, independentemente de sua experiência em codificação, criem chatbots com eficiência.

### Benefícios do uso de plataformas de chatbot:

- facilidade de desenvolvimento.
- suporte multicanais.
- processamento de linguagem natural (NLP).
- capacidades de integração com serviços, APIs e bancos de dados de terceiros.
- análise e insights.
- escalabilidade e desempenho.
- manutenção e atualizações.
- comunidade e suporte.

### Antes de mais nada...

- um projeto de chatbot é semelhante a um projeto de desenvolvimento de software. Antes de iniciar, é necessário definir alguns pontos para que se tenha o direcionamento correto ao longo da construção do projeto.
- é preciso definir:

1. O problema que você busca solucionar.
2. O tempo que será investido para resolver esse problema.
3. Definir as integrações necessárias.

- com essas informações, é possível definir a estratégia, a ferramenta e a tecnologia para construir o fluxo de conversação e trazer clareza quanto às métricas que serão necessárias para definir o grau de sucesso do projeto.
- ao participar de todo e qualquer projeto de chatbot, será necessário escolher:
  - os canais de comunicação (onde o chatbot vai interagir), 
  - a plataforma de integração e
  - a plataforma de IA e os frameworks de chatbots (framework pronto com inteligência artificial em um canal de comunicação?).

## 1.1 Recursos da Plataforma de Chatbot

- oferecem uma ampla gama de recursos e capacidades que capacitam os desenvolvedores a criar agentes de conversação sofisticados e inteligentes.
- as plataformas servem como kits de ferramentas abrangentes, fornecendo a infraestrutura e os recursos necessários para agilizar o desenvolvimento, a implementação e o gerenciamento de chatbots.
- principais recursos oferecidos:

1. `Processamento de Linguagem Natural (NLP)`:
- permite que os chatbots entendam e interpretem a entrada do usuário, extraiam significado e gerem respostas apropriadas.
- os algoritmos NLP lidam com tarefas como reconhecimento de intenção, extração de entidade e análise de sentimento, aprimorando a capacidade do chatbot de compreender as consultas do usuário e se envolver em conversas significativas.

2. `Suporte multicanais`:
- incluindo sites, aplicativos de mensagens, plataformas de mídia social e dispositivos habilitados para voz.

3. `gerenciamento de diálogo`:
- permitem que os desenvolvedores definam caminhos de diálogo, gerenciem as intenções do usuário e gerem respostas dinamicamente com base no contexto.

4. `construtores de interface visual`:
- interfaces de arrastar e soltar, que permitem o design de fluxos de conversação, prompts de usuário e modelos de resposta, simplificando o processo de criação.

5. `integração com serviço externos`:
- fornecem integrações com serviços externos e APIs, permitindo que os chatbots acessem e recuperem informações de bancos de dados, sistemas de CRM, plataformas de comércio eletrônico e outras fontes relevantes.

6. `recursos de aprendizado de máquina e IA`:
- podem incorporar recursos de aprendizado de máquina e IA, permitindo que os chatbots aprendam com as interações do usuário e melhorem com o tempo.
- podem fornecer recursos como classificação de intenção, reconhecimento de entidade e respostas com reconhecimento de contexto, capacitando chatbots para lidar com uma ampla variedade de consultas de usuários e se adaptar às mudanças nas necessidades dos usuários.

7. `análise e relatórios`:
- as plataformas geralmente incluem análises integradas e resursos de relatórios, que capturam dados sobre interações do usuário, métricas de engajamento, texas de conversão e satisfação do usuário.

8. `ferramentas de teste e depuração`:
- ferramentas que permitem que os desenvolvedores simulem as interações do usuário, validem os fluxos de diálogo e identifiquem e resolvam problemas ou bugs.
- ajuda a refinar a funcionalidade, a precisão e a experiência do usuário do chatbot.

9. `segurança e conformidade`:
- oferecem recursos como armazenamento seguro de dados, criptografia, autenticação de usuário e conformidade com regulamentações específicas do setor, como GDPR ou HIPAA.

10. `colaboração e controle de versão`.

## 1.2 Processo de Desenvolvimento de Chatbot

### 1. Definir os casos de uso:
- identificar a finalidade e os objetivos do seu chatbot.
- determinar os casos de uso ou cenários específicos em que será implantado.
- entender o público-alvo, suas necessidades e as tarefas nas quais o chatbot ajudará.

### 2. Projetar fluxos de conversação: 
- planejar a estrutura de conversação e os fluxos de diálogo do chatbot. 
- definir como o chatbot irá interagir com os usuários, antecipar diferentes intenções do usuário e mapear as etapas necessárias para atender a essas intenções.
- considerar os diferentes caminhos que uma conversa pode seguir com base nas respostas do usuário e criar um fluxo intuitivo e natural que oriente os usuários em direção aos resultados desejados.

### 3. Desenvolver processamento de linguagem natural (NLP): 
- implementar recursos de NLP para permitir que o chatbot entenda e interprete a entrada do usuário.
- envolve o treinamento de modelos de aprendizado de máquina para reconhecimento de intenção, extração de entidade e análise de sentimento. 
- utilizar bibliotecas e estruturas NLP para processar e obter significado das consultas do usuário, aprimorando a capacidade do chatbot de fornecer respostas precisas e contextualmente relevantes.

### 4. Criar gerenciamento de diálogo: 
- implementae um sistema robusto de gerenciamento de diálogo, envolvendo gerenciamento das intenções do usuário, rastreamento do histórico de conversas e garantia de transições suaves entre as diferentes partes da caixa de diálogo. 
- considerar o uso de técnicas como máquinas de estado ou sistemas baseados em regras para gerenciar a complexidade do diálogo de forma eficaz.

### 5. Integrar serviços externos: 
- pode incluir a integração com APIs para recuperar informações de bancos de dados, acessar serviços de terceiros ou executar tarefas específicas. 

### 6. Testar e validar:
- realizar testes de unidade para validar componentes individuais.
- conduzir testes de integração para verificar a comunicação perfeita entre diferentes módulos.
- realizar testes de usuário para coletar feedback e identificar áreas de melhoria. 
- usar estruturas e ferramentas de teste para simular as interações do usuário e avaliar o desempenho do chatbot em diferentes cenários.

### 7. Implantar e monitorar: 
- implantar o chatbot nas plataformas ou canais de comunicação desejados, como sites, aplicativos de mensagens ou dispositivos habilitados para voz. 
- monitorar o desempenho do chatbot, as interações do usuário e as métricas de engajamento para reunir insights e identificar áreas para otimização.
- analisar continuamente o feedback do usuário e adaptar o chatbot com base nas necessidades e preferências do usuário.

### 8. Iterar e melhorar: 
- o desenvolvimento do chatbot é um processo iterativo. 
- reunir continuamente o feedback do usuário, analisar o comportamento do usuário e medir as métricas de desempenho. 
- usar essa abordagem baseada em dados para identificar áreas em que o chatbot pode ser aprimorado, como refinar fluxos de diálogo, melhorar modelos de NLP ou incorporar recursos adicionais.
- atualizar e iterar regularmente para garantir sua relevância e eficácia ao longo do tempo.

## 1.3 Canais de comunicação

- a escolha sempre deve estar baseada no seu cliente, em quem vai utilizar o chatbot.
- segundo a pesquisa "Mensageria no Brasil 2023", feita pelo Panorama Mobile Time, no Brasil, o WhatsApp é o aplicativo mais popular e está presente em 99% dos smartphones brasileiros. O Instagram está logo atrás, com 81%, seguido pelo Facebook Messenger (74%), o Telegram (45%) e, por fim, o Signal (12%).
- uma tendência para os próximos anos é o aumento do uso de alto-falantes inteligentes, também conhecidos como Smart Speakers. 

## 1.4 Plataformas de integração

- são ferramentas que facilitam o lançamento de um chatbot em um ou mais canais de comunicação, reduzindo o tempo de Go-to-Market. 
- as principais plataformas (no quesito Market share) disponibilizam uma ferramenta para criar o chatbot sem a necessidade do treinamento de IA.
- a necessidade de utilizar uma plataforma de integração se deve ao fato de as demandas estarem sempre crescendo e mudando, e em razão do processo burocrático para publicar um chatbot nas principais plataformas, em especial, nas plataformas do Facebook (Messenger, WhatsApp e Instagram). Por isso empresas e desenvolvedores optam por usar esse tipo de plataforma para publicar um chatbot em questão de minutos.

> No Brasil, as plataformas mais utilizadas são: `Chatfuel`, `Manychat`e `Take Blip`, sendo a Take Blip é a única plataforma de uma empresa brasileira.

### a) Chatfuel:
- é uma plataforma de integração que permite a criação do chatbot por meio da ferramenta de construção de fluxo de conversa, com ou sem uso do mecanismo de IA próprio da plataforma.
- é possível enquadrar o Chatfuel como uma plataforma de IA, por conta do seu motor de NLP disponível.
- disponibiliza uma lista de templates com exemplos de conteúdo para que o usuário possa iniciar com um escopo predefinido.
- é possível realizar a integração com qualquer plataforma de IA comum a API, além de ser possível integrar somente no Facebook Messenger.
- a conta gratuita atualmente permite interação com até 50 perfis no Facebook Messenger.

### b) Manychat:
- é uma das maiores plataformas de integração do mundo. 
- possui uma estrutura para construir o chatbot com a ferramenta de criação de fluxos de conversa e permite integrar com uma plataforma de IA por meio de uma API. 
- disponibiliza uma grande variedade de templates gratuitos e pagos.
- possui grande variedade de integrações com os principais canais de comunicação, como Facebook Messenger, WhatsApp, Instagram, SMS e e-mail.
- disponibiliza a integração com outras plataformas e recursos, como Google Spreadsheet, Shopify, MailChimp, HubSpot, entre outros. 
- possui parceria como Facebook, possui acesso beta à API do WhatsApp e do Instagram.
- em seu plano gratuito, limita o acesso a 1000 usuários no chatbot e algumas funções estão restritas ao plano Pro.

### c) Take Blip:
- ferramenta de construção de fluxo de conversa.
- a plataforma **não possui um mecanismo próprio de IA**: disponibiliza uma integração nativa com as três principais plataformas de IA - IBM Watson Assistant, Microsoft LUIS e Dialogflow (Google).
- canais de comunicação: WhatsApp, Facebook Messenger, Telegram, SMS, e-mail, Blip Chat e Workplace Chat.
- possui um plano gratuito com o acesso a todas as funcionalidades. 

> A escolha entre uma dessas plataformas ou até outras não listadas varia de acordo com o escopo do projeto e o conhecimento do time que está trabalhando nele.

## 1.5 Plataformas de IA

- possuem como vantagem o uso da tecnologia de processamento de linguagem natural (Natural Language Understanding — NLP), o treinamento de um modelo de conversação por meio da tecnologia de Machine Learning (ou treinamento de máquina). Isso significa treinar uma máquina para ser capaz de responder a perguntas ou solicitações dos usuários que estão interagindo no chat.
- no momento em que se define o escopo do projeto de chatbot, escolher entre um dos quatro tipos de chatbots: chatbot com base em botões, chatbot com base em reconhecimento de palavra-chave, chatbot contextual e voicebot. 

### a) plataforma de Watson Assistant, da IBM:
- possui em sua estrutura principal de treinamento o uso de intenções, entidades e diálogo. 
  - intenção: objetivo do usuário ao mandar aquela mensagem. 
  - entidade: complemento da informação: duas frases podem ter a mesma intenção (objetivo), mas com entidades diferentes (complemento). 
  - diálogo: entra para criar a árvore de decisão.
- o usuário da plataforma agrupa frases de exemplos em intenções e define grupo de palavras ou termos na mesma entidade. No diálogo, define cada fluxo de conversa considerando a primeira pergunta do usuário do chatbot até a última resposta dada.
- disponibiliza outras funcionalidades como Webhook (chamada de API em um determinado momento da conversa para armazenar um dado ou buscar um dado em um banco de dados), Desambiguação (clarificar qual é a intenção real da frase), Analytics (análise de métricas), Versionamento e chat de teste.
- já disponibiliza algumas integrações com canais de comunicação, como página de Chat, Facebook Messenger, Slack, WhatsApp e Phone. 
- alguns canais de comunicação necessitam revisar o conteúdo do chatbot e receber dados da empresa ou desenvolvedor para posteriormente disponibilizar oficialmente, como Facebook Messenger e WhatsApp. 
- para ter acesso ao serviço, criar uma conta na IBM Cloud gratuitamente (sem a necessidade de inserir o cartão de crédito) e criar uma instância do Watson Assistant no plano litev(limite de 1000 usuários e 10.000 mensagens por mês).

### b) Dialogflow:
- trabalha com o modelo de intenção e entidade, para o treinamento dos exemplos que compõem a base do NLP. 
- conta com a funcionalidade de Webhook para possibilitar a chamada de API de dentro do próprio chatbot (seja para acesso de um dado externo ou para enviar um dado armazenado) e possui um chat de teste.
- integrações com Facebook Messenger, Workplace do Facebook, Hangouts Chat, LINE, Slack, Telegram e com integrações via código aberto, como Kik, Skype, Cisco Webex, Twitter, Viber e Twilio.
- na Google Cloud, você recebe um crédito de US$600 (seiscentos dólares) para usar em 12 meses na plataforma, incluindo o serviço de Dialogflow. Basta criar uma conta na nuvem da Google e inserir o cartão de crédito para ativar a conta e, na sequência, criar a instância do serviço do Dialogflow.

### c) LUIS (Language Understanding):
- possui a capacidade de utilizar a tecnologia de Machine Learning para treinar o modelo de intenção e entidade.
- a estrutura de treinamento é similar à do Watson Assistant e do Dialogflow, porém você não faz a configuração da árvore de decisão. 
- no final, o que o usuário tem é um JSON (JavaScript Object Notation) com os dados do texto do usuário, as intenções identificadas com a intenção com maior nível de confiança e a lista de entidades encontradas no texto. O usuário da plataforma que receber o JSON deverá construir a melhor resposta programaticamente, o que torna menos amigável para o público que não costuma programar esse tipo de serviço.
- a solução da Microsoft para o uso do LUIS é a integração com outro serviço, chamado Azure Bot Service, que possui uma ferramenta visual para construção do fluxo de conversa e utiliza o modelo do LUIS como base de treinamento para a construção do chatbot. 
- após publicação do chatbot, o usuário pode configurar uma página na Web, Microsoft Teams, Skype, Slack, Cortana, Facebook Messenger, Kik, Telegram, Slack e outros.
- possui um plano gratuito que contempla 1M de chamadas de API no seu modelo de intenção e entidade, e o Azure Bot Service possui o plano Standard, que disponibiliza mensagens ilimitadas gratuitamente. 
- para criar uma conta na Azure, é necessário inserir um cartão de crédito para ativar a conta e o usuário receberá R$670,00 (seiscentos e setenta reais) de crédito para usar nos primeiros 30 dias.

---

## FAST TEST

### 1. As plataformas de ChatBots oferecem um conjunto de funcionalidades e capacidades que simplificam o processo de desenvolvimento e melhoram o envolvimento do usuário. Com base nesta afirmação, selecione a alternativa incorreta.
> Capacidade de desenvolvimento de serviços em nuvem para que a base de dados do sistema esteja disponível de forma escalável e pronta para atendimento online.

### 2. No cenário em rápida evolução da IA conversacional, dois termos que surgem com frequência são chatbots e assistentes virtuais. Embora ambos envolvam a interação com os usuários por meio de conversas, eles atendem a propósitos distintos e têm recursos diferentes. É essencial compreender as nuances dessas tecnologias para aproveitá-las efetivamente em vários contextos. Indique a alternativa que diz respeito a atuação do chatbot.
> Geralmente operam dentro de um contexto ou domínio específico. Eles são treinados ou programados para responder a tipos específicos de consultas ou comandos. Embora alguns chatbots possam ter consciência contextual limitada, suas respostas geralmente são baseadas em regras ou padrões predefinidos.

### 3. Um projeto de chatbot é semelhante a um projeto de desenvolvimento de software. Antes de iniciar, é necessário definir alguns pontos para que se tenha o direcionamento correto ao longo da construção do projeto. Selecione a alternativa que indique um ponto que não deve ser realizado no início do projeto do chatbot.
> Medir a eficiência do atendimento.

### 4. Além do cenário citado de atendimento ao cliente, há outras finalidades para as quais as empresas utilizam o chatbot. Quais seriam?
> Vendas, apoio ao backoffice, cobrança e marketing.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)
<div id="fase06" align="center">
<h1>FASE 6 - MODEL</h1>
<h2>Capítulo 09: Chatbot com IBM Watson Assistant.</h2>
</div>

<div align="center">
<h2>1. CHATBOT COM IBM WATSON ASSISTANT</h2>
</div>

## 1.1 IBM Watson Assistant

- é um serviço de criação e treinamento de chatbots, muito utilizado por diversas empresas, como Bradesco/BIA e Magalu/Lu. 
- desempenha um papel fundamental no avanço da tecnologia de chatbot, aproveitando a evolução da IA, ML, NLP, IA Generativa e LLMs para oferecer às empresas uma solução de conversação sofisticada e eficiente.

### 1.1.1 Cenários:

- em alguns casos, não é possível entender o que o usuário quer dizer, porque o chatbot não possui conhecimento necessário para responder à pergunta (cenário chamado de `Long-tail`/cauda longa).
- como solução, considerar o uso de uma IA Generativa, com um `Large-Language Model (LLM)` para conhecimentos gerais, ou com um serviço, também da IBM Cloud, chamado de Watson Discovery (serviço com a capacidade de analisar dados não estruturados dentro de arquivos (HTML, Word, JSON e PDF) por meio de buscas).
- cenários de uso mais simples, que demandem somente o conteúdo treinado no chatbot, são classificados como `Short-tail` (ou cauda curta).

### a) `Short-tail`:
- projetados para lidar com um conjunto limitado de perguntas ou intenções bem definidas e frequentes. E
- fornecem respostas rápidas e concisas, muitas vezes com base em regras predeterminadas ou modelos simples de ML.
- objetivo: simplificar as interações comuns, como consultas de perguntas frequentes ou consultas básicas de suporte ao cliente.
- serviços de chatbot baseados em nuvem pública (como Watson Assistant e Amazon Lex) geralmente usam esse domínio devido à facilidade de implementação e economia.
- funcionam como assistentes virtuais eficientes para tarefas rotineiras, reduzindo a carga de trabalho dos agentes humanos e fornecendo respostas instantâneas e consistentes.

### b) `Long-tail`:
- voltados para lidar com uma ampla gama de consultas de usuários complexas e diversas. 
- contam com algoritmos NLP avançados, técnicas de aprendizado profundo (Deep Learning) e grandes modelos de linguagem (Large-Language Models) para compreender as complexidades da linguagem natural e abordar intenções mais específicas e variadas. 
- Dialogflow e Microsoft LUIS, oferecidos por provedores de nuvem pública, se destacam. 
- empresas que exigem chatbots para lidar com interações complexas, dar suporte a setores de nicho ou fornecer assistência detalhada preferem essas plataformas. 
- desempenham um papel vital ao oferecer experiências altamente personalizadas e personalizadas aos usuários, atendendo a um espectro mais amplo de necessidades e aumentando a satisfação do cliente.

> A distinção entre chatbots de cauda curta (Short-tail) e cauda longa (Long-tail) gira em torno do escopo e da complexidade das capacidades de conversação que eles possuem.

### 1.1.2 Sobre o Watson Assistant

- disponível no catálogo da IBM Cloud.
- oferece planos para que desenvolvedores, designers, startups e pequenas, médias e grandes empresas possam utilizar o serviço.
- tipos de planos disponíveis:

a) ***Lite***: 
- até 1.000 usuários ativos mensais únicos (métrica conhecida como MAU — Monthly Active Users) e 10.000 mensagens recebidas de forma gratuita por mês.
- é possível criar até 5 Skills diferentes (Dialog, Action ou Search) com até 100 nós de diálogo cada. 
- esse plano não expira, portanto pode ser utilizado por tempo indeterminado, respeitando os limites de uso.

b) ***Trial***:
- até 5.000 usuários ativos mensais únicos e 50.000 mensagens recebidas de forma gratuita por mês.
- funcionalidades disponíveis são iguais ao plano seguinte (plano Plus), porém tem 30 dias de acesso gratuito (depois será necessário inserir os dados de um cartão de crédito para subir de plano e continuar tendo acesso às funcionalidades).

c) ***Plus***: 
- acesso ilimitado ao número de usuários ativos mensais únicos e mensagens recebidas por mês.
- plano pago pelo volume de uso. 
- até 50 Skills por instância do serviço e não possui limite na quantidade de nós de diálogo.
- modelo de cobrança é feito pelo número de usuários únicos que interagem com o Watson Assistant durante o mês.

d) ***Enterprise***: 
- mesmos benefícios e modelo de cobrança que o Plus, com limite maior de Skills por instância (de 50 para 100 Skills).

e) ***Enterprise with data isolation***: 
- mesmos benefícios e modelo de cobrança que o plano Enterprise.
- acesso a um ambiente isolado para trabalhar com dados sensíveis (necessário para algumas indústrias, como a da Saúde).

## 1.2 Criação do seu serviço de chatbot

### 1.2.1 Criação de uma nova conta na IBM Cloud

1. Acessar a plataforma do [IBM Academic Initiative](https://www.ibm.com/academic) e clicar em Register now.
2. Na página seguinte, inserir seu e-mail e clicar no botão Submit.
3. Preencher os campos e inserir o código de confirmação que foi enviado para o seu e-mail.
4. Voltar para a tela de Log in novamente, inserir e-mail e senha. Caso seja solicitado a configuração da autenticação de dois fatores (2FA), você pode escolher a opção e-mail e inserir o mesmo e-mail usado no IBMid para receber o código de autenticação.
5. Desça até o tópico Most popular topics covered e clique no retângulo IBM Cloud > Desça até o tópico onde é possível ver as opções Courseware, Software e Resources. Clique no item Software e depois clique na seta azul no box IBM Cloud Feature Code.
6. Clicar no texto Request Feature Code e copiar o código que aparece logo depois do texto “Your IBM Cloud Promo Code is:". Este código de 16 caracteres é o Promocode que será necessário durante acriação e ativação da conta IBM Cloud.
7. Acesse a [plataforma IBM Cloud](https://cloud.ibm.com/login) e insira o seu e-mail FIAP no campo IBMid e clique no botão azul Continue. Digite a sua senha e clique no botão azul Log in.
8. Assim que acessar o painel principal da plataforma, um box irá aparecer. Clique no texto Register with a code e cole o seu Promocode.
9. Clique no botão azul Upgrade account e pronto! Sua conta agora está liberada para acessar uma camada gratuita de serviços, incluindo o Watson Assistant e o Node-RED.

### 1.2.2 Criação de uma nova instância de Watson Assistant

- `provisionar um serviço`: ação que faz com que você tenha uma “cópia” do serviço em sua conta e é com esta ação que permite que você possa configurar para atender a sua necessidade.

> Um exemplo que utilizaremos é com o serviço do Watson Assistant. Você provisionará uma instância, e criará um novo chatbot com uma base de treinamento próprio.

- para acessar o catálogo: 
  - a primeira opção é clicar no botão de “Catalog” no menu superior.
  - a segunda opção é clicar no botão azul de “Create resource”, no canto superior direito da tela e próximo da foto do seu perfil.
- na página de catálogo, buscar pelo serviço “Watson Assistant” na barra de pesquisa, abaixo da palavra “Catalog”. A
  - é possível filtrar pela categoria “AI / Machine Learning”.
  - clicar em cima do retângulo do serviço para ver mais detalhes do serviço e para provisionar na sua conta.
- na página de detalhes e provisionamento do serviço, neste caso, não há necessidade de mudar nenhuma informação, pois será provisionada uma instância na região de Dallas (us-south), plano gratuito e não fará modificação de nome da instância ou tags. 
- clicar no botão azul de “Create” para provisionar uma nova instância do serviço na sua conta.
- na página de detalhes da instância do serviço do Watson Assistant, você tem acesso a plataforma de treinamento do chatbot, a credencial (chave de API para realizar o acesso via API ou SDK), a visão do plano atual e documentação de como começar e das APIs disponíveis no serviço. Além disso, você consegue, no menu canto esquerdo, criar mais credenciais ou trocar o plano da sua instância. Para realizar a criação de um chatbot e treiná-lo, é necessário entrar na plataforma de treinamento. Para isso, clique no botão azul de **“Launch Watson Assistant”**.
- você cairá na página de “Welcome” e será induzido a criar um assistente (assistant), que utiliza funcionalidades que são provenientes da nova experiência do Watson Assistant. 
- o passo a passo desta aula será focado na experiência clássica, a mais utilizada pelas empresas. Para mudar para a experiência clássica, clicar no ícone do usuário, no canto superior direito, e clicar na opção “Switch to classic experience”. A plataforma vai solicitar confirmação da mudança e você clicará no botão azul de “Switch”. Você pode mudar para a nova experiência a qualquer momento, apenas realizando o mesmo procedimento e clicando na opção **“Switch to new experience"**.
- dentro da ferramenta de treinamento, você consegue enxergar dois itens no menu na lateral esquerda: Skills e Assistants.
  - `Skills`: base de conhecimento do seu chatbot; a Skill será o local onde realizará o treinamento do chatbot, incluindo frases para ensiná-lo a entender a mensagem dos usuários e também onde configurará as respostas dele. 
  - `Assistants`: conjunto de Skills, no qual você agrupa as bases de conhecimento em um único assistente. Você dá ao assistente virtual uma ou mais habilidades para poder lidar com os diversos cenários do seu cliente.

> **Skill** é o local de treinamento do chatbot, e o **Assistant** é a forma de unir as Skills e integrar nos canais de comunicação — e isso inclui a página Web tanto na opção de um pronto para colocar no HTML do seu site como a opção de ter um link de um chat para compartilhar com seus conhecidos para testar o conteúdo publicamente.

- Na prática:

1. na página inicial do Watson Assistant, com a experiência clássica, clicar no botão cinza de **“Create assistant”** para criar o assistente (assistant) que será utilizado para adicionar um novo Dialog Skill e será disponibilizado através de uma página na web. 
2. Na página de criação de um novo assistente, colocar o “Name” como “Pizzaria”, e deixar o campo “Description” vazio (nome e descrição do assistente servem apenas para localização). Clicar no botão azul de “Create assistant”. 
3. Uma vez criado, o assistente (assistant) pode integrar com um Action Skillou Dialog Skill, e um Search Skill. Nesta aula, utilizaremos o ***Dialog Skill***, que trabalha com o modelo de intenção, entidade e diálogo. Clique no botão azul de “Add dialog skill” para criar a base de treinamento do seu assistante (assistant).

- `Actions Skill`: 
  - oferece uma interface simples onde qualquer profissional pode construir um fluxo conversacional para o seu assistente seguir.
  - o complexo processo de criação de dados de treinamento ocorre atrás das cenas automaticamente.
- `Dialog Skill`: 
  - oferece um conjunto de editores para que você use para definir ambos os seus dados de treinamento e a conversa.
  - a conversa é representada como uma árvore de diálogo. 
  - você usa o editor de diálogo gráfico para criar uma espécie de script para o seu assistente ler quando ele interage com seus clientes.
  - a caixa de diálogo identifica os objetivos comuns do cliente que você ensina a reconhecer e fornece respostas úteis.
- `Search Skill`: 
  - alavanque informações de bases de conhecimento corporativo existentes ou outras coleções de conteúdo de autoria de especialistas no assunto para atender a consultas de clientes imprevistas ou mais sutis. 
  - para uma determinada consulta do usuário, usa o serviço IBM Watson Discovery para procurar uma fonte de dados de seu conteúdo de autoatendimento e retornar uma resposta.

## 1.3 Treinamento do seu chatbot

- na ***página de criação de um novo Dialog Skill***, você visualizará uma página de configuração geral da Dialog Skill. 
- nessa página, é possível criar uma Skill a partir de três formas diferentes: Create skill, Use sample skill e Upload skill:

  - `Create skill`: 
    - para criar um Dialog Skill do zero. 
    - é a opção que você utilizará com maior frequência nos novos projetos dentro da empresa.
  - `Use sample skill`: 
    - você pode usar um chatbot de exemplo, de serviço de atendimento ao consumidor (“Customer Care Sample Skill”), disponível na lista.
    - é um ótimo exemplo para aprender uma estrutura simples de um chatbot, com algumas funcionalidades implementadas, como Jump to e Skip user input na área de diálogo (na árvore de decisão).
  - `Upload skill`: 
    - você pode importar uma Skill já criada a partir de um arquivo JSON, gerado ao criar uma nova Skill e atualizado toda vez que você faz alguma alteração na Skill.
    - normalmente, você utiliza essa opção quando vai movimentar uma Skill de uma instância de Watson Assistant para outra, que pode ser por conta de uma atualização do seu ambiente produtivo, a partir do ambiente de testes ou quando você precisa resgatar uma versão antiga que está armazenada em um sistema de controle de versionamento, como Github ou Bitbucket.
  
- para este laboratório prático, você criará um chatbot de pizzaria.
- no Watson Assistant, para criar um novo Dialog Skill, é obrigatório definir dois campos: "Name” (para identificação) e “Language”. Opcionalmente, você pode escrever no campo descrição.
  - para o laboratório, nome “Pizzaria” e linguagem “Brazilian Portuguese”.
  - clicar em Create Skill.
- após a criação, será redirecionado para dentro da sua Skill a fim de fazer o treinamento. Você treinará três itens importantes: Intenção, Entidade e Diálogo (os três pilares do Watson Assistant):

  - `Intenção (ou Intent)`: 
    - considerado como propósito, objetivo.
    - analisar a frase dos usuários com o objetivo de entender “Qual o propósito dele(a) ao fazer essa pergunta?”.
    - aqui é onde você agrupa exemplos de frases a fim de poder analisar uma frase, não pelas palavras-chave, mas pelo contexto.
    - no caso da pizzaria, duas pessoas podem pedir pizza de maneiras diferentes. A partir disso, você colocará os dois exemplos em uma mesma intenção para mapear formas diferentes de pedir pizza e ensinar o Watson Assistant a entender que são formas diferentes para alcançar o mesmo objetivo.
  - `Entidade (ou Entity)`: 
    - considerado complemento da informação.
    - usado para diferenciar uma frase da outra. 
    - o mesmo usuário pode mandar duas mensagens, com a mesma intenção, com algo que diferencie uma frase da outra. Esse algo pode ser uma entidade. 
    - no contexto de pizzaria, uma entidade pode ser o sabor de uma pizza: a mesma pessoa pode pedir uma pizza em momentos diferentes e o sabor pode ser diferente. A entidade de sabor é o que diferenciará o custo de uma pizza para outra, por isso é necessário utilizar esse item.
  - `Diálogo (ou Dialog)`: 
    - é nesse ponto que você cria toda a árvore de decisão do Watson Assistant. 
    - você une a intenção com a entidade (se houver) e cria-se todo o fluxo de diálogo.

- logo na tela inicial, ***treinar o primeiro pilar: a Intenção***; há três formas diferentes: adicionar nova intenção a partir do botão azul “Create intent”, usar exemplos do catálogo de conteúdo, na aba “Content Catalog”, ou importar um arquivo CSV a partir do botão “Upload intents”. 
  - no dia a dia da empresa, é comum gerir o conteúdo em uma planilha Excel para, depois, exportar o formato em CSV e importar no Watson Assistant.
  - aqui, como instrumento de estudo, você utilizará a própria ferramenta de treinamento para criar o seu primeiro chatbot. 
- ***clique no botão azul “Create intent”***. 
  - no primeiro campo, aparece um # (hashtag ou cerquilha): intenções serão representadas com uma # seguida do nome definido, enquanto entidades serão representadas com um @ seguido do nome definido. 
- ***dê o nome da intenção de “fazer_pedido”***, clique no botão azul “Create intent” (ou aperte Enter) e ***defina pelo menos 5 exemplos*** (número recomendável para se criar um modelo de intenção minimamente funcional): é uma digitalização de uma experiência da vida real, mas com a escalabilidade para atender a demanda demais pessoas. Essas frases de exemplos são usadas para treinar o modelo da intenção de sua Skill.
  - insira uma frase de cada vez e clique no botão azul “Add example” (ou aperte Enter) para adicionar na lista de exemplo. Exemplos de frases:

~~~
- "Desce uma pizza de mussarela"
- "Eu gostaria de fazer o meu pedido"
- "Manda uma pizza de calabresa"
- "Me vê uma pizza"
- "Quero fazer o meu pedido"
~~~

- após adicionar os exemplos, clique na seta azul, no canto superior esquerdo, para voltar para a lista de intenções.
- agora, clique na aba “Entities” para acessar as entidades.
  - é possível criar a sua própria entidade (botão azul “Create entity”) ou importar um arquivo CSV a partir do botão “Upload entities”.
  - além disso, você consegue usar entidades predefinidas pela IBM, chamada de “System entities”; algumas entidades de sistemas disponíveis em língua portuguesa:
    - **@sys-time**: reconhece tempo no formato tradicional e em outros formatos mais usuais dentro de uma conversa. Exemplos: 20:59, 10 da manhã, em 10 minutos, agora, daqui a 1 hora.
    - **@sys-date**: reconhece datas no formato tradicional e em outros formatos mais usuais dentro de uma conversa. Exemplos: 12/12/2018, 7 de setembro, hoje, amanhã, agora, na próxima sexta.
    - **@sys-percentage**: reconhece valores com o símbolo de % (porcentagem) ou escrito "porcentagem". Exemplos: 50%, 90 por cento.
    - **@sys-currency**: reconhece valores monetários na frase informada pelo usuário. Exemplos: 20 centavos, 50 reais, R$ 75,00.
    - **@sys-number**: reconhece números como dígitos e escritos. Exemplos: 21, vinte e um.
- ***criaremos a nossa própria entidade***: clique no botão azul “Create entity” e defina o nome de “sabor”, que será o complemento da informação. Ao fazer um novo pedido, o usuário deverá informar o sabor da pizza.
  - diferentemente das intenções, as entidades trabalham em um modelo um pouco diferente de dados para treinamento: a estrutura de inserir exemplos é mantida, porém você insere valores e seus `sinônimos` (por questões de variações regionais e até errôneas) ou `expressão regular` (para ensinar um padrão ao invés de ensinar diversas variações com a mesma estrutura, como CEP, CPF)
  - no caso da pizzaria, criaremos uma entidade de sabor e os valores da entidade com seus sinônimos, como calabresa, muçarela e portuguesa.

~~~
- Valor: "calabresa". Sinônimo: "linguiça" e "calabreza".
- Valor: "muçarela". Sinônimo: "queijo" e "mussarela".
- Valor: "portuguesa". Sinônimo: "portuga" e "lusa".
~~~

- agora que temos a intenção #fazer_pedido e a entidade @sabor, ***construir o fluxo de diálogo na próxima aba, de “Dialog”***. 
  - há dois retângulos, um embaixo do outro, de “Bem-vindo” e de “Em outros casos”.
  - no Watson Assistant, chamamos esse retângulo de `nó de Diálogo (ou Dialog Node)`: quando um usuário faz uma pergunta, passa por cada nó de cima para baixo, até achar um que seja compatível com a frase enviada pelo usuário.
  - é dado o match com o nó de “Bem-vindo” com a primeira interação do usuário no primeiro contato com o chatbot. E é dado match com o nó de “Em outros casos” quando o chatbot não souber identificar a pergunta do usuário em uma das intenções ou entidades criadas. O nó de “Em outros casos” sempre deverá ser o último nó da árvore de decisão.
- crie um nó entre ambos os nós iniciais: clicar sobre o botão de três bolinhas do nó de “Bem-vindo” e clicar na opção ***“Add node below"***. Definir o campo “If assistant recognizes” com a intenção #fazer_pedido. É possível adicionar outros valores, como outras intenções ou entidades.
  - no campo ***"Assistant responds"***, definir a resposta para o usuário; é possível usar textos, criar um menu de opções, dar uma pausa, enviar uma imagem, transferir para um atendente humano ou para um outro canal de atendimento. 
  - o campo ***"Then assistant should"*** é usado para definir se o chatbot deve esperar o usuário responder ou se deve, automaticamente, pular para outro nó.
- clicar no ***botão "Customize"***, no canto superior direito da caixa do seu nó. Uma caixa será aberta. Habilite somente o ***item "Slot"*** e clique no botão azul "Apply". Você estará habilitando a funcionalidade que permite que você peça um certo dado para o usuário e salve este dado como uma variável de contexto, sinalizado pelo símbolo $ (cifrão).
  - assim que habilitar, você verá uma nova seção dentro do nó, chamado "Then check for". 
  - haverá 3 campos: o primeiro campo você deverá informar uma intenção, entidade ou variável de contexto. Definindo o primeiro campo, o segundo campo automaticamente será preenchido com o mesmo nome, apenas substituindo o # ou @ por $ (da variável de contexto). O último campo você deve configurar com uma pergunta no cenário de quando o usuário não fornecer nenhum dado. Preencha os campos com a entidade @sabor, e o último com a pergunta "Qual é o sabor da pizza?".
  - a funcionalidade de Slots funciona como um loop: o usuário somente sairá quando fornecer corretamente todos os dados válidos para preencher os itens do Slot.
- com os campos todos preenchidos, basta definir a resposta, ou mais de uma resposta, para o usuário. Nesse exemplo, deixamos apenas uma frase de “Ok! Anotei o seu pedido. Sua pizza de $sabor será entregue em até 40 minutos. Obrigado e boa noite!”.
- agora que você tem uma Skill elaborada e treinada, chegou a hora de criar um Assistant e gerar uma página na Web para compartilhar com outras pessoas.

- `testando a Skill treinada`:
  - clicar no botão branco do canto superior direito, “Try it”, para abrir o chat interno da ferramenta. 
  - esse chat é feito para realizar todos os testes e não desconta do valor limite de mensagens por mês de qualquer plano do serviço do Watson Assistant.
- agora que você tem uma Skill elaborada e treinada, chegou a hora de criar um Assistant e gerar uma página na Web para compartilhar com outras pessoas.

## 1.4 Criação do Assistente e integrações

- volte para a tela inicial da ferramenta do Watson Assistant, clicando no item “Assistants”. 
- para testar as integrações nos canais de comunicação, clicar em uma das opções de integração no canto direito do Assistant: algumas integrações poderão ser configuradas direto na plataforma, e outras demandarão um trabalho de programação.
- atualmente existem 9 integrações no Watson Assistant, disponíveis na aba Assistants. Além das integrações existentes, na documentação do Watson Assistant, você encontra a documentação para integrar o seu assistente com outros serviços externos, como service desk (Salesforce, Zendesk, Genesys Cloud, NICE, inContact, Twilio Flex, Oracle B2C Service e service desk customizado) e telefone (Twilio Flex e Genesys Cloud).

### a) Web chat: 

- disponibiliza um widget customizável e seguro para adicionar em seu website. 
- você pode configurar como e onde o widget do web chat aparecerá e você pode usar um tema alinhado com a sua marca e design do website. 
- se um cliente precisar de ajuda, a integração com web chat pode transferir a conversa para um agente (atendente).

### b) Phone: 

- permite que seu assistante (assistant) converse com clientes pelo telefone usando os serviços IBM Watson Text to Speech (serviço de sintetização de voz) e Speech to Text (serviço de transcrição de áudio para texto). 
- se seu cliente pedir para conversar com uma pessoa, a integração por telefone pode transferir a ligação para um agente (atendente).

### c) WhatsApp with Twilio: 

- integre com o WhatsApp para que seu assistente possa trocar mensagens com seus clientes onde eles estão. 
- cria uma conexão entre seu assistente (assistant) e o WhatsApp através do provedor de serviços Twilio. 
- é nessário ter uma conta de mensageria e um número de telefone no Twilio. 
- o WhatsApp possui um rigoroso processo para que a plataforma possa revisar todos os negócios que querem interagir com clientes em sua rede. 
- WhatsApp, empresa do grupo Meta, requer que você registre seu negócio no diretório de negócio da Meta.•

### d) Slack: 

- permite que seu assistente (assistant) responda a perguntas que são feitas em mensagens diretas ou em canais onde o assistente é diretamente mencionado.

### e) Facebook Messenger: 

- permite que seu assistente (assistant) responda a mensagens em uma determinada página no Facebook.

### f) SMS with Twilio: 

- clientes podem enviar mensagens de texto para o seu número de telefone disponibilizado pelo Twilio. 
- Twilio usa um webhook para que você possa configurar para enviar uma requisição POST com a mensagem de texto no corpo da requisição (body) para o seu assistente (assistant). Cada resposta do assistente é enviado de volta para o Twilio para que possa ser convertido em uma mensagem SMS de saída para ser enviada para o cliente. A resposta é enviada para a API do Twilio para processamento. 
- você disponibiliza sua conta Twilio (Twilio account SID) e as informações do token de autenticação do projeto, que servem como sua credencial de acesso a API do Twilio.

### g) Intercom:

- é uma plataforma de mensageria de cliente para ajudar negócios a crescerem através do melhor relacionamento durante o ciclo de vida do cliente. 
- Intercom possui parceria com a IBM para adicionar um novo agente (agent) para o time de suporte do cliente, um assistente do Watson Assistant.
- permite que a aplicação transmita conversas de usuário perfeitamente entre seu assistente e agentes humanos. 
- se você integrar seu assistente com o Intercom, a aplicação do Intercom se torna a aplicação que interage com seus clientes. 
- todas as interações com os usuários são iniciados e gerenciados pelo Intercom.

### h) Custom application: 

- se nenhuma integração existente atender a sua necessidade, você pode construir sua própria aplicação como a interface entre o seu assistente e seus usuários. 
- exemplos de integrações customizadas: disponibilizar seu assistente no Google Home e na Amazon Alexa.

### i) Voice Agent (Telephony):

- permite gerar um número de telefone comercial que é conectado automaticamente ao seu assistente.
- ou, se preferir, pode conectar o assistente à sua infraestrutura existente configurando um SIP (Session Initiation Protocol) trunk existente.
- SIP trunk é equivalente a uma linha telefônica analógica, exceto que usa Voz sobre Protocolo de Internet (VoIP) para transmitir dados de voz e pode suportar várias chamadas simultâneas.
- o trunk pode se conectar à rede telefônica pública comutada (PSTN) ou à central privada (PBX) local de sua empresa. 
- se você optar por gerar um número de telefone gratuito para o seu assistente, um SIP trunk será fornecido automaticamente pelo IntelePeer.
- você também pode optar por usar um tronco SIP existente de um provedor como IntelePeer, Genesys ou Twilio.

> No caso da opção de “Integrate web chat”, você pode gerar um script em Javascript para inserir no HTML do seu site e utilizar a interface gráfica pronta da IBM para interagir com o seu chatbot. Ou você pode ver outras opções ao clicar no botão “Add integration”. Para testar em uma página pronta, sem precisar atualizar código ou subir um novo site, você pode selecionar a opção “Preview” e gerar um link para uma aplicação pronta com um chat no meio da tela; dessa forma, você pode compartilhar com seus amigos, colegas e familiares para que eles testem o seu chatbot.

---

## FAST TEST

### 1. Sobre Actions Skill, selecione a afirmação correta:
> Oferece uma interface simples, na qual qualquer profissional pode construir um fluxo conversacional para o seu assistente seguir. O complexo processo de criação de dados de treinamento ocorre atrás das cenas automaticamente.

### 2. Sobre Search Skill, selecione a afirmação correta:
> Alavanque informações de bases de conhecimento corporativo existentes ou outras coleções de conteúdo de autoria de especialistas no assunto para atender a consultas de clientes imprevistas ou mais sutis. Para uma determinada consulta do usuário, usa o serviço IBM Watson Discovery para procurar uma fonte de dados de seu conteúdo de autoatendimento e retornar uma resposta.

### 3. Sobre Dialog Skill, selecione a afirmação correta:
> Oferece um conjunto de editores para que você use para definir ambos os seus dados de treinamento e a conversa. A conversa é representada como uma árvore de diálogo. Você usa o editor de diálogo gráfico para criar uma espécie de script para o seu assistente ler quando ele interage com seus clientes. A caixa de diálogo identifica os objetivos comuns do cliente que você ensina a reconhecer e fornece respostas úteis.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)
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





--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)
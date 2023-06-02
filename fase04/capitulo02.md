<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 02: Internet: Como tudo começou. 🗺️</h2>
</div>

<div align="center">
<h2>1. INTERNET: COMO TUDO COMEÇOU</h2>
</div>

## 1.1 Introdução

- o universo do desenvolvimento de sistemas evolui rapidamente, ganhando a cada dia novas tecnologias, ferramentas e processos mais produtivos.
- a rede mundial de computadores está definitivamente incorporada à sociedade moderna, mudando o estilo de vida das pessoas.

## 1.2 História da Internet

> `Internet`: conjunto de redes de computadores interligados pelo mundo, que utilizam uma coleção de protocolos e serviços em comum para permitir uma comunicação plena.

- surgiu na Guerra Fria, na década de 1960.
  - os EUA desenvolveram a rede mundial de computadores com propósitos militares.
  - o objetivo foi descentralizar as informações e criar uma rede redundante (em caso de ataque, as informações não seriam perdidas e a comunicação entre os centros de informações seria mantida).
  - ***Dessa forma, a Agência de Pesquisas em Projetos Avançados (Arpa) desenvolveu uma rede de comunicações chamada Arpanet, a primeira rede de computadores do mundo!***

- nas décadas de 1970 e 1980, essa rede mundial de computadores foi utilizada também para comunicação no meio acadêmico, entre universidades americanas.

- na década de 1990, a Internet foi disponibilizada para a população.
  - o físico britânico Timothy John Berners-Lee desenvolveu a World Wide Web (WWW), que possibilita a utilização de interface gráfica e a criação de sites com a linguagem HTML, e a sua transferência com o protocolo HTTP, permitindo navegar de um site a outro.

## 1.3 Servidores

- computador de alta capacidade de processamento e armazenamento, onde rodam softwares específicos, e que está conectado à Internet. 
  - sites e aplicações web ficam disponíveis a qualquer dispositivo com acesso à Internet. 
  - é possível também implantar um sistema web em uma rede privada para restringir o acesso dos usuários. Essa rede é denominada como Intranet.

- para que os sites e aplicações web fiquem disponíveis na Internet, eles devem estar hospedados (implantados) em algum servidor.

> `Para acessar um site:` utilizar um programa chamado Navegador ou Browser > digitar a URL do site > uma mensagem será enviada ao servidor em que o site está hospedado > o servidor processa a mensagem > envia de volta as informações da página para o usuário.

- `Backbone`:
  - conjunto de poderosos computadores conectados por linhas de grande largura de banda (como canais de fibras ópticas, elos de satélites e elos de transmissão por rádio).
  - para constituir a Internet, vários backbones estão interligados e encontram-se hierarquicamente divididos: os de ligações intercontinentais (que derivam de backbones internacionais), que, por sua vez, derivam de backbones nacionais.
  - são a espinha dorsal da Internet, pois praticamente todas as informações que trafegam passam por backbones.
  - backbones de diferentes continentes estão conectados por meio de cabos (de fibra óptica) submarinos, que atravessam mares e oceanos, capazes de transmitir milhares de informações por segundo, permitindo uma troca de informação rápida e eficiente.

## 1.4 O Protocolo TCP/IP (TPC/IP Protocol Suite)

> `TCP` é o Protocolo de Controle de Transmissão, e `IP` é o Protocolo de Internet.

- permite a comunicação entre as redes espalhadas pelo mundo.
- a arquitetura TCP/IP surgiu em 1975 na rede Arpanet.
- arquitetura TCP/IP é ***formada por quatro camadas***, que possuem responsabilidades bem definidas, fornecendo serviços para as camadas superiores.

### 1. Camada de aplicação:
- utilizada pelos programas para enviar e receber informações de certos programas por meio da rede.
- nela, encontramos protocolos como SMTP (para e-mail), FTP (tranferência de arquivos) e HTTP (navegar na internet).

### 2. Camada de transporte:
- responsável por receber os dados enviados pela camada de aplicação, verificar a integridade e dividi-los em pacotes.

### 3. Camada de Rede:
- recebe os dados empacotados e os anexa ao endereço virtual (IP) do computador remetente e do destinatário.

### 4. Camada de Interface:
- recebe e envia pacotes pela rede.

Observações:
- em uma rede TCP/IP, cada equipamento conectado à rede deve possuir um **endereço único capaz de identificá-lo**, chamado de endereço `IP`.
  - o IP permite entrega das informações aos seus destinos de forma correta e eficiente. 
  - cada equipamento conectado à Internet deve possuir um endereço IP para ser encontrado na rede.

## 1.5 Domínios

- para facilitar a memorização dos endereços de equipamentos conectados à Internet, utiliza-se os nomes de domínios, que permitem a tradução para um endereço IP.
- a associação de nomes de domínio para um endereço IP é feita por um conjunto de servidores de DNS – Domain Name System (Sistema de Nomes de Domínios).
- o DNS está estruturado em dois pontos básicos:
  - Organização da Internet em Domínios.
  - Distribuição dos Servidores DNS na Internet.
- tem como objetivo evitar a reutilização de um mesmo nome por mais de um equipamento conectado à Internet e descentralizar o cadastramento deles.
- cada país possui uma entidade responsável por atribuir endereços de IP e fazer a sua associação com um nome.

<div align="center">
<h2>2. SERVIÇOS DISPONÍVEIS NA INTERNET</h2>
</div>

- ponto comum: modelo de implementação cliente-servidor (os serviços são disponibilizados em programas-servidores, e o usuário acessa os programas por meio da Internet, utilizando programas-clientes).

## 2.1 World Wide Web (WWW)

- serviço de acesso a informações por hipertexto, que cria a imagem de uma teia que interliga documentos pela Internet.
- são documentos que podem conter imagens, textos e recursos multimídia (documentos hipermídia).
- a estrutura desses documentos é desenvolvida utilizando a linguagem de marcação `HTML (Hypertext Markup Language)`, que permite a ligação com outros documentos (hyperlinks).
- um documento HTML é localizado na WWW por um identificador chamado `Uniform Resource Locator(URL)`. 
  - a URL identifica o tipo deserviço, o endereço do servidor e onde o documento está dentro desse servidor.

> exemplo: "http://www.fiap.com.br/graduacao"

- **http** (Hypertext Transfer Protocol): protocolo de comunicação para transmissão de documentos de hipertexto (HTML) na World Wide Web presente na camada de aplicação da arquitetura TCP/IP
- **www.fiap.com.br**: nome de domínio, que será traduzido por um servidor de DNS para o endereço de IP do servidor onde está instalado o site da FIAP.
- **/graduacao**: subdiretório que fica dentro do domínio principal, onde se encontram informações sobre os cursos de graduação da Fiap.

- para o usuário acessar o serviço WWW, é necessária utilização de um programa-cliente: `browser ou navegador`.
  - permite inserir a URL da página que deseja acessar.
  - o browser recebe as informações, interpreta e exibe a página HTML.
  - há diversos browsers disponíveis gratuitamente, como Microsoft Edge, Mozilla Firefox, Google Chrome, Opera etc.
  - passos para acessar uma página web:
    - usuário insere no browser a URL da página que deseja acessar.
    - o nome de domínio é traduzido para o endereço de IP do servidor.
    - com o endereço de IP, o browser envia uma requisição HTTP para o servidor. 
    - o servidor processa a requisição e envia uma resposta HTTP com as informações da página HTML. 
    - o browser recebe a resposta, interpreta o documento HTML e mostra a página para o usuário.

## 2.2 FTP – Protocolo de Transferência de Arquivos

- é o serviço-padrão da Internet para transferência de arquivos entre computadores. 
- seu funcionamento se baseia no estabelecimento de uma comunicação entre o cliente FTP e o servidor FTP remoto, tornando possível navegar na estrutura de diretórios do servidor FTP e executar comandos para a manipulação de diretórios e arquivos.

## 2.3 E-Mail – Serviços de correio eletrônico

- tem por objetivo a comunicação e troca de dados entre computadores.
- o funcionamento tem como base um endereço conhecido como e-mail address ou endereço de correio eletrônico (usuario@dominio).
- esses serviços são baseados nos protocolos POP3, IMAP e SMTP, que estão presentes também na camada de aplicação e são utilizados para enviar e receber as mensagens dos servidores de e-mail.
  - há vários outros, como Telnet: para execução remota de aplicações e o Network News que permite a disponibilização e recebimento de informações agrupadas por categorias.

### Recursos da Internet que mudaram o estilo de vida das pessoas:

- ambiente de acesso remoto.
- transmissão de mídia.
- voz sobre IP (VoIP).

## 2.4 W3C (World Wide Web Consortium) e Web Standards

- criada em 1994.
- trata-se de uma organização internacional formada por empresas, instituições, pesquisadores e desenvolvedores. 
- cria normas e especificações aplicáveis aos diversos segmentos e setores da web (chamados de `Padrões Web ou Web Standards`), [disponíveis aqui](https://www.w3.org/).

> Web Standards é um conjunto de normas, diretrizes, recomendações, notas, artigos, tutoriais e afins de caráter técnico produzidos pelo W3C e destinados a orientar fabricantes, desenvolvedores e projetistas para o uso de práticas que possibilitem a criação de uma Web acessível a todos, independentemente dos dispositivos usados ou de suas necessidades especiais.

- benefícios de utilizar os padrões:
  - as páginas que seguem padrões web terão grande visibilidade nos resultados de busca da web.
  - a acessibilidade permite acesso de todas as pessoas. 
    - podem utilizar browsers de voz, que leem documentos para pessoas com deficiência visual. 
    - além de seguirem padrões que permitem que os usuários com Internet de baixa velocidade ou que utilizam browsers portáteis com dispositivos de telas pequenas possam usar os sites normalmente.

<div align="center">
<h2>3. DESENVOLVIMENTO EM CAMADAS</h2>
</div>


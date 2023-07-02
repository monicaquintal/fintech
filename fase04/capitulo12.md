<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 12: A rede social dos desenvolvedores. 😺🐙</h2>
</div>

<div align="center">
<h2>1. A REDE SOCIAL DOS DESENVOLVEDORES</h2>
</div>

## 1.1 Sistema de controle de versão

- em 2005, Linus Torvalds, criador do Linux, desenvolveu um novo sistema de controle de versão chamado `Git`.

- em 2008, foi criado o `GitHub`, uma rede social de compartilhamento de código, um repositório de códigos-fontes, que podem ser privados ou abertos, de desenvolvedores iniciantes até grandes empresas. 

### 1.1.2 Instalação e configuração do Git

- para instalar, acessar o [site do Git](git-scm.com).
- o site vai identificar o sistema operacional e,então, clicar no botão Download.
- após baixar o arquivo executável, o processo de instalação é simples (easy-to-install).
- com o Git instalado, configurar o sistema para identificar o desenvolvedor responsável pelas alterações.
  - `git -v` verifica se o git está instalado e a versão.
- para criar o primeiro diretório, criar uma pasta e,com o botão direito, clicar na opção Git Bash Here.
- o terminal se abrirá, e devemos digitar o primeiro comando: `git init`. 
  - é criada uma pasta oculta chamada .git.
  - quer dizer que iniciamos o repositório. 
- para configurar o repositório com o nome e o e-mail, digitar o seguinte comandono terminal:

~~~git
git config --global user.name "Fulana da Silva"
git config --global user.email "email@fiap.com.br"
~~~

- a configuração acima é global, para evitar que em todo projeto seja necessária uma nova configuração.
- para verificar se o nome e e-mail foram setados corretamente, entrar com os comandos:

~~~git
git config user.name
git config user.email
~~~

### 1.1.3 Estados dos arquivos e commits

- o comando `git status` informa o estado de nosso arquivo (o que há de alterações).
  - untracked = arquivo desconhecido para o Git.
    - o Git entende que existe um arquivo, mas não identifica nenhum estado.
    - precisamos informar para o Git que esse arquivo deve ser versionado e, para isso, executar os próximos dois comandos.

- `comando git add nomeDoArquivo.extensao` (informa para o Git que esse arquivo deve ser versionado).
- `comando git commit -m "Primeiro commit"` (responsável pela gravação no repositório).

### 1.1.4 Navegação entre as versões

- para verificar todo o histórico de mudanças em nosso repositório, utilizamos o comando `git log`.
  - git log retorna um ID, autor, data e a própria alteração realizada.
- `git diff`: após executar esse comando, o Git informa qual foi a alteração (texto em verde) e quantas alterações foram realizadas (texto em azul).

### 1.1.5 Desfazendo alterações

## 1.2 Organizando o trabalho

- para aumentar a produtividade em sistemas de controle de versão, há a possibilidade de nomear as hashes, criando tags e versões paralelas do código.

### 1.2.1 Trabalhando com branches e tags

- um branch no Git é um ponteiro móvel para um desses commits.
- o nome do branch padrão no Git é master. 
- conforme começa a fazer commits, você recebe um branch master que aponta para o último commit que você fez. Cada vez que você faz um novo commit, ele avança automaticamente.
- `git branch nome-da-branch`.

### 1.2.2 Merge 

- mescla alterações nas branches.
- comando `git merge`.

### 1.2.3 Resolução de conflitos

### 1.2.4 Ignorando arquivos do repositório

- o `gitignore` especifica arquivos intencionalmente não rastreados que o Git deve ignorar.

## 1.3 Conhecendo o GitHub

- é a maior rede social de código aberto utilizando o sistema de controle de versão Git. 
- em 2018, a Microsoft comprou o site GitHub.

### 1.3.1 Trabalhando com repositórios remotos

### 1.3.2 `git clone`

- o comando git clone é utilizado para realizar a baixa de uma branch específica do servidor remoto do repositório, o GitHub. 
- pode ser utilizado o protocolo HTTPS (com usuário e senha) ou o protocolo SSH (com um certificado de chave público e privada) para troca de informações e dados com o servidor.

### 1.3.3 `git pull`

- há situações em que temos arquivos atualizados no repositório remoto e arquivos que não estão atualizados no repositório local.
- o `git pull` é responsável pela atualização de todas as versões.
- ideal quando se está trabalhando off-line e os arquivos locais ainda não estão sincronizados com o repositório remoto. 

### 1.3.4 `git push`

- é o inverso do git pull.
- é por meio dele que você envia seus arquivos atualizados para o seu repositório remoto, no caso o GitHub.

### 1.3.5 `git checkout`

- utilizado para realizar a troca de branch ativa, ou também para reverter arquivos que estão alterados na branch local.

## 1.4 Boas práticas

- perfil customizado.
- exemplo de readme.

---

## FAST TEST

### 1. Qual comando é responsável pela atualização de todasas versões, ideal para quando se está trabalhando off-line?
> git pull.

### 2. Identifique qual afirmação relacionada a GitHub é falsa:
> No GitHub, os repositórios podem ser apenas privados.

### 3. No GitHub, qual é o comando utilizado para realizar a baixa de uma branch específica do seevidor remoto do repositório?
> git clone.

---

## QUIZ - VIEW

### 1. O Bootstrap é um framework front-end responsivo, elegante e de fácil aprendizado que permite uma maior agilidade no desenvolvimento de páginas Web. Originalmente, o Bootstrap foi criado como um projeto interno de qual empresa:
> Twitter

### 2. A frase “É a principal organização internacional para padronização da World Wide Web. Consiste em um consórcio internacional que agrega empresas, órgãos governamentais e organizações independentes com a finalidade de estabelecer padrões para a criação e a interpretação de conteúdo para a Web.”, refere-se a:
> W3C

### 3. No início da década de 1990, Timothy John Berners-Lee desenvolveu a World Wide Web (WWW) utilizando uma linguagem de programação que viria a revolucionar o mundo. No caso, estamos falando da linguagem de programação:
> HTML

### 4. Considerar a tipologia que será utilizada em um projeto é fundamental para que o usuário tenha uma experiência agradável ao acessar a página Web. Neste contexto, a maioria dos navegadores Web (browsers) têm como fonte padrão:
> Times New Roman

### 5. Em relação às camadas de desenvolvimento Web, qual tecnologia está associada à camada de apresentação?
> CSS

### 6. Qual tag é responsável pela inserção da maioria dos componentes de um formulário?
> input

### 7. Em um formulário, qual atributo é utilizado para definir uma palavra ou frase que ficará visível dentro dos campos, de modo a sugerir aos usuários como efetuar o preenchimento destes campos?
> placeholder.

### 8. A comunicação entre as redes espalhadas por todo o mundo é possível pelo uso do conjunto de protocolos conhecido como:
> TCP/IP

### 9. Muitas vezes chamada de “caixa mágica”, qual tag é um contêiner que poderá ser criado para armazenar qualquer tipo de conteúdo?
> &lt;div&gt;

### 10. Por meio de um conjunto de regras CSS, é possível determinar como o layout de uma página Web será exibido em diferentes tamanhos de telas. Este conceito é chamado de:
> Design responsivo

### 11. Quando trabalhamos com HTML, temos que sempre ter em mente que ela é uma linguagem de:
> Marcação

### 12. Para que o navegador Web (browser) entenda a formatação da página, é necessário colocar as regras CSS dentro da tag:
> &lt;style&gt;

---

## Atividade Cap 12 - A rede social dos desenvolvedores - Subir seu site no GIT

<em>"Assista novamente os vídeos do Capítulo 12, crie o seu repositório e envie os arquivos do projeto Fintech.<br>
Atenção para a entrega:<br>
Nesta atividade, você deverá criar um documento contendo o link do seu perfil no GitHub. Exporte para PDF e faça o upload do arquivo em nossa plataforma.<br>
Lembre-se de manter o repositório como público, pois somente assim o professor que irá corrigir a atividade conseguirá avaliar o trabalho realizado."</em>

> Atividade desenvolvida [aqui](https://github.com/monicaquintal/cashPro).

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)
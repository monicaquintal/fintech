// RETORNANDO ELEMENTOS PELO ID:

// 1) utilizando o getElementById()
const getId = document.getElementById('vingadores');
console.log(getId);
// 2) utilizando o document.querySelector()
const queryId = document.querySelector('#vingadores');
console.log(queryId);

// --------------------------------------------------------

// RETORNANDO ELEMENTOS PELA CLASS:

// 1) utilizando o getElementsByClassName()
const getClass = document.getElementsByClassName('nome');
console.log(getClass);
// 2) utilizando o document.querySelectorAll()
const queryClass = document.querySelectorAll('.nome');
console.log(queryClass);

// --------------------------------------------------------

// RETORNANDO ELEMENTOS PELA TAG:

// 1) utilizando o getElementsByTagName()
const getTag = document.getElementsByTagName('td');
console.log(getTag);

// 2) utilizando o document.querySelectorAll()
const queryTag = document.querySelectorAll('td');
console.log(queryTag);

// --------------------------------------------------------

// MANIPULANDO DADOS (propriedade “text-content” para altera de Capitão América para Homem Aranha):

// 1) Pegando o elemento
console.log(queryTag[5]);
console.log(`${queryTag[5].textContent} será trocado pelo Homem Aranha`);
// 2) Alterando o nome
queryTag[5].textContent = 'Homem Aranha';

// --------------------------------------------------------

// OBTENDO INFORMAÇÕES ATRAVÉS DE ATRIBUTOS

// 1) recuperando o atributo na página HTML
const dataAtualizacao = document.querySelector('[data-JS]');
// 2) recuperando a data completa
const dataAtual = new Date();
// 3) formatando a data
const formataData = Intl.DateTimeFormat('pt-BR', {dateStyle: "long",});
dataAtualizacao.textContent += formataData.format(dataAtual);

// --------------------------------------------------------

// ESTUDANDO EVENTOS (calculando XP dos heróis)

// 1) recuperando o botão
const btnCalcular = document.querySelector('#calcular');
// 2) atribuindo a função ao botão recuperado
btnCalcular.addEventListener('click', () => {
  //3) recuperando os elementos que têm a classe vingador
  const vingadores = document.querySelectorAll('.vingador');
  // 4) usando um for para percorrer o array - forEach()
  vingadores.forEach(vingador => {
    // 5) recuperando o valor da força e convertendo em um número
    const forca = Number(vingador.querySelector('.forca').textContent);
    // 6) recuperando o valor da agilidade e convertendo em um número
    const agilidade = Number(vingador.querySelector('.agilidade').textContent);
    // 7) recuperando o valor da velocidade e convertendo em um número
    const velocidade = Number(vingador.querySelector('.velocidade').textContent);
    // 8) calculando os xp de cada vingador
    const resultadoXP = (forca + agilidade + velocidade)/3;
    // 9) exibindo na página o xp correspondente
    vingador.querySelector('.xp-Final').textContent = resultadoXP.toFixed(1);
    // 10) verificar se o XP é menor que 91 e colocar duas classes CSS para chamar a atenção ao herói
    if (resultadoXP <= 91) {
      vingador.classList.add('bg-danger', 'text-light');
    }
  })
})
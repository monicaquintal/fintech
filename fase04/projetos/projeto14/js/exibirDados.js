function exibirXP() {
  // recuperando os elementos que têm a classe vingador
  const vingadores = document.querySelectorAll('.vingador');
  // usando um for para percorrer o array - usaremos o forEach()
  vingadores.forEach(vingador => {
    // recuperando o valor da força e convertendo em um número
    const forca = vingador.querySelector('.forca').textContent;
    // recuperando o valor da agilidade e convertendo em um número
    const agilidade = vingador.querySelector('.agilidade').textContent;
    // recuperando o valor da velocidade e convertendo em um número
    const velocidade = vingador.querySelector('.velocidade').textContent;
    // calculando os xp de cada vingador
    const resultadoXP = calcularXP(forca, agilidade, velocidade);
    // exibindo na página o xp correspondente
    vingador.querySelector('.xp-Final').textContent = resultadoXP.toFixed(1);
  })
}
// chamando as funções
formataData();
exibirXP();
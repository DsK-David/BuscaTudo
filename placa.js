const axios = require("axios");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Digite a placa do veículo: ", async placa => {
  try {
    const response = await axios.get(`https://api-de-placas.com/v1/carros/${placa}`);
    const { data } = response;

    console.log(`
    Marca: ${data.marca}
    Modelo: ${data.modelo}
    Ano: ${data.ano}
    Cor: ${data.cor}
    `);
    rl.close();
  } catch (error) {
    console.error("Não foi possível obter informações sobre a placa informada");
    rl.close();
  }
});

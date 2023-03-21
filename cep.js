const axios = require("axios");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Digite o CEP: ", async cep => {
  try {
    const response = await axios.get(`https://viacep.com.br/ws/${cep}/json/`);
    const { data } = response;

    console.log(`
    CEP: ${data.cep}
    Logradouro: ${data.logradouro}
    Bairro: ${data.bairro}
    Cidade: ${data.localidade}
    Estado: ${data.uf}
    `);
    rl.close();
  } catch (error) {
    console.error("Não foi possível obter informações sobre o CEP informado");
    rl.close();
  }
});

const google = require('google-it');
const fs = require('fs')
const https = require('https');
const cheerio = require('cheerio');

// Dicionário de respostas
const respostas = {
  "O que é inteligência artificial?": "Inteligência artificial é a simulação de processos inteligentes por computadores ou máquinas.",
  "Quem foi Albert Einstein?": "Albert Einstein foi um físico teórico alemão que desenvolveu a teoria da relatividade geral.",
  "Qual é a capital do Brasil?": "A capital do Brasil é Brasília."
}

// Função que retorna a resposta de acordo com a pergunta
function get_resposta(pergunta) {
  if (pergunta in respostas) {
    return respostas[pergunta];
  } else {
    const query = pergunta;
    return google({ query: query, limit: 1, lang: 'pt-BR' })
      .then(results => {
        const url = results[0].link;
        return new Promise((resolve, reject) => {
          https.get(url, res => {
            let data = '';
            res.on('data', chunk => {
              data += chunk;
            });
            res.on('end', () => {
              const $ = cheerio.load(data);
              const resposta = $('p').first().text();
              const dados = data;
              resolve(resposta);
              fs.writeFile('news.txt', JSON.stringify(resposta), function (err) {
                if (err) throw err;
                console.log('Dados salvos em news.txt');
              });
            });
          }).on('error', err => {
            reject(err);
          });
        });
      })
      .catch(() => {
        return "Desculpe, não encontrei nenhuma resposta para esta pergunta.";
      });
  }
}

// Loop principal do chatbot
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Digite sua pergunta: ', pergunta => {
  get_resposta(pergunta)
    .then(resposta => {
      console.log(resposta);
      readline.close();
    })
    .catch(() => {
      console.error("Erro ao obter resposta");
      readline.close();
    });
});

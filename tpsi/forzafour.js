const intersezioneNomi = (listaA, listaB) => {
  const setB = new Set(listaB);
  
  // 1. Filtriamo listaA cercando elementi in setB
  // 2. Usiamo un Set per rimuovere i duplicati del risultato
  // 3. Stampiamo joinando i nomi con un a capo
  const risultati = [...new Set(listaA.filter(nome => setB.has(nome)))];
  
  console.log(risultati.join('\n'));
};

const nomi1 = ["mario", "giovanni", "mario", "luca", "carlo", "luca", "fabio"];
const nomi2 = ["alberto", "flavio", "paolo", "alberto", "carlo", "marco", "mario", "mario", "fabio", "pino", "luca"];

intersezioneNomi(nomi1, nomi2);
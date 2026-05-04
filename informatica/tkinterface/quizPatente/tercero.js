const analizzaVoti = (elencoVoti) => {
  const occorrenze = elencoVoti.reduce((acc, voto) => 
    acc.set(voto, (acc.get(voto) || 0) + 1), new Map());

  // Trasformiamo la Map in un array di stringhe formattate e stampiamo tutto insieme
  console.log([...occorrenze].map(([voto, num]) => `${voto} => ${num}`).join('\n'));
};

const votiIn = ["A", "B", "E", "A", "C", "B", "D", "A", "D", "C", "C", "E", "B", "E", "B"];
analizzaVoti(votiIn);
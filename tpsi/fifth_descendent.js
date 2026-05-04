const calcolaFatturaTotale = (prodotti, scontoPerc) => {
  const moltiplicatore = (100 - scontoPerc) / 100;

  // Sommiamo direttamente i prezzi scontati nell'accumulatore
  const totale = prodotti.reduce((somma, p) => somma + (p.prezzo * moltiplicatore), 0);

  console.log(`OUT: ${totale}`);
};

const carrello = [
  { nome: "Telefono", prezzo: 500 },
  { nome: "Laptop", prezzo: 1000 },
  { nome: "Cuffie", prezzo: 100 },
  { nome: "Monitor", prezzo: 300 }
];

calcolaFatturaTotale(carrello, 22);
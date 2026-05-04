function calcolaDistanzaDna(sequenzaA, sequenzaB) {
  if (sequenzaA.length !== sequenzaB.length) {
    throw new Error("Le catene di DNA devono avere la stessa lunghezza");
  }

  // Trasformiamo in array, filtriamo solo i caratteri diversi e leggiamo la lunghezza
  const differenze = sequenzaA.split('').filter((carattere, indice) => {
    return carattere !== sequenzaB[indice];
  });

  return differenze.length;
}

// Test di verifica
try {
  console.log("Distanza:", calcolaDistanzaDna("ABCABCDDCDAAAAAAC", "ABCABCEECDAABAABD")); // 5
  console.log("Distanza (Vuote):", calcolaDistanzaDna("", "")); // 0
} catch (errore) {
  console.error("Errore riscontrato:", errore.message);
}
class AutomaSpostamento {
  #posX;
  #posY;
  #origX;
  #origY;

  constructor(coordinataX = 0, coordinataY = 0) {
    this.#posX = coordinataX;
    this.#posY = coordinataY;
    this.#origX = coordinataX;
    this.#origY = coordinataY;
  }

  // Metodi di movimento
  alto() { this.#posY++; }
  basso() { this.#posY--; }
  destra() { this.#posX++; }
  sinistra() { this.#posX--; }

  get coordinateAttuali() {
    return { x: this.#posX, y: this.#posY };
  }

  get distanzaPercorsa() {
    const dx = this.#posX - this.#origX;
    const dy = this.#posY - this.#origY;
    // Teorema di Pitagora: sqrt(a² + b²)
    return Math.sqrt(dx ** 2 + dy ** 2);
  }

  eseguiPercorso(comandi) {
    const dizionarioAzioni = {
      'A': 'alto',
      'B': 'basso',
      'D': 'destra',
      'S': 'sinistra'
    };

    // Trasformiamo la stringa in array e usiamo reduce
    // L'accumulatore qui non ci serve per un valore finale, 
    // ma per processare ogni comando in sequenza senza cicli for/foreach.
    [...comandi].reduce((_, comando) => {
      const nomeMetodo = dizionarioAzioni[comando];
      if (this[nomeMetodo]) this[nomeMetodo]();
      return null; 
    }, null);
  }
}

// Verifica
const mioRobot = new AutomaSpostamento(2, 4);
mioRobot.eseguiPercorso('ADDAAD');

console.log("Coordinate finali:", mioRobot.coordinateAttuali); 
console.log("Distanza calcolata:", mioRobot.distanzaPercorsa);
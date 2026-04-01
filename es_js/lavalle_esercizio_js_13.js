let calcolaSomma = function(n) {
    let limite = Number(n);
    let somma = 0;

    for (let i = 0; i <= limite; i++) {
        somma += i;
    }

    return somma;
};

let risultato1 = calcolaSomma(5);
console.log("Somma da 0 a 5: " + risultato1);

let risultato2 = calcolaSomma("10");
console.log("Somma da 0 a 10: " + risultato2);

let risultato3 = calcolaSomma(3);
console.log("Somma da 0 a 3: " + risultato3);
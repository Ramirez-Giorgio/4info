let calcolatore = function(a, b, callback) {
    return callback(a, b);
};

let somma = function(x, y) { return x + y; };
let prodotto = function(x, y) { return x * y; };
let potenza = function(x, y) { return x ** y; };

console.log(calcolatore(5, 3, somma));
console.log(calcolatore(5, 3, prodotto));
console.log(calcolatore(2, 3, potenza));
let maggioreTre = function(a, b, c) {
    return a > b ? (a > c ? a : c) : (b > c ? b : c);
};

console.log(maggioreTre(10, 5, 20));
console.log(maggioreTre(100, 200, 50));
console.log(maggioreTre(3, 2, 1));
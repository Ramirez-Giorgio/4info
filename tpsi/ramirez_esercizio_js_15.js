let fibonacci = function(n) {
    let num = Number(n);
    if (num <= 1) return num;
    let a = 0, b = 1, temp;
    for (let i = 2; i <= num; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
};

console.log(fibonacci(0));
console.log(fibonacci(1));
console.log(fibonacci(5));
console.log(fibonacci("7"));
console.log(fibonacci(10));
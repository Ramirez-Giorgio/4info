let trovaMinore = function(o1, o2, o3) {
    let ms1 = (o1.h * 3600) + (o1.m * 60) + o1.s;
    let ms2 = (o2.h * 3600) + (o2.m * 60) + o2.s;
    let ms3 = (o3.h * 3600) + (o3.m * 60) + o3.s;

    if (ms1 <= ms2 && ms1 <= ms3) return o1;
    if (ms2 <= ms1 && ms2 <= ms3) return o2;
    return o3;
};

let t1 = { h: 12, m: 10, s: 5 };
let t2 = { h: 9, m: 45, s: 0 };
let t3 = { h: 15, m: 0, s: 20 };
console.log(trovaMinore(t1, t2, t3));

let t4 = { h: 1, m: 5, s: 10 };
let t5 = { h: 1, m: 5, s: 5 };
let t6 = { h: 1, m: 5, s: 15 };
console.log(trovaMinore(t4, t5, t6));
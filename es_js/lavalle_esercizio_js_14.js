let calcolaDifferenza = function(ora1, ora2) {
    let ms1 = (ora1.h * 3600000) + (ora1.m * 60000) + (ora1.s * 1000);
    let ms2 = (ora2.h * 3600000) + (ora2.m * 60000) + (ora2.s * 1000);
    let diff = ms1 - ms2;
    if (diff < 0) diff = -diff;

    return {
        ms: diff,
        s: diff / 1000,
        m: diff / 60000,
        h: diff / 3600000
    };
};

let o1 = { h: 10, m: 30, s: 0 };
let o2 = { h: 8, m: 15, s: 30 };
let res1 = calcolaDifferenza(o1, o2);
console.log(res1.ms, res1.s, res1.m, res1.h);

let o3 = { h: 12, m: 0, s: 0 };
let o4 = { h: 13, m: 45, s: 0 };
let res2 = calcolaDifferenza(o3, o4);
console.log(res2.ms, res2.s, res2.m, res2.h);
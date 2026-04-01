let analizzaOggetto = function(obj) {
    let chiavi = Object.keys(obj);
    for (let i = 0; i < chiavi.length; i++) {
        let k = chiavi[i];
        let v = obj[k];
        let t = typeof v;
        if (t === "string") {
            console.log(k, t, v.toLowerCase());
        } else {
            console.log(k, t, v);
        }
    }
};

let ogg1 = { nome: "MARIO", eta: 30, citta: "TORINO", attivo: true, ID: 123 };
analizzaOggetto(ogg1);

let ogg2 = { marca: "FIAT", modello: "PANDA", anno: 2020, colore: "ROSSO", km: 5000 };
analizzaOggetto(ogg2);
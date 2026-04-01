let Animale = function(nome, specie, eta) {
    this.nome = nome;
    this.specie = specie;
    this.eta = eta;

    this.verso = function() {
        console.log(this.nome + " sta emettendo un verso");
    };

    this.mangia = function() {
        console.log(this.nome + " sta mangiando");
    };

    this.enumera = function() {
        let chiavi = Object.keys(this);
        for (let i = 0; i < chiavi.length; i++) {
            console.log(chiavi[i]);
        }
    };
};

let Automobile = function(marca, modello, anno) {
    this.marca = marca;
    this.modello = modello;
    this.anno = anno;

    this.accendi = function() {
        console.log("Auto " + this.marca + " accesa");
    };

    this.suona = function() {
        console.log("Beep Beep!");
    };

    this.enumera = function() {
        let chiavi = Object.keys(this);
        for (let i = 0; i < chiavi.length; i++) {
            console.log(chiavi[i]);
        }
    };
};

let Poligono = function(nome, lati, colore) {
    this.nome = nome;
    this.lati = lati;
    this.colore = colore;

    this.disegna = function() {
        console.log("Disegno un " + this.nome + " " + this.colore);
    };

    this.info = function() {
        console.log("Questo poligono ha " + this.lati + " lati");
    };

    this.enumera = function() {
        let chiavi = Object.keys(this);
        for (let i = 0; i < chiavi.length; i++) {
            console.log(chiavi[i]);
        }
    };
};

let cane = new Animale("Fido", "Cane", 5);
let gatto = new Animale("Luna", "Gatto", 3);

let auto1 = new Automobile("Fiat", "500", 2020);
let auto2 = new Automobile("Ford", "Mustang", 1967);

let triangolo = new Poligono("Triangolo", 3, "Rosso");
let quadrato = new Poligono("Quadrato", 4, "Blu");

cane.enumera();
gatto.enumera();
auto1.enumera();
auto2.enumera();
triangolo.enumera();
quadrato.enumera();
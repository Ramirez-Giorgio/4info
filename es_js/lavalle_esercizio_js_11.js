let Automobile = function (marca, modello, colore, alimentazione, anno) {
  this.marca = marca;
  this.modello = modello;
  this.colore = colore;
  this.alimentazione = alimentazione;
  this.anno = anno;

  this.accendi = function () {
    console.log("L'auto " + this.marca + " " + this.modello + " è accesa");
  };

  this.descrivi = function () {
    console.log("Questa auto è una " + this.marca + " " + this.modello + " di colore " + this.colore);
  };

  this.stampa_anno = function () {
    console.log("L'anno di immatricolazione è: " + this.anno);
  };
};

let auto1 = new Automobile("Fiat", "500", "Rossa", "Elettrica", 2022);
let auto2 = new Automobile("Tesla", "Model 3", "Nera", "Elettrica", 2023);
let auto3 = new Automobile("Ford", "Mustang", "Blu", "Benzina", 1967);
let auto4 = new Automobile("Toyota", "Yaris", "Grigia", "Ibrida", 2021);
let auto5 = new Automobile("Alfa Romeo", "Giulia", "Verde", "Diesel", 2020);

auto1.accendi();
auto1.descrivi();
auto1.stampa_anno();

auto2.accendi();
auto2.descrivi();
auto2.stampa_anno();

auto3.accendi();
auto3.descrivi();
auto3.stampa_anno();

auto4.accendi();
auto4.descrivi();
auto4.stampa_anno();

auto5.accendi();
auto5.descrivi();
auto5.stampa_anno();
let Automobile = function() {
    this.persone = 0;
    this.velocita = 0;
    this.rapporto = 1;
    this.accesa = false;

    this.impostaPersone = function(n) {
        if (this.velocita === 0 && n >= 0 && n <= 5) {
            this.persone = n;
        }
    };

    this.impostaVelocita = function(v) {
        if (this.accesa === true && v >= 0 && v <= 180) {
            if (v <= this.velocita + 30 && v >= this.velocita - 30) {
                this.velocita = v;
            }
        }
    };

    this.aumentaRapporto = function() {
        if (this.accesa === true && this.rapporto < 6) {
            this.rapporto++;
        }
    };

    this.diminuisceRapporto = function() {
        if (this.accesa === true && this.rapporto > 1) {
            this.rapporto--;
        }
    };

    this.toggleAccensione = function() {
        if (this.accesa === true) {
            this.accesa = false;
            this.velocita = 0;
            this.rapporto = 1;
        } else {
            this.accesa = true;
        }
    };

    this.visualizzaStato = function() {
        console.log("Stato Auto:");
        console.log("- Accesa: " + this.accesa);
        console.log("- Persone: " + this.persone);
        console.log("- Velocità: " + this.velocita + " km/h");
        console.log("- Marcia: " + this.rapporto);
        console.log("---------------------------");
    };
};

let miaAuto = new Automobile();

miaAuto.toggleAccensione();
miaAuto.impostaPersone(3);
miaAuto.aumentaRapporto();
miaAuto.impostaVelocita(20);
miaAuto.visualizzaStato();

miaAuto.impostaVelocita(60); 
miaAuto.impostaVelocita(50);
miaAuto.visualizzaStato();

miaAuto.toggleAccensione();
miaAuto.visualizzaStato();
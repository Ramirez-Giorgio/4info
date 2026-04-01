function generaPitagorica(){
    let colonne = document.getElementById('colonne').value;    
    let tabella = document.getElementById('pitagorica');
    if(colonne < 4 || colonne >12){ // controllo che le colonne siano tra le 4 e 12
        alert("inserisci numero valido");
        return; // cosi che non esegue l'esercizio anche con numeri non validi
    }

    for(let r = 0; r <= colonne; r++){ //per creare le righe
        let riga = document.createElement('tr');
        tabella.append(riga);
        for(let c = 0; c <= colonne; c++){// per creare le colonne
            let cella = document.createElement('td')//crea il tag per l html
            if(r != 0 || c!= 0){
              cella.innerText = r*c;
                if(r == 0){
                    cella.innerText = c;   
                    cella.classList.add('header')
                }
                if(c == 0){
                    cella.innerText = r;   
                    cella.classList.add('header')
                }
            }
            riga.append(cella) // mette le celle nella riga
        }
    }   
}

function calcolaMultipli(){
    let numero = document.getElementById('numero').value;
    let tabella = document.getElementById('pitagorica');
    let righe = tabella.children;



    if(numero <= 0){
        alert("inserisci un numero positivo");
        return;
    }

    for(let r = 1; r < righe.length; r++ ){
        let riga = righe[r]
        let celle = riga.children;

        for(let c = 1; c < celle.length; c++){
            let cella = celle[c];
            let cellaValue = Number(cella.innerText) || 0;

                console.log(cellaValue)
            if(cellaValue % numero == 0){
                cella.classList.add('multiplo');
            }
        }
    }

}


function calcolaDivisori(){
let numero = document.getElementById('numero').value;
    let tabella = document.getElementById('pitagorica');
    let righe = tabella.children;



    if(numero <= 0){
        alert("inserisci un numero positivo");
        return;
    }

    for(let r = 1; r < righe.length; r++ ){
        let riga = righe[r]
        let celle = riga.children;

        for(let c = 1; c < celle.length; c++){
            let cella = celle[c];
            let cellaValue = Number(cella.innerText) || 0;

                console.log(cellaValue)
            if(cellaValue % numero == 0){
                cella.classList.add('divisore');
            }
        }
    }


}


// function generaPitagorica() {
//             let colonne = document.getElementById('colonne').value;
//             let tabella = document.getElementById('pitagorica');
//             tabella.innerHTML = ""; // pulizia tabella

//             if (colonne < 4 || colonne > 12) {
//                 alert("inserisci numero valido");
//                 return;
//             }

//             for (let r = 0; r <= colonne; r++) {
//                 let riga = document.createElement('tr');
//                 tabella.append(riga);

//                 for (let c = 0; c <= colonne; c++) {
//                     let cella = document.createElement('td');

//                     if (r === 0 && c === 0) {
//                         cella.innerText = "";
//                         cella.classList.add('header');
//                     } else if (r === 0) {
//                         cella.innerText = c;
//                         cella.classList.add('header');
//                     } else if (c === 0) {
//                         cella.innerText = r;
//                         cella.classList.add('header');
//                     } else {
//                         cella.innerText = r * c;
//                     }

//                     riga.append(cella);
//                 }
//             }
//         }


// function calcolaMultipli() {
//     let numero = Number(document.getElementById('numero').value);
//     let tabella = document.getElementById('pitagorica');
//     let righe = tabella.children;

//     if (numero <= 0) {
//         alert("inserisci un numero positivo");
//         return;
//     }

//     for (let r = 1; r < righe.length; r++) {
//         let celle = righe[r].children;

//         for (let c = 1; c < celle.length; c++) {
//             let cellaValue = Number(celle[c].innerText);

//             if (cellaValue % numero === 0) {
//                 celle[c].classList.add('multiplo');
//             }
//         }
//     }
// }


//         function calcolaDivisori() {
//             let numero = Number(document.getElementById('numero').value);
//             let tabella = document.getElementById('pitagorica');
//             let righe = tabella.children;

//             if (numero <= 0) {
//                 alert("inserisci un numero positivo");
//                 return;
//             }

//             for (let r = 1; r < righe.length; r++) {
//                 let celle = righe[r].children;

//                 for (let c = 1; c < celle.length; c++) {
//                     let cellaValue = Number(celle[c].innerText);

//                     if (cellaValue !== 0 && numero % cellaValue === 0) {
//                         celle[c].classList.add('divisore');
//                     }
//                 }
//             }
//         }
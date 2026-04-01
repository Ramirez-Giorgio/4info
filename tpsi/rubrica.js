function salva(){
    console.log('fun salva')
    let cognome = document.getElementById('cognome').value;
    let nome = document.getElementById('nome').value;
    let indirizzo = document.getElementById('indirizzo').value;
    let telefono = document.getElementById('telefono').value;
    let tabella = document.getElementById('tabella');
    console.log(cognome);
    console.log(nome);
    console.log(indirizzo);
    console.log(telefono);

    if(cognome == '' && 
        nome == '' &&
        indirizzo == '' &&
        telefono == ''
    ){
        alert("compila tutti i campi");
        return;
    }
    else{

        // creo le caselle e il tr per la riga
        const tr = document.createElement('tr');
        
        let id = new Date().getTime(); // id univoco
        tr.id = id;  //assegno l'id direttamente al tr

        const tdCognome = document.createElement('td')
        const tdNome = document.createElement('td')
        const tdNumero = document.createElement('td')
        const tdIndirizzo = document.createElement('td')
        const tdRimuovi = document.createElement('td')
        const buttonRimuovi = document.createElement('button')
        const hr = document.createElement('hr')
        

        // metto il testo dentro le caselle
        tdCognome.innerText = cognome;
        tdNome.innerText = nome;
        tdNumero.innerText = telefono;
        tdIndirizzo.innerText = indirizzo;
        buttonRimuovi.innerText = 'Rimuovi'; //metto rimuovi come testo interno
        buttonRimuovi.addEventListener('click',rimuovi); // gli metto la funzione dentro e lo metto onclick()
        buttonRimuovi.colspan = 2 //opzionale

        tdRimuovi.append(buttonRimuovi); //prima appendo il bottone dentro la casella

        // per inserire appendere
        tr.append(tdCognome)
        tr.append(tdNome)
        tr.append(tdIndirizzo)
        tr.append(tdNumero)
        tr.append(tdRimuovi);   //e poi appendo la casella alla riga
        tabella.append(tr);     //le caselle appese alla riga vengono appese a loro volta alla tabella
        tabella.append(hr)
    }
}

function rimuovi(id){
    console.log("funzione rimuovi");
    let riga = document.getElementById(id);
        riga.remove();
}


function cerca(){
    console.log('funzione cerca')
}

// function salva(){
//     let cognome = document.getElementById('cognome').value;   // prendo il cognome scritto
//     let nome = document.getElementById('nome').value;         // prendo il nome
//     let indirizzo = document.getElementById('indirizzo').value; // prendo l'indirizzo
//     let telefono = document.getElementById('telefono').value; // prendo il numero
//     let tabella = document.getElementById('tabella');         // prendo la tabella dove aggiungere le righe

//     // controllo se tutti i campi sono vuoti
//     if(cognome == '' && nome == '' && indirizzo == '' && telefono == ''){
//         alert("compila tutti i campi");   // avviso l'utente
//         return;                           // interrompo la funzione
//     } else {

//         const tr = document.createElement('tr');   // creo una nuova riga della tabella

//         let id = new Date().getTime();  // genero un ID unico basato sull'orario
//         tr.id = id;                     // assegno l'ID alla riga <tr>

//         // creo tutte le celle per la riga
//         const tdCognome = document.createElement('td');   // cella cognome
//         const tdNome = document.createElement('td');      // cella nome
//         const tdNumero = document.createElement('td');    // cella telefono
//         const tdIndirizzo = document.createElement('td'); // cella indirizzo
//         const tdRimuovi = document.createElement('td');   // cella per il bottone rimuovi
//         const buttonRimuovi = document.createElement('button'); // creo il bottone

//         // inserisco il testo nelle celle
//         tdCognome.innerText = cognome;     // metto cognome nella cella
//         tdNome.innerText = nome;           // metto nome
//         tdNumero.innerText = telefono;     // metto telefono
//         tdIndirizzo.innerText = indirizzo; // metto indirizzo
//         buttonRimuovi.innerText = 'Rimuovi'; // testo del bottone

//         // collego il bottone alla funzione rimuovi passando l'id della riga
//         buttonRimuovi.addEventListener('click',rimuovi);  // chiamo rimuovi(id) quando cliccato

//         tdRimuovi.append(buttonRimuovi); // metto il bottone dentro la cella

//         // aggiungo tutte le celle alla riga
//         tr.append(tdCognome);   // aggiungo cella cognome
//         tr.append(tdNome);      // aggiungo cella nome
//         tr.append(tdIndirizzo); // aggiungo cella indirizzo
//         tr.append(tdNumero);    // aggiungo cella telefono
//         tr.append(tdRimuovi);   // aggiungo cella bottone

//         tabella.append(tr);     // aggiungo la riga completa alla tabella
//     }
// }

// function rimuovi(el){ // el è l'oggetto su cui viene chiamata la funzione (in questo caso il pulsante)
//     const idPulsante = el.srcElement.id //prende l'id del bottone cliccato
//     let trRemove = document.getElementById(idPulsante)
//     trRemove.remove()
// }

// function cerca(){
//     console.log('funzione cerca');          // debug funzione cerca
// }

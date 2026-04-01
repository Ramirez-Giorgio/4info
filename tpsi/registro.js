// document.addEventListener("DOMContentLoaded",main);

// function ottieniOggetto(id){ 
//     return document.getElementById(id);
// }
// function ottieniOggetti(classe){ 
//     return document.getElementsByClassName(classe);
// }
// function creaOggetto(tag){ 
//     return document.createElement(tag);
// }

// function main(){
//     let Pulsante = ottieniOggetto("addStudente"); 
//     Pulsante.addEventListener("click",invio);   
// }

// function pulisciCampi(val1,val2){ 
//     val1.value ="";
//     val2.value ="";
// }

// function creaTabellaStudente(cognome,nome){
//     let body = document.getElementsByTagName("body")[0];
//     let studenteId = Date.now(); 

//     let tabellaStudente = creaOggetto("table");
//     let rigaStudente = creaOggetto("tr");
//     let nomeStudente = creaOggetto("td");
//     let Materia = creaOggetto("td");
//     let inputMateria = creaOggetto("input");
//     let Voto = creaOggetto("td");
//     let inputVoto = creaOggetto("input");
//     let invia = creaOggetto("td");
//     let Media = creaOggetto("td"); // 

    
//     nomeStudente.innerText = `${cognome} ${nome}`;
//     nomeStudente.classList.add("grassetto");

//     inputMateria.type = "text";
//     inputMateria.placeholder = "Materia";
//     inputVoto.type = "number";            
//     inputVoto.max = "10";
//     inputVoto.min = "2";
//     inputVoto.step = "0.5";
//     inputVoto.placeholder="Voto";
    
//     invia.innerText="Invia";
//     Media.innerText="Media";
//     invia.addEventListener("click",inviaVoto);
//     Media.addEventListener("click",calcolaMedia); 

//     tabellaStudente.classList.add(studenteId); 
//     invia.classList.add(studenteId);
//     invia.classList.add("pulsante");
//     Media.classList.add(studenteId);


//     Materia.append(inputMateria);
//     Voto.append(inputVoto);
//     rigaStudente.append(nomeStudente);
//     rigaStudente.append(Materia);
//     rigaStudente.append(Voto);
//     rigaStudente.append(invia);
//     rigaStudente.append(Media);
//     tabellaStudente.append(rigaStudente);
//     body.append(tabellaStudente);       
// }

// function invio(){
//     let cog = ottieniOggetto("inputCognome");
//     let nom = ottieniOggetto("inputNome");
    
//     if(cog.value == "" || nom.value == ""){
//         alert("Inserire tutti i campi");
//         return;
//     }
//     creaTabellaStudente(cog.value,nom.value);
//     pulisciCampi(cog,nom);
// }

// function inviaVoto(el){
//     let classe = el.srcElement.classList[0];            
//     let tabellaStudente = ottieniOggetti(classe)[0];    
//     let righe = tabellaStudente.children;
//     let CelleDiInput = righe[0].children;
//     let materia = CelleDiInput[1].children[0];
//     let voto = CelleDiInput[2].children[0];

//     if(materia.value =="" || voto.value==""){
//         alert("Per inserire un voto riempi tutti i campi di input");
//         return;
//     }
    
//     creaRigaVoto(materia.value,voto.value,tabellaStudente);
//     pulisciCampi(materia,voto);
// }

// function calcolaMedia(el){
//     let classe = el.srcElement.classList[0];
//     let tabellaStudente = ottieniOggetti(classe)[0];
//     let righe = tabellaStudente.children;
//     if(righe.length < 4){
//         alert("Attenzione, si può calcolare la media solo se si ha più di 1 voto");
//         return;
//     }
//     let media = calcola(righe);

//     let rigaMedia = tabellaStudente.querySelector("#cella-media"); 
//     if(rigaMedia){
//         rigaMedia.remove();
//     }
//     let riga = creaOggetto("tr");
//     let mediaTitolo = creaOggetto("td");
//     let mediaTd = creaOggetto("td");
    
//     riga.id="cella-media";
//     mediaTitolo.innerText="Media";
//     mediaTitolo.classList.add("grassetto");
//     mediaTitolo.colSpan="2";
//     mediaTd.innerText=`${media.toFixed(2)}`;
//     mediaTd.classList.add("grassetto");
//     mediaTd.colSpan="3";
    
//     riga.append(mediaTitolo);
//     riga.append(mediaTd);
//     tabellaStudente.append(riga);
// }

// function calcola(righe){ 
//     let somma = 0.0;
//     let cont = 0;
//     for(let i = 2;i<righe.length;i++){
//         let voto = righe[i].children[1];
//         somma += Number(voto.innerText);
//         cont++;
//     }
//     return somma/cont;
// }

// function creaRigaVoto(materiaVal,votoVal,tabella){ 
//     let righe = tabella.children;
//     if(Number(votoVal) == NaN){
//         alert("Voto non valido");
//         return;
//     }else if(Number(votoVal) < 2 || Number(votoVal) > 10){
//         alert("voto non valido");
//         return;
//     }
//     if(righe.length == 1){
//         aggiungiHeader(tabella); 
//     }

//     let materia = creaOggetto("td");
//     let voto = creaOggetto("td");
//     let riga = creaOggetto("tr");

//     materia.colSpan="2";
//     voto.colSpan="3";
//     materia.innerText=materiaVal;
//     voto.innerText=votoVal;

//     riga.append(materia);
//     riga.append(voto);
    
//     let rigaMedia = tabella.querySelector("#cella-media");
//     if(!rigaMedia){                                      
//         tabella.append(riga);
//     }else{
//         rigaMedia.parentNode.insertBefore(riga,rigaMedia) 
//     }

// }

// function aggiungiHeader(tabella){ 
//     let materia = creaOggetto("td");
//     let voto = creaOggetto("td");
//     let riga = creaOggetto("tr");

//     materia.colSpan="2";
//     voto.colSpan="3";
//     materia.innerText="Materia";
//     materia.classList.add("grassetto");
//     voto.innerText="Voto";
//     voto.classList.add("grassetto");

//     riga.append(materia);
//     riga.append(voto);
//     tabella.append(riga);
// }
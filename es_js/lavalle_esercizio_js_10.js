const utente = {
    nome: "Marco",
    titolo: "Il Supremo",
    livello: 99,
    linguaggio: "JavaScript"
};

const chiavi = Object.keys(utente);

for (let i = 0; i < chiavi.length; i++) {
    const chiaveCorrente = chiavi[i];         
    const valoreCorrente = utente[chiaveCorrente]; 
    
    console.log(`Proprietà: ${chiaveCorrente} -> Valore: ${valoreCorrente}`);
}
'''
Gruppo 2 - Sistema di gestione del magazzino di un negozio
Requisiti e richieste
Il gruppo dovrà sviluppare un programma che permetta la gestione del magazzino di un
negozio. Il sistema dovrà includere:
1. La registrazione di nuovi prodotti con nome, codice identificativo, quantità
disponibile e prezzo.
2. La possibilità di aggiornare la quantità di un prodotto in seguito a una vendita o a un
nuovo rifornimento.
3. La visualizzazione dell'inventario attuale.
4. La ricerca di un prodotto specifico nel magazzino.
'''
class gestione_Magazzino:
    def _init__(self):
        self.magazzino = []

    def aggiungi_prodotto(self,nome,codice,quantita,prezzo): #task 1
        if id_aggiunta in self.magazzino[codice]:
            print("Il prodotto è già presente nel magazzino")
        else:
            self.magazzino.append({
                nome: nome,
                codice: codice,
                quantita: quantita,
                prezzo: prezzo
            })

    def aggiorna_quantita(self,codice,quantita): #task 2
        if operazione == "Rifornimento":
            self.magazzino[codice][quantita] += variazione
        elif operazione == "Vendita":
            self.magazzino[codice][quantita] -= variazione
        else:
            print("Operazione non valida")

    def visualizza_inventario(self): #task 3
        visualizzazione_inventario = []
        for prodotto in self.magazzino:
            visualizzazione_inventario.append(prodotto)
        return visualizzazione_inventario
    
    def stampa_dettagli_ricerca(): #task 4
        for prodotto in dettagli_ricerca:
            print(prodotto)




magazzino = gestione_Magazzino()

while True:
    print("1. Aggiungi un prodotto al magazzino")
    print("2. Aggiorna la quantità di un prodotto")
    print("3. Visualizza l'inventario attuale")
    print("4. Cerca un prodotto nel magazzino tramite ID")
    print()
    print("5. Esci")
    print("-----------------------------")

    scelta = input("Seleziona un numero: ")

    if scelta == "1":
        id_aggiunta = input("Inserisci il codice identificativo del prodotto da aggiungere al magazzino: ")
        magazzino.aggiungi_prodotto(id_aggiunta,nome,codice,quantita,prezzo)
        print("Prodotto aggiunto al magazzino")

    elif scelta == "2":
        id_aggiornamento = input("Inserisci il codice identificativo del prodotto da aggiornare: ")
        if id_aggiornamento in self.maagazzino[codice]:
            operazione = input("Vuoi effettuare un rifornimento o una vendita? ")
            variazione = input("Inserisci la variazione: ")
        magazzino.aggiorna_quantita(id_aggiornamento,quantita, operazione, variazione)
        print("Quantità del prodotto aggiornata")

    elif scelta == "3":
        magazzino.visualizza_inventario(visualizzazione_inventario)
        for prodotto in visualizzazzione_inventario:
            print(prodotto)

    elif scelta == "4":
        dettagli_ricerca = []

        id_ricerca = input("Inserisci il codice identificativo del prodotto da cercare: ")

        if id_ricerca in self.magazzino[codice]:
            if prodotto[codice] == id_ricerca:
                dettagli_ricerca.append(prodotto)
            print("Prodotto trovato")
        else:
            print("Prodotto non trovato")
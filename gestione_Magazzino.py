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
        magazzino.aggiungi_prodotto(id_aggiunta, nome, codice, quantita, prezzo)
        print("Prodotto aggiunto al magazzino")
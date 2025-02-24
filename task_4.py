  
    def stampa_dettagli_ricerca(): #task 4
        for prodotto in dettagli_ricerca:
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

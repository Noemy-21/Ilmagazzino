class GestioneMagazzino:
    def __init__(self):
        self.magazzino = {}

    def aggiungi_prodotto(self, nome, codice, quantita, prezzo):  # Task 1

        if codice in self.magazzino:
            print("Il prodotto è già presente nel magazzino.") #!!! il controllo non funziona
        else:
            self.magazzino[codice] = {
                "nome": nome,
                "quantita": int(quantita),
                "prezzo": float(prezzo)
            }
            print("Prodotto aggiunto al magazzino.")

    def aggiorna_quantita(self, codice, operazione, variazione):  # Task 2
        if codice in self.magazzino:
            variazione = int(variazione)
            if operazione.lower() == "rifornimento":
                self.magazzino[codice]["quantita"] += variazione
            elif operazione.lower() == "vendita":
                if self.magazzino[codice]["quantita"] >= variazione:
                    self.magazzino[codice]["quantita"] -= variazione
                else:
                    print("Errore: Quantità insufficiente per la vendita.")
            else:
                print("Operazione non valida.")
        else:
            print("Prodotto non trovato nel magazzino.")

    def visualizza_inventario(self):  # Task 3
        if not self.magazzino:
            print("Il magazzino è vuoto.")
        else:
            for codice, prodotto in self.magazzino.items():
                print(f"Codice: {codice}, Nome: {prodotto['nome']}, Quantità: {prodotto['quantita']}, Prezzo: {prodotto['prezzo']:.2f}€")

    def cerca_prodotto(self, codice):  # Task 4
        if codice in self.magazzino:
            prodotto = self.magazzino[codice]
            print(f"Prodotto trovato: Codice: {codice}, Nome: {prodotto['nome']}, Quantità: {prodotto['quantita']}, Prezzo: {prodotto['prezzo']:.2f}€")
        else:
            print("Prodotto non trovato.")


magazzino = GestioneMagazzino()

while True:
    print("\n1. Aggiungi un prodotto al magazzino")
    print("2. Aggiorna la quantità di un prodotto")
    print("3. Visualizza l'inventario attuale")
    print("4. Cerca un prodotto nel magazzino tramite codice identificativo")
    print("5. Esci")
    print("-----------------------------")

    scelta = input("Seleziona un numero: ")

    if scelta == "1":
        codice = input("Inserisci il codice identificativo del prodotto: ")
        nome = input("Inserisci il nome del prodotto: ")
        quantita = input("Inserisci la quantità del prodotto: ")
        prezzo = input("Inserisci il prezzo del prodotto: ")
        magazzino.aggiungi_prodotto(nome, codice, quantita, prezzo)
    
    elif scelta == "2":
        codice = input("Inserisci il codice identificativo del prodotto da aggiornare: ")
        operazione = input("Vuoi effettuare un rifornimento o una vendita? ")
        variazione = input("Inserisci la variazione di quantità: ")
        magazzino.aggiorna_quantita(codice, operazione, variazione)
    
    elif scelta == "3":
        magazzino.visualizza_inventario()
    
    elif scelta == "4":
        codice = input("Inserisci il codice identificativo del prodotto da cercare: ")
        magazzino.cerca_prodotto(codice)
    
    elif scelta == "5":
        print("Uscita dal programma.")
        break
    
    else:
        print("Scelta non valida. Riprova.")

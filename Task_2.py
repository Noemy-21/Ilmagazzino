class gestione_Magazzino:
    def _init__(self):
        self.magazzino = []
    
    def aggiorna_quantita(self,codice,quantita): #task 2
        if operazione == "Rifornimento":
            self.magazzino[codice][quantita] += variazione
        elif operazione == "Vendita":
            self.magazzino[codice][quantita] -= variazione
        else:
            print("Operazione non valida")

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

 elif scelta == "2":
        id_aggiornamento = input("Inserisci il codice identificativo del prodotto da aggiornare: ")
        if id_aggiornamento in self.maagazzino[codice]:
            operazione = input("Vuoi effettuare un rifornimento o una vendita? ")
            variazione = input("Inserisci la variazione: ")
        magazzino.aggiorna_quantita(id_aggiornamento,quantita, operazione, variazione)
        print("Quantità del prodotto aggiornata")
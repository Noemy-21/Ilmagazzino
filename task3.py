def visualizza_inventario(self): #task 3
        visualizzazione_inventario = []
        for prodotto in self.magazzino:
            visualizzazione_inventario.append(prodotto)
        return visualizzazione_inventario

while True:
    print("1. Aggiungi un prodotto al magazzino")
    print("2. Aggiorna la quantità di un prodotto")
    print("3. Visualizza l'inventario attuale")
    print("4. Cerca un prodotto nel magazzino tramite ID")
    print()
    print("5. Esci")
    print("-----------------------------")

    scelta = input("Seleziona un numero: ")

elif scelta == "3":
        magazzino.visualizza_inventario(visualizzazione_inventario)
        for prodotto in visualizzazzione_inventario:
            print(prodotto)

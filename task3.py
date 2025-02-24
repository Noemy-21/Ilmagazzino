def visualizza_inventario(self):  # Task 3
        if not self.magazzino:
            print("Il magazzino è vuoto.")
        else:
            for codice, prodotto in self.magazzino.items():
                print(f"Codice: {codice}, Nome: {prodotto['nome']}, Quantità: {prodotto['quantita']}, Prezzo: {prodotto['prezzo']:.2f}€")

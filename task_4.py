  def cerca_prodotto(self, codice):  # Task 4
        if codice in self.magazzino:
            prodotto = self.magazzino[codice]
            print(f"Prodotto trovato: Codice: {codice}, Nome: {prodotto['nome']}, Quantità: {prodotto['quantita']}, Prezzo: {prodotto['prezzo']:.2f}€")
        else:
            print("Prodotto non trovato.")
   

class GestioneMagazzino:
    def __init__(self):
        self.magazzino = {}

    def aggiungi_prodotto(self, nome, codice, quantita, prezzo):  # Task 1

    # errore in Task 1 : se viene inserito un codice già presente nel magazzino, il prodotto viene aggiunto comunque

        if codice in self.magazzino:
            print("Il prodotto è già presente nel magazzino.") #!!! il controllo non funziona
        else:
            self.magazzino[codice] = {
                "nome": nome,
                "quantita": int(quantita),
                "prezzo": float(prezzo)
            }
            print("Prodotto aggiunto al magazzino.")





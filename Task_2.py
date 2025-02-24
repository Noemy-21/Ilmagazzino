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

def visualizza_inventario(self): #task 3
        visualizzazione_inventario = []
        for prodotto in self.magazzino:
            visualizzazione_inventario.append(prodotto)
        return visualizzazione_inventario



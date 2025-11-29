from tree import Tree


class BinaryTree(Tree):
    """
    Classe base astratta che rappresenta una struttura ad albero binario.
    """

    # ---------------------- metodi astratti addizionali ----------------------
    def left(self, p):
        """
        Restituisce una Position che rappresenta il figlio sinistro di 'p'.

        Restituisce None se 'p' non ha un figlio sinistro.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def right(self, p):
        """
        Restituisce una Position che rappresenta il figlio destro di 'p'.

        Restituisce None se 'p' non ha un figlio destro.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    # ---------- metodi concreti implementati in questa classe ----------
    def sibling(self, p):
        """
        Restituisce una Position che rappresenta il fratello di 'p' (o None se non è fratello).
        """
        parent = self.parent(p)
        if parent is None:                      # allora p è la radice
            return None                         # la radice non ha fratelli
        else:
            if p == self.left(parent):
                return self.right(parent)       # possibilmente None
            else:
                return self.left(parent)        # possibilmente None

    def children(self, p):
        """
        Restituisce un contenitore iterabile con i figli della posizione 'p'.
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

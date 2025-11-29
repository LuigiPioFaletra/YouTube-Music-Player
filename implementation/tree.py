class Tree:
    """
    Classe base astratta che rappresenta una struttura ad albero.
    """

    # ------------------------------- classe Position innestata -------------------------------
    class Position:
        """
        Un'astrazione che rappresenta la posizione di un singolo elemento.
        """

        def element(self):
            """
            Restituisce l'elemento memorizzato in questa Position.
            """
            raise NotImplementedError('Deve essere implementato dalla sottoclasse')

        def __eq__(self, other):
            """
            Restituisce True se 'other' Position rappresenta la stessa posizione.
            """
            raise NotImplementedError('Deve essere implementato dalla sottoclasse')

        def __ne__(self, other):
            """
            Restituisce True se 'other' non rappresenta la stessa posizione.
            """
            return not (self == other)      # opposto a __eq__

    # ---------- metodi astratti che la sottoclasse concreta deve supportare ----------
    def root(self):
        """
        Restituisce Position che rappresenta la radice dell'albero (None se è vuoto).
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def parent(self, p):
        """
        Restituisce Position che rappresenta il genitore di 'p' (None se 'p' è radice).
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def num_children(self, p):
        """
        Restituisce il numero di figli della Position p.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def children(self, p):
        """
        Restituisce un contenitore iterabile con i figli della posizione 'p'
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def __len__(self):
        """
        Restituisce il numero totale di elementi nell'albero.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    # ---------- metodi concreti implementati in questa classe ----------
    def is_root(self, p):
        """
        Restituisce True se la Position 'p' è la radice dell'albero.
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        Restituisce True se la Position 'p' non ha figli.
        """
        return self.num_children(p) == 0

    def is_empty(self):
        """
        Restituisce True se l'albero è vuoto.
        """
        return len(self) == 0

    def depth(self, p):
        """
        Restituisce il numero di livelli che separano la Position 'p' dalla radice.
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _heigh2(self, p):
        """
        Restituisce l'altezza del sottoalbero radicato in Position 'p'.
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._heigh2(c) for c in self.children(p))

    def heigh(self, p=None):
        """
        Restituisce l'altezza del sottoalbero radicato in Position 'p'.

        Se 'p' è None restituisce l'altezza dell'intero albero.
        """
        if p is None:
            p = self.root()
        return self._heigh2(p)

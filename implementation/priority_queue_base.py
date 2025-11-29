class PriorityQueueBase:
    """
    Classe di base astratta per una coda prioritaria.
    """

    # --------------------- classe Item innestata ---------------------
    class _Item:
        """
        Composito leggero per archiviare elementi della coda prioritaria
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):    # less-than comparison: specifica il criterio di confronto
            return self._key < other._key   # confronta gli elementi in base alle loro chiavi

    # -----------------------------------------------------------------
    def is_empty(self):
        """
        Restituisce True se la coda di priorità è vuota.
        """
        return len(self) == 0

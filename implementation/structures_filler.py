from random import randint
from probe_hash_map import ProbeHashMap
from heap import HeapPriorityQueue
from unsorted_table_map import UnsortedTableMap
from sorted_priority_queue import SortedPriorityQueue
import file_reader 

songs = file_reader.read_songs()
singers = file_reader.read_singers()
genres = file_reader.read_genres()
modified_genres = file_reader.read_modified_genres()
links = file_reader.read_links()
    

"""
Metodi utilizzati per riempire di dati le seguenti strutture:
- Tabella hash;
- Heap;
- Mappa;
- Coda prioritaria.
"""


def random_draw():
    """
    Crea una lista di numeri casuali da 0 alla lunghezza della lista di canzoni sottratto 1 e restituisce una lista
    di canzoni disposte casualmente, prelevandole da quella derivata dal file "songs.txt" e selezionandole dalle
    posizioni della stessa nel medesimo ordine con cui queste sono disposte nella lista di numeri casuali.
    """
    songs_positions_list, random_songs_list = [], []
    songs = file_reader.read_songs()

    while len(songs_positions_list) != len(songs):
        extracted_index = randint(0, len(songs) - 1)      # Estrazione casuale degli indici delle canzoni nella lista
        if extracted_index not in songs_positions_list:
            songs_positions_list.append(extracted_index)  # Aggiunta dell'indice alla lista degli indici estratti
    for i in range(0, len(songs)):
        random_songs_list.append(songs[songs_positions_list[i]])    # Inserimento canzoni in ordine come gli indici
    return random_songs_list


def find_songs(chosen_genre):
    """
    Restituisce la lista di canzoni del genere musicale scelto dall'utente.
    """
    genre_positions_list, founded_genres, founded_songs_list = [], [], []
    hash_map = hash_map_filling()
    modified_genres = file_reader.read_modified_genres()

    for i in range(0, len(modified_genres)):
        if chosen_genre in modified_genres[i]:      # Verifica presenza genere cercato nella lista dei generi modificati
            genre_positions_list.append(i)          # Aggiunta indici genere nella lista delle posizioni del genere
    for i in range(0, len(genre_positions_list)):
        founded_genres.append(modified_genres[genre_positions_list[i]])  # Aggiunta generi trovati nella propria lista
    for i in range(0, len(founded_genres)):
        founded_songs_list.append(hash_map.__getitem__(founded_genres[i]))  # Aggiunta valori hash map su lista finale
    return founded_songs_list


def hash_map_filling():
    """
    Crea e riempie una tabella hash. Inserisce:
    - Come chiavi i generi musicali modificati;
    - Come valori le posizioni all'interno della lista posizionale dei relativi link di YouTube.
    """
    _next = 0  # Variabile privata usata come indice per tenere conto delle posizioni dei link nella lista posizionale
    hash_map = ProbeHashMap()
    modified_genres = file_reader.read_modified_genres()

    for i in range(0, len(links)):
        if i == 0:
            hash_map.__setitem__(modified_genres[i], links.first())     # Aggiunta primo elemento lista e primo link
            _next = links.after(links.first())  # L'indice passa alla posizione del link successivo al primo
        elif i == len(links) - 1:
            hash_map.__setitem__(modified_genres[i], links.last())      # Aggiunta ultimo elemento lista e ultimo link
        else:
            hash_map.__setitem__(modified_genres[i], _next)
            _next = links.after(_next)  # L'indice passa alla posizione del link successivo a uno diverso dal primo
    return hash_map


def heap_filling():
    """
    Crea e riempie un heap. Inserisce:
    - Come chiavi i titoli delle canzoni;
    - Come valori i relativi cantanti.
    """
    heap = HeapPriorityQueue()
    for i in range(0, len(songs)):
        heap.add(songs[i], singers[i])          # Inserimento canzoni e cantanti dalle relative liste
    return heap


def sp_map_filling():
    """
    Crea e riempie una mappa. Inserisce:
    - Come chiavi i titoli delle canzoni;
    - Come valori le posizioni dei relativi link nella lista posizionale.
    """
    _next = 0  # Variabile privata usata come indice per tenere conto delle posizioni dei link nella lista posizionale
    sp_map = UnsortedTableMap()
    for i in range(0, len(links)):
        if i == 0:
            sp_map.__setitem__(songs[i], links.first())     # Aggiunta primo elemento lista e primo link
            _next = links.after(links.first())              # L'indice passa alla posizione del link successivo al primo
        elif i == len(links) - 1:
            sp_map.__setitem__(songs[i], links.last())      # Aggiunta ultimo elemento lista e ultimo link
        else:
            sp_map.__setitem__(songs[i], _next)
            _next = links.after(_next)  # L'indice passa alla posizione del link successivo a uno diverso dal primo
    return sp_map


def pg_map_filling():
    """
    Crea e riempie una mappa. Inserisce:
    - Come chiavi le posizioni dei link nella lista posizionale;
    - Come valori i relativi generi musicali.
    """
    _next = 0  # Variabile privata usata come indice per tenere conto delle posizioni dei link nella lista posizionale
    pg_map = UnsortedTableMap()
    genres = file_reader.read_genres()

    for i in range(0, len(links)):
        if i == 0:
            pg_map.__setitem__(links.first(), genres[i])    # Aggiunta primo elemento lista e primo link
            _next = links.after(links.first())              # L'indice passa alla posizione del link successivo al primo
        elif i == len(links) - 1:
            pg_map.__setitem__(links.last(), genres[i])     # Aggiunta ultimo elemento lista e ultimo link
        else:
            pg_map.__setitem__(_next, genres[i])
            _next = links.after(_next)  # L'indice passa alla posizione del link successivo a uno diverso dal primo
    return pg_map


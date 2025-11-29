from positional_list import PositionalList

"""
Metodi utilizzati per leggere informazioni dal file "songs.txt".
In particolare, vengono svolte operazioni di :
- Lettura di canzoni, attraverso il metodo "read_songs()";
- Lettura di cantanti, tramite il metodo "read_singers()";
- Lettura di generi musicali, mediante il metodo "read_genres()";
- Modifica di nomi dei generi musicali, grazie al metodo "read_modified_genres();
- Lettura di link di YouTube delle canzoni, con il metodo "read_links()".
"""
links_list = PositionalList()


def read_songs():
    """
    Legge il file "songs.txt" e inserisce ogni canzone in una lista.
    """
    songs_list = []
    in_file = open("songs.txt", "r")            # Apertura del file per lettura
    lines = in_file.readlines()                 # Lettura dell'intero file
    in_file.close()

    for line in lines:
        information = line.split(", ")          # Lista ottenuta dividendo i dati della riga considerata
        songs_list.append(information[0])       # Inserimento del primo dato della riga nella lista delle canzoni
    return songs_list


def read_singers():
    """
    Legge il file "songs.txt" e inserisce ogni cantante in una lista.
    """
    singers_list = []
    in_file = open("songs.txt", "r")            # Apertura del file per lettura
    lines = in_file.readlines()                 # Lettura dell'intero file
    in_file.close()

    for line in lines:
        information = line.split(", ")          # Lista ottenuta dividendo i dati della riga considerata
        singers_list.append(information[1])     # Inserimento del secondo dato della riga nella lista dei cantanti
    return singers_list


def read_genres():
    """
    Legge il file "songs.txt" e inserisce ogni genere musicale in una lista, ripetendo quelli già aggiunti.
    """
    genres_list = []
    in_file = open("songs.txt", "r")            # Apertura del file per lettura
    lines = in_file.readlines()                 # Lettura dell'intero file
    in_file.close()

    for line in lines:
        information = line.split(", ")          # Lista ottenuta dividendo i dati della riga considerata
        genres_list.append(information[2])      # Inserimento del terzo dato della riga nella lista dei generi
    return genres_list


def read_modified_genres():
    """
    Legge il file "songs.txt" e inserisce ogni genere musicale in una lista, ripetendo quelli
    già aggiunti e applicando delle modifiche ai nomi di tali generi per la codifica hash.
    """
    genres_list = read_genres()
    modified_genres_list = genres_list[:]       # Copia della lista dei generi, che dovranno essere modificati

    for i in range(0, len(modified_genres_list)):
        modified_genres_list[i] = modified_genres_list[i] + " - " + str(i + 1)  # Modifica del nome del genere
    return modified_genres_list


def read_link():
        """
        Legge il file "songs.txt" e inserisce ogni link di YouTube in una lista posizionale.
        """
        global links_list
        positions_list = []
         # Lista posizionale contenente i link di YouTube delle canzoni
        for line in open("songs.txt"):  # Scorrimento del file "songs.txt" per ricerca del carattere "," riga per riga
            for character_positions, character in enumerate(line):
                if character == ',':
                    positions_list.append(character_positions)  # Aggiunta valore posizione nella relativa lista
            links_list.add_last(line[positions_list[2] + 2:-1])  # Aggiunta link YouTube nella propria lista
            positions_list = []  # Svuotamento della lista con i valori delle posizioni delle "," nella riga

def read_links():
    global links_list
    return links_list
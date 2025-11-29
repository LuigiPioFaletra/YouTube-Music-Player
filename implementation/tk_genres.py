from tkinter import *
import structures_filler as sf
from queue1 import ArrayQueue as Aq
import reproduction
from unsorted_table_map import UnsortedTableMap as Ut
from center import center


def menu():
    """
    Metodo di creazione dell'interfaccia grafica per la scelta del genere.
    """
    global w, root, variable
    root = Tk()
    root.geometry('180x100')
    musical_genres_list = ["Blues", "Metal", "Country", "Dance", "Funky", "Hip Hop", "Jazz", "Pop", "Rap", "Rock"]
    variable = StringVar(root)
    variable.set('Blues')
    w = OptionMenu(root, variable, *musical_genres_list)
    w.pack()
    btn = Button(root, text='DONE', command=selected_item)
    btn.pack(side='bottom')
    center.center(root)

    root.mainloop()


def selected_item():
    """
    Metodo richiamato nel momento in cui viene premuto il bottone "done", che preleva il genere
    selezionato e richiama la funzione "find_songs", la quale ritorna tutte le canzoni di quel genere.
    """
    global variable
    position = sf.find_songs(str(variable.get()))
    root.destroy()
    reproduction.choices("position", position)

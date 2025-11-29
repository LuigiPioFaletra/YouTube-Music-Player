import reproduction
from tkinter import *
import structures_filler as sf
from queue1 import ArrayQueue as Aq
from unsorted_table_map import UnsortedTableMap as Ut
from center import center


def menu():
    """
    Metodo che manda in esecuzione l'interfaccia grafica che
    permette di selezionare le canzoni che si vogliono ascoltare.
    """
    global listbox, root, map
    map = sf.sp_map_filling()
    root = Tk()
    root.geometry('180x200')
    listbox = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
    i = 0
    for key in map.__iter__():
        listbox.insert(i, key)
        i = i+1
    btn = Button(root, text='DONE', command=selected_item)
    btn.pack(side='bottom')
    listbox.pack()
    center.center(root)

    root.mainloop()


def selected_item():
    """
    Metodo relativo al pulsante "done" che va a caricare le canzoni scelte all'interno della coda.
    """
    global listbox
    queue = Aq()
    for i in listbox.curselection():
        Aq.enqueue(queue, Ut.__getitem__(map, listbox.get(i)))
    root.destroy()
    reproduction.choices("coda", queue)

from cProfile import label
from os import remove
from time import sleep
from matplotlib.pyplot import text
from heap import HeapPriorityQueue as Hp
from request_data import RequestData as Rd
from statistics import data as St
import file_reader as rf
import reproduction
from positional_list import PositionalList
from tkinter import *
from request_data import RequestData as RD
import threading
from center import center


link = PositionalList()

"""
Classe relativa alla creazione della top 100 delle canzoni.
"""
heap = Hp()

def classification(data):
    """
    Metodo per creare una classificazione delle canzoni in base ai like e ai commenti delle stesse.
        """
    for_like = round(float(data._like / data._view * 100), 2)
    for_comment = round(float(data._comment / data._view * 100), 2)
    average = for_like * for_comment / 2
    priority = 100 - average
    return priority


def load():
    """
    Metodo che, attraverso la libreria "request", invia delle request che ritornato tutti i dati delle canzoni.
    """
    global link, text,heap
    link = rf.read_links()
    heap = Hp()
    Request = RD()
    position = PositionalList.first(link)
    sleep(2)
    for i in range(PositionalList.__len__(link)):
        if i % 3 == 0 :
            text['text'] = "Attendere"
        else:
            attendere = "Attendere" + i%3*"."
            text['text'] = attendere

        data = Rd.research(Request, position.element())
        priorità = classification(data)
        Hp.add(heap, priorità, position)
        position = PositionalList.after(link, position) 
    root.destroy()


def start():
    """
    Metodo che permette di inizializzare il thread e l'interfaccia grafica
    """
    start_new_thread()
    tk()


def tk():
    """
    Metodo che controlla l'interfaccia grafica 
    """
    global text, root, thread
    root = Tk() 
    root.rowconfigure(5, weight=15, minsize=100)
    root.columnconfigure(3, weight=10, minsize=75)    
                        
    topFrame = Frame(master=root,relief=RAISED, borderwidth=2)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM) 

    text = Label(topFrame,  text="Attendere", width=33 , height=4,  font=("Helvetica", 10))
    text.grid(columnspan = 3, row = 0) 
    center.center(root)

    root.mainloop()
    reproduction.choices("heap", heap)


def start_new_thread():
    """
    Metodo che inizializza e fa partitere il thread
    """
    global thread
    thread = threading.Thread(target= load)
    thread.start()




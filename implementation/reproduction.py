from logging import root
from msilib.schema import Media
from tkinter import *
from matplotlib.pyplot import pause
import file_reader as rf
from heap import HeapPriorityQueue as Hp
from linked_deque import LinkedDeque as Ld
from sorted_priority_queue import SortedPriorityQueue as Sp
from time import sleep
from queue1 import ArrayQueue as Aq
import vlc
import pafy
import urllib.request
import threading
from center import center


def play():
    """
    Metodo che manda in esecuzione l'interfaccia grafica del player con i relativi
    pulsanti che permettono di muoversi avanti e indietro nella coda prioritaria.
    """
    global button2, text, title, root
    root = Tk() 
    var = IntVar()
    root.rowconfigure(5, weight=15, minsize=100)
    root.columnconfigure(3, weight=10, minsize=75)
    topFrame = Frame(master=root, relief=RAISED, borderwidth=2)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    text = Label(topFrame, text=title, width=33, height=4, font=("Helvetica", 10))
    text1 = Label(topFrame, text='', width=33, height=3)
    button1 = Button(topFrame, text='<<', command=lambda: [var.set(1), backward()], width=12)
    button2 = Button(topFrame, text='||', command=lambda: [var.set(1), pause()], width=9)
    button3 = Button(topFrame, text='>>', command=lambda: [var.set(1), forward()], width=12)
    button4 = Button(topFrame, text='X', command=lambda: [var.set(1), back_to_tree()], width=12)
    text.grid(columnspan=3, row=0)
    text1.grid(columnspan=3, row=1)
    button1.grid(column=0, row=5)
    button2.grid(column=1, row=5)
    button3.grid(column=2, row=5)
    button4.grid(columnspan=3, row=6)
    center.center(root)

    root.mainloop()    


def backward():
    """
    Metodo relativo al pulsante "indietro" del player che permette di andare alla canzone precedente.
    """
    global queue, player, text, close
    close = FALSE
    thread.join()
    player.stop()
    queue = Ld.before(queue)
    control(Ld.position_element(queue))
    title = vlc_reproduction(Ld.position_element(queue))
    text['text'] = title
    button2['text'] = "||"
    player.play()


def forward():
    """
    Metodo relativo al pulsante "avanti" del player che permette di andare alla canzone successiva.
    """
    global queue, player, text, close
    close = FALSE
    thread.join()
    player.stop()
    queue = Ld.after(queue)
    control(Ld.position_element(queue))
    title = vlc_reproduction(Ld.position_element(queue))
    text['text'] = title
    button2['text'] = "||"
    player.play()


def pause():
    """
    Metodo relativo al pulsante "pausa" del player che permette di mettere in pausa la canzone che si sta ascoltando.
    """
    global player, button2, text
    if button2['text'] == "||":
        button2['text'] = ">"
        player.set_pause(1)
    elif button2['text'] == ">":
        button2['text'] = "||"
        player.set_pause(0)
    

def back_to_tree():
    """
    Metodo che permette di fermare il player.
    """
    global root, player, close
    close = FALSE
    root.destroy()
    player.stop()
    thread.join()
    return_tree()


def return_tree():
    """
    Metodo che richiama la classe ReTree la quale permette di richiamare nuovamente
    il decision tree per effettuare altre operazioni dipendenti dalle scelte dell'utente.
    """
    from decision_tree import ReTree
    ReTree.restart()


def control(element):
    """
    Metodo che ferma la riproduzione una volta giunti all'ultima canzone del player.
    """
    if element == "end":
        back_to_tree()


def choices(choice, data):
    """
    Metodo che permette d'inizializzare la coda con le relative canzoni in base alle scelte fatte.
    """
    global queue, player, text, title, close
    queue = Ld()
    player = vlc.MediaPlayer()
    if choice == "heap":
        for i in range(Hp.__len__(data)-1):
            item = Hp()
            item = Hp.remove_min(data)
            link = item[1]
            queue.insert_last(link.element())
    elif choice == "coda":
        for i in range(Aq.__len__(data)):
            item = Aq()
            item = Aq.dequeue(data)
            queue.insert_last(item.element())
    elif choice == "position":
        for link in data:
            queue.insert_last(link.element())
    elif choice == "priority":
        for i in range(Sp.__len__(data)):
            item = Sp()
            item = Sp.remove_min(data)
            link = item[1]
            queue.insert_last(link.element())
    queue.insert_last("end")
    queue = queue.first2()
    title = vlc_reproduction(Ld.position_element(queue))
    play()
 

def vlc_reproduction(url):
    """
    Metodo che permette, attraverso il modulo vlc, di far sentire la canzone all'utente.
    """
    global player, Media, flag, close
    flag = FALSE
    close = TRUE
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    title = best.title
        
    code = urllib.request.urlopen(url).getcode()
    if str(code).startswith('2') or str(code).startswith('3'):
        print('Stream is working')
    else:
        print('Stream is dead'),
 
    media = vlc.Media(playurl)
    player.set_media(media)

    vlc_manager = player.event_manager()
    vlc_manager.event_attach(vlc.EventType.MediaPlayerEndReached, waiting)

    player.play()

    start_new_thread()

    return str(title)


def waiting(event):
    """
    Metodo d'impostazione del processo di attesa in fase di attach dell'evento legato al riproduttore audio.
    """
    global flag
    flag = TRUE



def blocking_function():
    """
    Metodo che permette di riprodurre il brano successivo 
    """
    while close:
        if flag:
            forward()


def start_new_thread():
    """
    Funzione che permette la creazione di un thread eseguito in parallelo al programma
    """
    global thread
    thread = threading.Thread(target=blocking_function)
    thread.start()




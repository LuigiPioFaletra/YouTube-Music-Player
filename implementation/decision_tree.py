from multiprocessing.connection import wait
from typing_extensions import Self
from matplotlib.pyplot import flag
from pyparsing import col
from tree import Tree
from linked_binary_tree import LinkedBinaryTree as Lk
import top_100 as Tp
from tkinter import *
import file_reader as rf
from time import sleep
import tk_queue
import tk_genres
import shuffle_playback as sp
from center import center


class DecisionTree:
    """
    Classe che implementa il decision tree necessario per far scegliere all'utente cosa vuole ascoltare.
    """

    def loading(decision_tree):
        """
        Metodo che permette di andare a inizializzare il decision tree
        tramite le varie domande che vengono poste all'utente.
        """
        p = Lk._add_root(decision_tree, "Vuoi ascoltare un po' di musica?")
        p_right = Lk._add_right(decision_tree, p, "Vuoi ascoltare qualcosa nello specifico?")
        p_left = Lk._add_left(decision_tree, p, "Buona giornata")
        p = p_right
        p_right = Lk._add_right(decision_tree, p, "Vuoi scegliere un genere che ti piace?")
        p_left = Lk._add_left(decision_tree, p, "Vuoi sentire le top 100")
        p1 = p_right
        p = p_left
        p_right = Lk._add_right(decision_tree, p, "Top_100")
        p_left = Lk._add_left(decision_tree, p, "Vuoi attivare la riproduzione casuale?")
        p = p1
        p1 = p_left
        p_right = Lk._add_right(decision_tree, p, "Genres")
        p_left = Lk._add_left(decision_tree, p, "Vuoi scegliere tu le canzoni?")
        p2 = p_left
        p = p1
        p_right = Lk._add_right(decision_tree, p, "Ti piace la musica rilassante?")
        p_left = Lk._add_left(decision_tree, p, "Buona giornata")
        p = p_right
        p_right = Lk._add_right(decision_tree, p, "Shuffle_Playback - RL")
        p_left = Lk._add_left(decision_tree, p, "TI piace la musica movimentata?")
        p = p_left
        p_right = Lk._add_right(decision_tree, p, "Shuffle_Playback - MV")
        p_left = Lk._add_left(decision_tree, p, "Shuffle_Playback - CS")
        p = p2
        p_right = Lk._add_right(decision_tree, p, "Playlist")
        p_left = Lk._add_left(decision_tree, p, "Buona giornata")

    def tree(decision_tree):
        """
        Metodo che realizza l'interfaccia grafica del decision tree, in cui l'utente può rispondere alle relative
        domande attraverso due pulsanti "si" e "no". In base alla scelta dell'utente, si richiama la relativa classe.
        """
        global p, root, flag
        var = IntVar()
        root.rowconfigure(3, weight=15, minsize=100)
        root.columnconfigure(2, weight=10, minsize=75)
        topFrame = Frame(master=root, relief=RAISED, borderwidth=1)
        topFrame.pack()

        bottomFrame = Frame(root)
        bottomFrame.pack(side=BOTTOM)
        text = Label(topFrame, text='', width=40, height=4, fg='blue')
        text1 = Label(topFrame, text='', width=40, height=1, fg='blue')
        button1 = Button(topFrame, text='Si', fg='red', command=lambda: [var.set(1), DecisionTree.right()], width=20)
        button2 = Button(topFrame, text='No', fg='black', command=lambda: [var.set(1), DecisionTree.left()], width=20)
        text.grid(columnspan=2, row=0)
        text1.grid(columnspan=2, row=1)
        button1.grid(column=0, row=3)
        button2.grid(column=1, row=3)
        center.center(root)
        p = Lk.root(decision_tree)
        for i in range(Lk.__len__(decision_tree)):
            if p.element() == 'Top_100':
                root.destroy()
                Tp.start()
                break
            elif p.element() == 'Shuffle_Playback - RL':
                root.destroy()
                print("RL")
                sp.case("RL")
                break
            elif p.element() == 'Shuffle_Playback - MV':
                root.destroy()
                print("MV")

                sp.case("MV")
                break
            elif p.element() == 'Shuffle_Playback - CS':
                root.destroy()
                print("CS")

                sp.case("CS")
                break
            elif p.element() == 'Playlist':
                root.destroy()
                tk_queue.menu()
                break
            elif p.element() == 'Genres':
                root.destroy()
                tk_genres.menu()
                break
            elif p.element() == 'Buona giornata':
                root.destroy()
                exit()
            else:
                text['text'] = p.element()
                root.wait_variable(var)
        root.mainloop()

    def right():
        """
        Metodo relativa alla scelta "si".
        """
        global p
        p = Lk.right(decision_tree, p)

    def left():
        """
        Metodo relativo alla scelta "no".
        """
        global p
        p = Lk.left(decision_tree, p)

    def start():
        """
        Metodo d'inizializzazione del decision tree attraverso l'utilizzo della
        lista posizionale, con il caricamento dei link relativi alle canzoni.
        """
        global decision_tree, p, root, flag
        decision_tree = Lk()
        root = Tk()
        flag = TRUE
        DecisionTree.loading(decision_tree)
        DecisionTree.tree(decision_tree)
    
    


class ReTree:
    """
    Classe che permette di richiamare nuovamente il decision tree da altre classi.
    """

    def restart():
        """
        Metodo che fa ripartire il processo d'inizializzazione del decision tree.
        """
        DecisionTree.start()


if __name__ == "__main__":
    rf.read_link()
    DecisionTree.start()


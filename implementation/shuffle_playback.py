from asyncio.windows_events import NULL
import random
from requests import request
import structures_filler as sf
import file_reader
from request_data import RequestData as Rd
from sorted_priority_queue import SortedPriorityQueue as Sp
import reproduction
from unsorted_table_map import UnsortedTableMap


def case(choice):
    """
    Metodo di scelta delle canzoni del genere musicale scelto dall'utente.
    """
    shuffle = Sp()
    MV = ["Dance", "Metal", "Pop", "Rock", "Hip Hop", "Rap"]
    map = sf.pg_map_filling()
    links = file_reader.read_links()
    links2 = []
    Request = Rd()

    for link in links.iter2():
        links2.append(link)
    links3 = [len(links2)]

    for i in range(len(links2)):
        r = random.randint(0, len(links2)-1)

        if links2[r] not in links3:
            if choice == "MV": 
                if UnsortedTableMap.__getitem__(map, links2[r]) in MV:
                    rando2 = random.randint(0, links2.__len__()/2)
                else:
                    rando2 = random.randint(links2.__len__()/2, links2.__len__())
            elif choice == "RL":
                if map.__getitem__(links2[r]) not in MV:
                    rando2 = random.randint(0, links2.__len__()/2)
                else:
                    rando2 = random.randint(links2.__len__()/2, links2.__len__())
            elif choice == "CS":
                rando2 = random.randint(0, links2.__len__())
            Sp.add(shuffle, rando2, links2[r])
        links3.append(links2[r])
    reproduction.choices("priority", shuffle)

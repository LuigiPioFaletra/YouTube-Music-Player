import json
import requests
from statistics import data as Dt


class RequestData:
    """
    Classe per richiamare il video di YouTube associato alla canzone in esecuzione e le sue statistiche.
    """

    def get_data(self, video_id, part, api_key):
        """
        Metodo che invia delle richieste attraverso le API di Google per recuperare le statistiche relative al video.
        """
        url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0][part]
        except KeyError as e:
            print(f'Error! Could not get {part} part of data: \n{data}')
            data = dict()
        return data

    def search(self, string):
        """
        Metodo che permette di estrapolare dal link il codice relativo al video.
        """
        p1 = string.find("=")
        p2 = string.find("&ab_")
        if p2 == -1:
            substring = string[p1+1:]
        else:
            substring = string[p1+1:p2]
        return substring

    def research(self, string):
        """
        Metodo che richiama la richiesta dei dati e li va inserire nell'oggetto "data".
        """
        video_id = self.search(string)
        data = self.get_data(video_id, "statistics", "AIzaSyDeV1KZNR1vqjAQ19IMMfU_-C24RodC38U")
        data = Dt(int(data["viewCount"]), int(data["likeCount"]), int(data["commentCount"]))
        return data

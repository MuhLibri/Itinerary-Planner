from Itinerary import *

class LembarItinerary:
    def __init__(self):
        # Lembar itinerary berupa list dari itinerary
        self._lembarItinerary: list[Itinerary] = []

    # Menambahkan Itinerary ke lembarItinerary. Itinerary yang disimpan pada lembarItinerary belum diinsert ke tabel Itinerary
    def addLembarItinerary(self, idItinerary, waktuAwal, waktuAkhir, namaObjekWisata, idTransportasi):
        self._lembarItinerary.append(Itinerary(idItinerary, waktuAwal, waktuAkhir, namaObjekWisata, idTransportasi))

    @property
    # Mengembalikan lembarItinerary
    def lembarItinerary(self):
        return self._lembarItinerary
    
    @lembarItinerary.setter
    # Mengisi lembarItinerary yang disimpan dengan masukan lembarItinerary
    def lembarItinerary(self, lembarItinerary: list[Itinerary]):
        self._lembarItinerary = lembarItinerary

    # Menghapus Itinerary pada lembarItinerary
    def deleteItinerary(self, index):
        self._lembarItinerary.pop(index)

    # Mereset lembarItinerary
    def resetLembarItinerary(self):
        self._lembarItinerary = []
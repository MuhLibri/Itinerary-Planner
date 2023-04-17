from Database import *
from Itinerary import *


class ItineraryController:
    def __init__(self):
        # Lembar itinerary berupa list dari itinerary
        self.lembarItinerary : list[Itinerary] = []
    
    def addItinerary(self, idItinerary, waktuAwal, waktuAkhir, namaObjekWisata, idTransportasi):
        self.lembarItinerary.append(Itinerary(idItinerary, waktuAwal, waktuAkhir, namaObjekWisata, idTransportasi))

    def getLembarItinerary(self):
        return self.lembarItinerary
    
    def searchLembarItinerary(self, idItinerary):
        self.lembarItinerary = Database.search('Itinerary', IdItinerary=idItinerary)

    def insertItinerary(self):
        for itinerary in self.lembarItinerary:
            Database.insert('Itinerary', IdItinerary=itinerary.idItinerary, WaktuAwal=itinerary.waktuAwal, WaktuAkhir=itinerary.waktuAkhir, NamaObjekWisata=itinerary.namaObjekWisata, IdTransportasi=itinerary.idTransportasi)

    def close():
        connect.close()
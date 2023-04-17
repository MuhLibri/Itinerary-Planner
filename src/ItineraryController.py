from Itinerary import *
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "itinerary.db")
connect = sqlite3.connect(db_path)
cursor = connect.cursor()

class ItineraryController:
    def __init__(self):
        # Lembar itinerary berupa list dari itinerary
        self.lembarItinerary : list[Itinerary] = []
    
    def addItinerary(self, idItinerary, waktuAwal, waktuAkhir, objekWisata, transportasi):
        self.lembarItinerary.append(Itinerary(idItinerary, waktuAwal, waktuAkhir, objekWisata, transportasi))

    def getLembarItinerary(self):
        return self.lembarItinerary
    
    def searchLembarItinerary(self, idItinerary):
        with connect:
            cursor.execute("SELECT * FROM Itinerary WHERE IdItinerary=:IdItinerary", {'IdItinerary': idItinerary})
            tempList = cursor.fetchall()
        self.lembarItinerary = [Itinerary(x[0], x[1], x[2], x[3], x[4]) for x in tempList]

    def insertItinerary(self):
        with connect:
            for itinerary in self.lembarItinerary:
                cursor.execute("INSERT INTO Itinerary VALUES (:IdItinerary, :WaktuAwal, :WaktuAkhir, :NamaObjekWisata, :IdTransportasi)", {'IdItinerary':itinerary.idItinerary, 'WaktuAwal':itinerary.waktuAwal, 'WaktuAkhir':itinerary.waktuAkhir, 'NamaObjekWisata':itinerary.objekWisata, 'IdTransportasi':itinerary.transportasi})
                
    def close():
        connect.close()
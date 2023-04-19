from Riwayat import *
from ItineraryController import *
from Database import *


class RiwayatController:
    @staticmethod
    def updateCatatan(idItinerary, catatan):
        Database.update("Riwayat", {'IdItinerary':idItinerary}, Catatan=catatan)

    @staticmethod
    def deleteRiwayat(idItinerary):
        Database.delete("Riwayat", IdItinerary=idItinerary)

    @staticmethod
    def searchRiwayat(idItinerary):
        queryRiwayat = Database.search("Riwayat", IdItinerary=idItinerary)
        queryLembarItinerary = ItineraryController.searchLembarItinerary(idItinerary)
        riwayat = Riwayat(queryLembarItinerary, queryRiwayat[0][1], queryRiwayat[0][2])
        return riwayat
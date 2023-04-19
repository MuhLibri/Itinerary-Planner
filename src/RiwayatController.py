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
    
    @staticmethod
    def getListRiwayat():
        list = []
        queryRiwayat = Database.search("Riwayat")
        for i in range (len(queryRiwayat)):
            queryLembarItinerary = ItineraryController.searchLembarItinerary(queryRiwayat[i][0])
            list.append(Riwayat(queryLembarItinerary, queryRiwayat[i][1], queryRiwayat[i][2]))

        return list
    
    @staticmethod
    def getStartDate(riwayat: Riwayat):
        listDate = [i.waktuAwal for i in riwayat.lembarItinerary.lembarItinerary]
        return sorted(listDate, key = lambda d: datetime.datetime.strptime(d, '%d/%m/%Y'))[0]


    @staticmethod
    def getEndDate(riwayat: Riwayat):
        listDate = [i.waktuAkhir for i in riwayat.lembarItinerary.lembarItinerary]
        return sorted(listDate, key = lambda d: datetime.datetime.strptime(d, '%d/%m/%Y'), reverse=True)[0]

    @staticmethod
    def getDuration(riwayat: Riwayat):
        startDate = datetime.datetime.strptime(RiwayatController.getStartDate(riwayat), '%d/%m/%Y')
        endDate = datetime.datetime.strptime(RiwayatController.getEndDate(riwayat), '%d/%m/%Y')
        delta = endDate-startDate
        return delta.days + 1
    
    @staticmethod
    def getListObjekWisata(riwayat: Riwayat):
        return [elmt.namaObjekWisata for elmt in (riwayat.lembarItinerary.lembarItinerary)]
    
    @staticmethod
    def getDaerahItinerary(riwayat: Riwayat):
        query = Database.search("ObjekWisata", NamaObjekWisata=riwayat.lembarItinerary.lembarItinerary[0].namaObjekWisata)
        return ', '.join([*set(elmt[1] for elmt in query)])
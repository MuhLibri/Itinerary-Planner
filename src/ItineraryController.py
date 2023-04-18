from Database import *
from LembarItinerary import *
import datetime


class ItineraryController:
    @staticmethod
    # Membuat Id Itinerary baru. Menambahkan IdItinerary baru dan tanggal pembuatan ke tabel Riwayat
    def createIdItinerary():
        num = Database.count("Riwayat") + 1
        idItinerary = ((6 - len(str(num))) * '0') + str(num)
        Database.insert("Riwayat", IdItinerary=idItinerary, TanggalBuat=datetime.datetime.today(), Catatan='')
        return idItinerary

    @staticmethod
    # Mengembalikan lembar itinerary yang ada pada tabel Itinerary sesuai dengan IdItinerary
    def searchLembarItinerary(idItinerary):
        searchResult = Database.search('Itinerary', IdItinerary=idItinerary)
        lembarItinerary = LembarItinerary()
        lembarItinerary.lembarItinerary = [Itinerary(x[0], x[1], x[2], x[3], x[4]) for x in searchResult]
        return lembarItinerary

    @staticmethod
    # Memasukkan lembarItinerary ke tabel Itinerary
    def insertLembarItinerary(lembarItinerary: LembarItinerary):
        for itinerary in lembarItinerary.lembarItinerary:
            Database.insert('Itinerary', IdItinerary=itinerary.idItinerary, WaktuAwal=itinerary.waktuAwal, WaktuAkhir=itinerary.waktuAkhir, NamaObjekWisata=itinerary.namaObjekWisata, IdTransportasi=itinerary.idTransportasi)

    @staticmethod
    # Memasukkan Itinerary ke tabel Itinerary
    def insertItinerary(itinerary: Itinerary):
        Database.insert('Itinerary', IdItinerary=itinerary.idItinerary, WaktuAwal=itinerary.waktuAwal, WaktuAkhir=itinerary.waktuAkhir, NamaObjekWisata=itinerary.namaObjekWisata, IdTransportasi=itinerary.idTransportasi)

    @staticmethod
    # Mengupdate satu tuple pada tabel Itinerary dengan updateValue yang sesuai dengan targetItinerary
    def updateItinerary(targetItinerary: Itinerary, updateValue: Itinerary):
        Database.update("Itinerary", {'IdItinerary':targetItinerary.idItinerary, 'WaktuAwal':targetItinerary.waktuAwal}, IdItinerary=updateValue.idItinerary, WaktuAwal=updateValue.waktuAwal, WaktuAkhir=updateValue.waktuAkhir, NamaObjekWisata=updateValue.namaObjekWisata, IdTransportasi=updateValue.idTransportasi)

    @staticmethod
    # Menghapus satu tuple pada tabel Itinerary yang sesuai dengan targetItinerary
    def deleteItinerary(targetItinerary: Itinerary):
        Database.delete("Itinerary", IdItinerary=targetItinerary.idItinerary, WaktuAwal=targetItinerary.waktuAwal)

    @staticmethod
    # Membuat Itinerary baru dan memasukkannya ke tabel Itinerary
    def createNewItinerary(firstTime: bool, itinerary: Itinerary):
        if (firstTime):
            idItinerary = ItineraryController.createIdItinerary()
            itinerary.idItinerary = idItinerary
        
        ItineraryController.insertItinerary(itinerary)
        return itinerary.idItinerary
from Database import *
from Itinerary import *
from datetime import date


class ItineraryController:
    def __init__(self):
        # Lembar itinerary berupa list dari itinerary
        self._lembarItinerary : list[Itinerary] = []
    
    # Membuat lembar itinerary baru. Menambah IdItinerary baru dan tanggal buat ke tabel RIwayat
    @staticmethod
    def createItinerary():
        num = Database.count("Riwayat") + 1
        idItinerary = ((6 - len(str(num))) * '0') + str(num)
        Database.insert("Riwayat", IdItinerary=idItinerary, TanggalBuat=date.today(), Catatan='')

    # Mengembalikan lembar itinerary yang ada pada tabel Itinerary sesuai dengan IdItinerary
    @staticmethod
    def searchLembarItinerary(idItinerary):
        searchResult = Database.search('Itinerary', IdItinerary=idItinerary)
        return [Itinerary(x[0], x[1], x[2], x[3], x[4]) for x in searchResult]

    # Menambahkan Itinerary ke lembarItinerary. Itinerary yang disimpan pada lembarItinerary belum diinsert ke tabel Itinerary
    def addItinerary(self, idItinerary, waktuAwal, waktuAkhir, namaObjekWisata, idTransportasi):
        self._lembarItinerary.append(Itinerary(idItinerary, waktuAwal, waktuAkhir, namaObjekWisata, idTransportasi))

    # Mengembalikan lembarItinerary
    def getLembarItinerary(self):
        return self._lembarItinerary

    # Memasukkan lemarItinerary ke tabel Itinerary
    def insertItinerary(self):
        for itinerary in self._lembarItinerary:
            Database.insert('Itinerary', IdItinerary=itinerary.idItinerary, WaktuAwal=itinerary.waktuAwal, WaktuAkhir=itinerary.waktuAkhir, NamaObjekWisata=itinerary.namaObjekWisata, IdTransportasi=itinerary.idTransportasi)
class Itinerary:
    def __init__(self, idItinerary, waktuAwal, waktuAkhir, namaObjekWisata, idTransportasi):
        self._idItinerary = idItinerary
        self._waktuAwal = waktuAwal
        self._waktuAkhir = waktuAkhir
        self._namaObjekWisata = namaObjekWisata
        self._idTransportasi = idTransportasi
    
    @property
    def idItinerary(self):
        return self._idItinerary

    @property
    def waktuAwal(self):
        return self._waktuAwal
    
    @property
    def waktuAkhir(self):
        return self._waktuAkhir
    
    @property
    def namaObjekWisata(self):
        return self._namaObjekWisata
    
    @property
    def idTransportasi(self):
        return self._idTransportasi

    @idItinerary.setter
    def idItinerary(self, idItinerary):
        self._idItinerary = idItinerary

    @waktuAwal.setter
    def waktuAwal(self, waktuAwal):
        self._waktuAwal = waktuAwal

    @waktuAkhir.setter
    def waktuAkhir(self, waktuAkhir):
        self._waktuAkhir = waktuAkhir

    @namaObjekWisata.setter
    def namaObjekWisata(self, objekWisata):
        self._namaObjekWisata = objekWisata

    @idTransportasi.setter
    def idTransportasi(self, transportasi):
        self._idTransportasi = transportasi

    def __str__(self):
        return "Id Itinerary: " + self.idItinerary + "\nWaktu Awal: " + self.waktuAwal + "\nWaktu Akhir: " + self.waktuAkhir + "\nObjek Wisata: " + self.namaObjekWisata + "\nId Transportasi: " + self.idTransportasi
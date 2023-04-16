class Itinerary:
    def __init__(self, idItinerary, waktuAwal, waktuAkhir, objekWisata, transportasi):
        self._idItinerary = idItinerary
        self._waktuAwal = waktuAwal
        self._waktuAkhir = waktuAkhir
        self._objekWisata = objekWisata
        self._transportasi = transportasi
    
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
    def objekWisata(self):
        return self._objekWisata
    
    @property
    def transportasi(self):
        return self._transportasi

    @idItinerary.setter
    def idItinerary(self, idItinerary):
        self._idItinerary = idItinerary

    @waktuAwal.setter
    def waktuAwal(self, waktuAwal):
        self._waktuAwal = waktuAwal

    @waktuAkhir.setter
    def waktuAkhir(self, waktuAkhir):
        self._waktuAkhir = waktuAkhir

    @objekWisata.setter
    def objekWisata(self, objekWisata):
        self._objekWisata = objekWisata

    @transportasi.setter
    def transportasi(self, transportasi):
        self._transportasi = transportasi

    def __str__(self):
        return "IdItinerary: " + self.idItinerary + "\nWaktu Awal: " + self.waktuAwal + "\nWaktu Akhir: " + self.waktuAkhir + "\nObjek Wisata: " + self.objekWisata + "\nId Transportasi: " + self.transportasi
    
#Itinerary('000001', 'jam 1, 1 Mei 2023', 'jam 2, 1 Mei 2023', 'Candi Borobudur', '000007')
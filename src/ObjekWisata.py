from Daerah import *

class ObjekWisata(Daerah):
    def __init__(self, namaDaerah, informasiDaerah, namaObjekWisata, informasiObjekWisata):
        super().__init__(namaDaerah, informasiDaerah)
        self._namaObjekWisata = namaObjekWisata
        self._informasiObjekWisata = informasiObjekWisata

    @property
    def namaObjekWisata(self):
        return self._namaObjekWisata
    
    @property
    def informasiObjekWisata(self):
        return self._informasiObjekWisata
    
    @namaObjekWisata.setter
    def namaObjekWisata(self, namaObjekWisata):
        self._namaObjekWisata = namaObjekWisata
    
    @informasiObjekWisata.setter
    def informasiObjekWisata(self, informasiObjekWisata):
        self._informasiObjekWisata = informasiObjekWisata

    def __str__(self):
        return "Nama Objek Wisata: " + self._namaObjekWisata + "\nNama Daerah: " + self._namaDaerah + "\nInformasi: " + self._informasiObjekWisata
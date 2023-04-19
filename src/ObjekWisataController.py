from ObjekWisata import *
from Database import *

class ObjekWisataController:
    @staticmethod
    def getObjekWisata(namaObjekWisata):
        return Database.search("ObjekWisata", NamaObjekWisata=namaObjekWisata)
    
    @staticmethod
    def getObjekWisataInDaerah(namaDaerah):
        return Database.search("ObjekWisata", NamaDaerah=namaDaerah)
from Daerah import *
from Database import *

class DaerahController:
    @staticmethod
    def getDaerah(namaDaerah):
        return Database.search("Daerah", starts_with=True, NamaDaerah=namaDaerah)
    
    @staticmethod
    def getListDaerahWisata():
        daerahWisata = Database.search("ObjekWisata")
        daerahWisata = [*set([elmt[1] for elmt in daerahWisata])]
        return daerahWisata
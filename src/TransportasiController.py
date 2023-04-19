from Transportasi import *
from Database import *

class TransportasiController:
    def getTransportasi(lokasiBerangkat, lokasiTujuan):
        return Database.search("Transportasi", LokasiBerangkat=lokasiBerangkat, LokasiTujuan=lokasiTujuan)
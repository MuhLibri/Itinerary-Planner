from LembarItinerary import *

class Riwayat:
    def __init__(self, lembarItinerary, tanggalBuat, catatan):
        self._lembarItinerary = lembarItinerary
        self._tanggalBuat = tanggalBuat
        self._catatan = catatan

    @property
    def lembarItinerary(self):
        return self._lembarItinerary
    
    @property
    def tanggalBuat(self):
        return self._tanggalBuat
    
    @property
    def catatan(self):
        return self._catatan

    @lembarItinerary.setter
    def lembarItinerary(self, lembarItinerary):
        self._lembarItinerary = lembarItinerary
    
    @tanggalBuat.setter
    def tanggalBuat(self, tanggalBuat):
        self._tanggalBuat = tanggalBuat
    
    @catatan.setter
    def catatan(self, catatan):
        self._catatan = catatan
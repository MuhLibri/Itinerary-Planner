class Daerah:
    def __init__(self, namaDaerah, informasiDaerah):
        self._namaDaerah = namaDaerah
        self._informasiDaerah = informasiDaerah

    @property
    def namaDaerah(self):
        return self._namaDaerah
    
    @property
    def informasiDaerah(self):
        return self._informasiDaerah
    
    @namaDaerah.setter
    def namaDaerah(self, namaDaerah):
        self._namaDaerah = namaDaerah

    @informasiDaerah.setter
    def informasiDaerah(self, informasiDaerah):
        self._informasiDaerah = informasiDaerah

    def __str__(self):
        return "Nama Daerah: " + self._namaDaerah + "\nInformasi: " + self._informasiDaerah
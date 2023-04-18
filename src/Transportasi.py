class Transportasi:
    def __init__(self, idTransportasi, namaTransportasi, lokasiBerangkat, lokasiTujuan, harga):
        self._idTransportasi = idTransportasi
        self._namaTransportasi = namaTransportasi
        self._lokasiBerangkat = lokasiBerangkat
        self._lokasiTujuan = lokasiTujuan
        self._harga = harga

    @property
    def idTransportasi(self):
        return self._idTransportasi
    
    @property
    def namaTransportasi(self):
        return self._namaTransportasi
    
    @property
    def lokasiBerangkat(self):
        return self._lokasiBerangkat
    
    @property
    def lokasiTujuan(self):
        return self._lokasiTujuan
    
    @property
    def harga(self):
        return self._harga
    
    @idTransportasi.setter
    def idTransportasi(self, idTransportasi):
        self._idTransportasi = idTransportasi
    
    @namaTransportasi.setter
    def namaTransportasi(self, namaTransportasi):
        self._namaTransportasi = namaTransportasi
    
    @lokasiBerangkat.setter
    def lokasiBerangkat(self, lokasiBerangkat):
        self._lokasiBerangkat = lokasiBerangkat
    
    @lokasiTujuan.setter
    def lokasiTujuan(self, lokasiTujuan):
        self._lokasiTujuan = lokasiTujuan
    
    @harga.setter
    def harga(self, harga):
        self._harga = harga

    def __str__(self):
        return "Id Transportasi: " + self._idTransportasi + "\nNama Transportasi: " + self._namaTransportasi + "\nLokasi Berangkat: " + self._lokasiBerangkat + "\nLokasi Tujuan: " + self._lokasiTujuan + "\nHarga: " + self._harga
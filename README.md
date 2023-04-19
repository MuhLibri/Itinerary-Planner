# IF2250-2023-K01-14-ItineraryPlanner



# Daftar Tabel
1. Tabel Daerah

|Atribut               |Tipe      |Boleh Null |
| ------               | ------   | ------    |
|NamaDaerah            |TEXT      |Tidak      |
|InformasiDaerah       |TEXT      |Boleh      |

2. Tabel ObjekWisata

|Atribut               |Tipe      |Boleh Null   |
| ------               | ------   | ------      |
|NamaObjekWisata       |TEXT      |Tidak        |
|NamaDaerah            |TEXT      |Tidak        |
|InformasiObjekWisata  |TEXT      |Boleh        |

3. Tabel Transposi

|Atribut               |Tipe      |Boleh Null   |
| ------               | ------   | ------      |       
|IdTransportasi        |TEXT      |Tidak        |
|NamaTransportasi      |TEXT      |Tidak        |
|LokasiBerangkat       |TEXT      |Tidak        |
|LokasiTujuan          |TEXT      |Tidak        |
|Harga                 |INTEGER   |Tidak        |

4. Tabel Itinerary

|Atribut               |Tipe      |Boleh Null   |
| ------               | ------   | ------      |
|IdItinerary           |TEXT      |Tidak        |
|WaktuAwal             |TEXT      |Tidak        |
|WaktuAkhir            |TEXT      |Tidak        |
|NamaObjekWisata       |TEXT      |Tidak        |
|IdTransportasi        |TEXT      |Tidak        |

5. Tabel Riwayat

|Atribut               |Tipe      |         |
| ------               | ------   | ------  |
|IdItinerary           |TEXT      |Tidak    |
|TanggalBuat           |TEXT      |Tidak    |
|Catatan               |TEXT      |Boleh    |

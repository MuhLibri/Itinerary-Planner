# IF2250-2023-K01-14-ItineraryPlanner



# Daftar Tabel
1. Tabel Daerah

| Atribut              |Tipe      | Atribut |Tipe    |
| ------               | ------   | ------  | ------ |
|NamaDaerah            |TEXT      |Tidak    |        |
|InformasiDaerah       |TEXT      |Boleh    |        |

2. Tabel ObjekWisata
| Atribut              |Tipe      | Atribut |Tipe    |
| ------               | ------   | ------  | ------ |
|NamaObjekWisata       |TEXT      |Tidak    |        |
|NamaDaerah            |TEXT      |Tidak    |        |
|InformasiObjekWisata  |TEXT      |Boleh    |        |

3. Tabel Transposi
| Atribut              |Tipe      | Atribut |Tipe    |
| ------               | ------   | ------  | ------ |
|IdTransportasi        |TEXT      |Tidak    |        |
|NamaTransportasi      |TEXT      |Tidak    |        |
|LokasiBerangkat       |TEXT      |Tidak    |        |
|LokasiTujuan          |TEXT      |Tidak    |        |
|Harga                 |INTEGER   |Tidak    |        |

4. Tabel Itinerary
| Atribut              |Tipe      | Atribut |Tipe    |
| ------               | ------   | ------  | ------ |
|IdItinerary           |TEXT      |Tidak    |        |
|WaktuAwal             |TEXT      |Tidak    |        |
|WaktuAkhir            |TEXT      |Tidak    |        |
|NamaObjekWisata       |TEXT      |Tidak    |        |
|IdTransportasi        |TEXT      |Tidak    |        |

5. Tabel Riwayat
| Atribut              |Tipe      | Atribut |Tipe    |
| ------               | ------   | ------  | ------ |
|IdItinerary           |TEXT      |Tidak    |        |
|TanggalBuat           |TEXT      |Tidak    |        |
|Catatan               |TEXT      |Boleh    |        |

# IF2250-2023-K01-14-ItineraryPlanner

# Tentang ItineraryPlanner
    Aplikasi ItineraryPlanner, merupakan aplikasi dengan lingkup personal yang dibuat untuk merancang jadwal liburan. Aplikasi ini dapat menampilkan list destinasi wisata serta semua objek wisata yang ada pada destinasi wisata tersebut. Aplikasi juga dapat menampilkan semua moda transportasi yang tersedia beserta harganya untuk menuju ke destinasi wisata. Dengan menggunakan fitur-fitur tersebut, ItineraryPlanner dapat digunakan untuk merancang rencana perjalanan untuk pengguna. Selain itu, rencana perjalanan yang telah dibuat dapat disimpan sebagai riwayat perjalanan dan dapat dilihat kembali oleh pengguna. Pengguna juga dapat menambahkan catatan pribadi pada riwayat tersebut.

# Requirement
Sebelum menjalankan aplikasi ItineraryPlanner, pengguna harus menginstall terlebih dahulu menginstall python dan PyQt

# Cara menjalankan
Untuk menjalankan aplikasi ItineraryPlanner, pengguna cukup membuka terminal pada folder src. Lalu, pengguna dapat mengetikkan ```python StartPage.py``` dan aplikasi pun dapat berjalan.

# Modul dan Pembagian Kerja


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

import sqlite3
import os.path
from Itinerary import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "itinerary.db")
connect = sqlite3.connect(db_path)
cursor = connect.cursor()


class Database:
    @staticmethod
    def insert(table: str, **attr):
        """
        table is the target table on database, **attr are the values to be inserted to the table
        example: insert('Riwayat', IdItinerary='000001', TanggalBuat='27/05/2023', Catatan='Asik')
        """
        with connect:
            if (table == "Itinerary"):
                cursor.execute("""INSERT INTO Itinerary VALUES 
                    (:IdItinerary, :WaktuAwal, :WaktuAkhir, :NamaObjekWisata, :IdTransportasi)""", 
                    {'IdItinerary':attr['IdItinerary'], 'WaktuAwal':attr['WaktuAwal'], 'WaktuAkhir':attr['WaktuAkhir'], 'NamaObjekWisata':attr['NamaObjekWisata'], 'IdTransportasi':attr['IdTransportasi']})
    
    @staticmethod
    def search(table: str, **attr):
        with connect:
            if (table == "Itinerary"):
                cursor.execute("SELECT * FROM Itinerary WHERE IdItinerary=:IdItinerary", {'IdItinerary': attr['IdItinerary']})
                retVal = [Itinerary(x[0], x[1], x[2], x[3], x[4]) for x in cursor.fetchall()]

        return retVal

    @staticmethod   
    def close():
        connect.close()
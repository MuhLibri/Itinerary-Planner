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
            attrs = ','.join([':'+s for s in attr.keys()])
            cursor.execute("INSERT INTO {} VALUES ({})".format(table, attrs), attr)
    
    
    @staticmethod
    def search(table: str, **attr):
        with connect:
            attrs = ','.join([s+'=:'+s for s in attr.keys()])
            cursor.execute("SELECT * FROM {} WHERE {}".format(table, attrs), attr)

        if table=='Itinerary':
            retVal = [Itinerary(x[0], x[1], x[2], x[3], x[4]) for x in cursor.fetchall()]
        elif table=='ObjekWisata':
            retVal = []

        return retVal


    @staticmethod   
    def close():
        connect.close()

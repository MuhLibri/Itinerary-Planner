import sqlite3
import os.path


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
        retVal = "Query not found"
        with connect:
            attrs = ','.join([s+'=:'+s for s in attr.keys()])
            cursor.execute("SELECT * FROM {} WHERE {}".format(table, attrs), attr)

        retVal = cursor.fetchall()
        return retVal
    

    @staticmethod
    def count(table: str):
        cursor.execute("SELECT COUNT(*) FROM {}", table)
        return cursor.fetchone()[0]


    @staticmethod
    def count(table: str):
        cursor.execute("SELECT COUNT(*) FROM {}", table)
        return cursor.fetchone()[0]

    @staticmethod   
    def close():
        connect.close()

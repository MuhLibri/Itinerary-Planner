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
    def update(table: str, **attr):
        with connect:
            modifiedAttribute = ','.join([s+'=:'+s for s in attr.keys()])
            index = modifiedAttribute.find(',')
            Condition = modifiedAttribute[0:index]
            modifiedAttribute = modifiedAttribute[index+1:len(modifiedAttribute)]
            cursor.execute("UPDATE {} SET {} WHERE {}".format(table, modifiedAttribute, Condition), attr)   


    @staticmethod
    def delete(table: str, **attr):
        with connect:
            attrs = ','.join([s+'=:'+s for s in attr.keys()])
            cursor.execute("DELETE FROM {} WHERE {}".format(table, attrs), attr)


    @staticmethod
    def search(table: str, **attr):
        with connect:
            if (bool(attr)):
                attrs = ','.join([s+'=:'+s for s in attr.keys()])
                cursor.execute("SELECT * FROM {} WHERE {}".format(table, attrs), attr)
            else:
                cursor.execute("SELECT * FROM {}".format(table))
        retVal = cursor.fetchall()
        return retVal


    @staticmethod
    def crossproduct(*tables):
        with connect:
            q = ','.join(tables)
            print(q)
            cursor.execute(f"SELECT * FROM {q}")
        retVal = cursor.fetchall()
        return retVal


    @staticmethod
    def naturaljoin(*tables):
        with connect:
            q = ' NATURAL INNER JOIN '.join(tables)
            cursor.execute(f"SELECT * FROM {q}")
        retVal = cursor.fetchall()
        return retVal


    @staticmethod
    def count(table: str):
        cursor.execute("SELECT COUNT(*) FROM {}".format(table))
        return cursor.fetchone()[0]


    @staticmethod   
    def close():
        connect.close()

print(Database.naturaljoin("Daerah", "ObjekWisata", "Transportasi"))
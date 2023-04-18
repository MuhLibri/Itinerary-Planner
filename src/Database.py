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
    def update(table: str, dict: dict, **attr):
        """
        table is the target table on database, dict are the conditions of the target, **attr are the values to be updated in the table
        example: update('Riwayat', {'IdItinerary':'000001'}, IdItinerary='000002', Catatan='hai')
        """
        with connect:
            condition = ' AND '.join([a + '=' + "'{}'".format(b) for a,b in dict.items()])
            modifiedAttribute = ','.join([s+'=:'+s for s in attr.keys()])
            cursor.execute("UPDATE {} SET {} WHERE {}".format(table, modifiedAttribute, condition), attr) 


    @staticmethod
    def delete(table: str, **attr):
        """
        table is the target table on database, **attr are the conditions for the tuple to be deleted in the table
        example: delete('Riwayat', IdItinerary='000001')
        """        
        with connect:
            attrs = ' AND '.join([s+'=:'+s for s in attr.keys()])
            cursor.execute("DELETE FROM {} WHERE {}".format(table, attrs), attr)


    @staticmethod
    def search(table: str, ignore_case: bool = False, starts_with: bool = False, contains: bool = False, **attr):
        """
        table is the target table on database, **attr are the conditions of the tuple in the table to be returned (can be empty)
        example: search('Riwayat', IdItinerary='000001')        
        """
        with connect:
            ignore_case_q = ""
            if (bool(attr)):
                if starts_with or contains:
                    attrs = ' AND '.join([s+' LIKE "'+'%'*contains+attr[s]+'%"' for s in attr.keys()])
                    print(attrs)
                else:
                    ignore_case_q = ignore_case*" COLLATE NOCASE"
                    attrs = ','.join([s+'=:'+s for s in attr.keys()])
                
                cursor.execute("SELECT * FROM {} WHERE {} {}".format(table, attrs, ignore_case_q), attr)
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
    def count(table: str, ignore_case: bool = False, **attr):
        """
        table is the target table on database, **attr are the conditions of the tuple in the table to be counted (can be empty)
        example: count('Itinerary', IdItinerary='000001')
        """
        if (bool(attr)):
            ignore_case_q = ignore_case*" COLLATE NOCASE"
            attrs = ','.join([s+'=:'+s for s in attr.keys()])
            cursor.execute("SELECT COUNT(*) FROM {} WHERE {} {}".format(table, attrs, ignore_case_q), attr)
        else:
            cursor.execute("SELECT COUNT(*) FROM {}".format(table))
        return cursor.fetchone()[0]


    @staticmethod
    def close():
        connect.close()

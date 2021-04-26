
import sqlite3 as sqdb


def createDataBase():
    conn = sqdb.connect("BUFFUR_DB.db")
    return conn
    
def connectDataBase():
    conn = sqdb.connect("BUFFUR_DB.db")
    return conn

def createTable(conn):
    conn.execute("Create table BUFFUR_DB(ID number, TITLE TEXT , NEWS TEXT, CLASS NUMBER primary key(ID, TITLE));")
    conn.commit()
    return conn

def DataLastID(conn):
    cursor = conn.execute("select * from BUFFUR_DB;")
    ID = 0
    for r in cursor:
        ID = r[0]
    return ID

def putDatainBuffer(conn, TITLE, NEWS, CLASS):
    ID = DataLastID(conn)+1
    st = '''insert into BUFFUR_DB(ID, TITLE, NEWS, CLASS) values(%s, """%s""", """%s""", %s);'''%(ID, TITLE, NEWS, CLASS)
    print(st)
    conn.execute(st)
    conn.commit()
    return conn
    
def getDataFromDataBase(conn):
    cursor = conn.execute("select * from BUFFUR_DB;")
    for r in cursor:
        print(">> ", r)
        print("\n\n\n")

def getDataForTraining(conn):
    limit = 10000
    train_data = []
    cursor = conn.execute("select * from BUFFUR_DB;")
    for row in cursor:
        train_data.append(row)
    length = len(train_data)
    if length > limit:
        return train_data[-limit:][::-1]
    return train_data[::-1]



#conn = createDataBase()

conn = connectDataBase()
#conn = createTable(conn)
# print(DataLastID(conn))

#dataInserted = [['title1', 'news1', 0], ['title2', 'news2', 1]]
'''
for item in dataInserted:
    t, n, c = item[0], item[1], item[2]
    conn = putDatainBuffer(conn, t, n, c)
'''
getDataFromDataBase(conn)





#conn.close()




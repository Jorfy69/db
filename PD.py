import sqlite3 as sql3
from sqlite3 import Error

#creating the data base
def createdb(databasename):
    
    try:
        conn = sql3.connect(databasename + '.db')
        print(f'DATABASE MADE IN: {sql3.version}')

    except Error as e:
        print(e)

    finally:
        conn.close()

def addtable(databasename,tablename,param):

    try:
        conn = sql3.connect(databasename + '.db')
        cursor = conn.cursor()
        cursor.execute(f'''DROP TABLE IF EXISTS {tablename}''')
        cursor.execute(f'CREATE TABLE [{tablename}]([{param[0]}] [{param[1]}], [{param[2]}] [{param[3]}])')
        print('[TABLE MADE]')

    except Error as e:
        print(e)

    finally:
        conn.commit()
        conn.close()

def removetable(databasename, tablename):

    try:

        conn = sql3.connect(databasename + '.db')
        cursor = conn.cursor()
        cursor.execute(f'DROP TABLE [{tablename}]')
        print('[TABLE DROPED]')

    except Error as e:
        print(e)

    finally:
        conn.commit()
        conn.close()
#using the databases
def insertdata(databasename, tablename,param,data):

    try:

        conn = sql3.connect(databasename + '.db')
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO [{tablename}]([{param[0]}], [{param[1]}]) Values('[{data[0]}]', '[{data[1]}]' );""")

    except Error as e:
        print(e)

    finally:
        conn.commit()
        conn.close()

def pulldata(databasename,tablename):
    
    try:
        
        conn = sql3.connect(databasename + '.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM [{tablename}]')
        info = cursor.fetchall()
        info_string = "\n".join([str(i) for i in info])
                       
        with open('Table Results.txt', 'a') as f:
            
            f.write(info_string)
            f.close()

    except Error as e:
        print(e)
   
    finally:
        conn.close()
    
def main():
   
   whattodo = input('What do you want to do: ')
   
   if whattodo.lower() == 'create database':
   
       dbname = input('What is the name of your database: ')
   
       createdb(dbname)
       print("[DATABASE MADE]")
   
   elif whattodo.lower() == 'add table':
   
       dbname = input('What database do u want to add the table to: ')
       tablename = input('What do you want the table to be called:  ')
       paramaterslist = input('What paramatars do u want in ur table: ').split()
   
       addtable(dbname, tablename, paramaterslist)
   
   elif whattodo.lower() == 'remove table':
   
       dbname = input('What database do u want to remove the table from: ')
       tablename = input('What table do you want to remove:  ')
   
       removetable(dbname, tablename)
   
   elif whattodo.lower() == 'insert data':
   
       dbname = input('Databasename: ')
       tablename = input('Tablename: ')
       tableparams = input('Table Parameters: ').split()
       data = input('Data: ').split()
       
       insertdata(dbname,tablename,tableparams,data)
   
   elif whattodo.lower() == 'pull data':
       
       dbname = input('Databasename: ')
       tablename = input('Tablename:')
       
       pulldata(dbname, tablename)
   elif whattodo.lower() == 'help':
        print('[Avalible Commands]\nCreate database: Makes a new database, to user specifications\n\nAdd Table: Adds a table to the database of users choice\n\nRemove table: Removes a table from a database that the user has chossen\n')
        print('Insert data: Puts data in to the desired table and database that the user chooses\n\nPull data: Take data from the selected table and writes it to a .txt file\n')
   else:
    print('Invlid command')
    
while __name__ == '__main__':

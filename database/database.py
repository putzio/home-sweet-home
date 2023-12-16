import mysql.connector  

DATABASE_NAME = "homeDB"

class Databse:
    def init(self, host = "localhost", user = "user", password = "password", db_name = "homeDB"):
        #Create the connection object   
        self.__myconn = mysql.connector.connect(host = host, user = user,passwd = password)
        self.__cur = self.__myconn.cursor()
        self.db_name = db_name
        self.__create_database()
        self.__myconn.database = self.db_name
    
    def __create_database(self):
        try:
            self.__cur.execute(f"show databases")
            dbs = self.__cur.fetchall() 
            if any(self.db_name  in db for db in dbs):
                print("Database already exists")
            else:
                #creating a new database  
                self.__cur.execute(f"create database {DATABASE_NAME}")  
                print("Database created successfully")
        except Exception as e:
            print(e)

    def create_table(self, table_name, columns):
        try:
            self.__cur.execute(f"show tables")
            tables = self.__cur.fetchall() 
            if any(table_name  in table for table in tables):
                print("Table already exists")
            else:
                #creating a new table  
                self.__cur.execute(f"create table {table_name} ({columns})")  
                print("Table created successfully")
        except Exception as e:
            print(e)
    
    def insert(self, table_name, columns, values):
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        try:
            self.__cur.execute(sql)
            self.__myconn.commit()
            print("Record inserted successfully")
        except Exception as e:
            print(e)
            # self.__myconn.rollback()
        print("table:")
        self.__cur.execute(f"SELECT * FROM {table_name}")
        for x in self.__cur:
            print(x)

    def __del__(self):
        self.__myconn.close()
        print("Database connection closed")


if __name__ == "__main__":
    db = Databse()
    db.init()
    db.create_table("alarms", "id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), description VARCHAR(255)")
    db.insert("alarms", "time, description", "'2021-01-01 12:00:00', 'Wake up'")
    del db
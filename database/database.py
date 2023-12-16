import mysql.connector

DATABASE_NAME = "homeDB"


class Databse:
    def init(self, host: str = "localhost", user: str = "user", password: str = "password", db_name: str = "homeDB"):
        """
        Initialize the database connection
        """
        # Create the connection object
        self.__myconn = mysql.connector.connect(host=host, user=user, passwd=password)
        self.__cur = self.__myconn.cursor()
        self.db_name = db_name
        self.__create_database()
        self.__myconn.database = self.db_name

    def __create_database(self):
        try:
            self.__cur.execute("show databases")
            dbs = self.__cur.fetchall()
            if any(self.db_name in db for db in dbs):
                print("Database already exists")
            else:
                self.__cur.execute(f"create database {DATABASE_NAME}")
                print("Database created successfully")
        except Exception as e:
            print(e)

    def create_table(self, table_name: str, columns: str) -> bool:
        """
        Create a new table in the database.

        Args:
            table_name (str): The name of the table to be created
            columns (str): The columns of the table to be created

        Returns:
            bool: True if the table was created successfully, False otherwise
        """
        try:
            self.__cur.execute("show tables")
            tables = self.__cur.fetchall()
            if any(table_name in table for table in tables):
                print("Table already exists")

            else:
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

    def delete(self, table_name, condition):
        sql = f"DELETE FROM {table_name} WHERE {condition}"
        try:
            self.__cur.execute(sql)
            self.__myconn.commit()
            print("Records deleted successfully")
        except Exception as e:
            print(e)
            # self.__myconn.rollback()

    def print_table(self, table_name):
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
    db.print_table("alarms")
    db.insert("alarms", "time, description", "'2021-01-01 12:00:00', 'Wake up'")
    db.insert("alarms", "time, description", "'2021-01-01 12:00:00', 'Wake up'")
    db.print_table("alarms")
    db.delete("alarms", "id>1")
    db.print_table("alarms")
    del db

import mysql.connector
from dataclasses import dataclass, field
from typing import Dict, List
from table import Table
import constants as C


class Databse:
    def init(
        self,
        host: str = C.DATABASE_HOST,
        user: str = C.DATABASE_USER,
        password: str = C.DATABASE_PASSWORD,
        db_name: str = C.DATABASE_NAME,
    ):
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
                self.__cur.execute(f"create database {self.db_name}")
                print("Database created successfully")
        except Exception as e:
            print(e)

    def create_table(self, table: Table) -> bool:
        """
        Create a new table in the database.

        Args:
            table (Table): The table object to create

        Returns:
            bool: True if the table was created successfully, False otherwise
        """
        try:
            self.__cur.execute("show tables")
            tables = self.__cur.fetchall()
            if any(table.name in t for t in tables):
                print("Table already exists")

            else:
                self.__cur.execute(f"create table {table.name} ({table.columns})")
                print("Table created successfully")
        except Exception as e:
            print(e)

    def insert(self, table: Table):
        """
        Insert new records into the database

        Args:
            table (Table): The table with objects to insert
        """
        for values in table.get_values_to_insert():
            sql = f"INSERT INTO {table.name} ({table.get_column_names_to_insert()}) VALUES ({values})"
            print(sql)
            try:
                self.__cur.execute(sql)
                self.__myconn.commit()
                print("Record inserted successfully")
            except Exception as e:
                print(e)

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

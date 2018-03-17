#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymssql


class databaseConnect(object):
    """
      Class which create database connection and returns cursor
      to interact with database.

    """

    def __init__(self,
                 server_name='',
                 username='',
                 password='',
                 database_name=''):
        """ Init function will work like constructor to this class.

        First thing to execute in this class - Let's take advantage of this.

        """
        self.server = server_name
        self.database = database_name
        self.username = username
        self.password = password

    def connect(self):
        """Connect to mssql database.

        Get cursor and set connection flag to True
        """
        self.connection = pymssql.connect(
            self.server,
            self.username,
            self.password,
            self.database
        )
        self.cursor = self.connection.cursor()

    def close(self):
        """Close connection from mssql.

        Commit changes before closing connection and
        set connection flag to false
        """
        self.connection.commit()
        self.connection.close()

    def execute(self, statement):
        """Execute queries from connection cursor.


        """
        queries = []

        self.connect()
        try:
            self.cursor.execute(statement)
            data = self.cursor.fetchall()
            queries.append(data)

        except pymssql.Error as error:
            print('An error occurred:', error.args[0])
            print('For the statement:', statement)

        for result in queries:
            if result:
                for row in result:
                    print(row)
            else:
                print(result)

        self.close()
        return queries

    def delete(self, statement):
        """Execute queries from connection cursor.


        """
        self.connect()
        task = ""
        try:
            self.cursor.execute(statement)
            task = "success"
        except pymssql.Error as error:
            print('An error occurred:', error.args[0])
            print('For the statement:', statement)
            task = error.args[0]

        self.close()
        return task

    def update(self, statement):
        """Execute queries from connection cursor.


        """
        self.connect()
        task = ""
        try:
            self.cursor.execute(statement)
            task = "success"
        except pymssql.Error as error:
            print('An error occurred:', error.args[0])
            print('For the statement:', statement)
            task = error.args[0]

        self.close()
        return task

    def execute_no_return(self, statement):
        """Execute queries from connection cursor.


        """
        self.connect()
        task = ""
        try:
            self.cursor.execute(statement)
            task = "success"
        except pymssql.Error as error:
            print('An error occurred:', error.args[0])
            print('For the statement:', statement)
            task = error.args[0]
        self.close()
        return task

    def columnnames(self, tablename):
        """Get coumn names of table specified.

        This will help in creating json key names easily.
        """
        columns = list()

        self.connect()
        try:
            base_query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS \
            WHERE TABLE_NAME = '{0}'\
            ORDER BY ORDINAL_POSITION" .format(tablename)

            self.cursor.execute(base_query)
            columns_row = self.cursor.fetchall()

            for i in columns_row:
                if i:
                    columns.append(i[0])
        except pymssql.Error as error:
            print('database error', error.args[0])

        self.close()
        return columns

    def column_names_datatype(self, tablename):
        """
        """

        result = dict()

        self.connect()
        try:
            base_query = "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS \
            WHERE TABLE_NAME = '{0}' \
            ORDER BY ORDINAL_POSITION" .format(tablename)

            self.cursor.execute(base_query)
            columns_row = self.cursor.fetchall()

            for entry in columns_row:
                if entry:
                    result.update({entry[0].lower(): entry[1]})
        except pymssql.Error as error:
            print('database error', error.args[0])

        self.close()
        return result

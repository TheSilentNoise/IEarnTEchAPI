from flask import request
import json
import jsonschema
from jsonschema import validate
import datetime
import uuid
from commons.utils import return_result
import pymysql
import re

from config.config import (
   SERVER_NAME,
   DB_NAME,
   USERNAME,
   PASSWORD
   )

class Queries:
    """
    Init constructor to instantiate the class
    """

    def __init__(self):

        self.conn = pymysql.connect(SERVER_NAME, USERNAME, PASSWORD, DB_NAME)

    def listUsers(self):
        data = []
        self.cursor = self.conn.cursor()
        queryString = "select * from user"
        self.cursor.execute(queryString)
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        for row in rows:
            row = dict(zip(columns,row))
            data.append(row)
        self.conn.close()
        #print(data)

        num_fields = len(self.cursor.description)
        field_names = [i[0] for i in self.cursor.description]
        #print(field_names)
        #   print(num_fields)

        return data
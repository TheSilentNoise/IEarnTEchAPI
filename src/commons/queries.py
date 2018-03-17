from flask import request
import json
import jsonschema
from jsonschema import validate
import datetime
import uuid
from commons.utils import return_result
import pymysql
from werkzeug.security import generate_password_hash,check_password_hash
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

        #print(data[0]['user_password'])

        return data

    def changeUserPassword(self,userId):

        jsonData = request.json

        oldPassword = jsonData['oldPassword']
        self.cursor = self.conn.cursor()
        queryString = "select user_password from user where id ="+str(userId)
        print(queryString)
        self.cursor.execute(queryString)
        dbPassword = self.cursor.fetchone()
        strPassword=(''.join(dbPassword))

        hashedPassword = check_password_hash(strPassword,oldPassword)
        print(hashedPassword)
        if(hashedPassword):
            newPassword = jsonData['newPassword']
            hashedNewPassword = generate_password_hash(newPassword,method='sha256')
            queryString = "Update user SET user_password='"+hashedNewPassword+"' WHERE id="+str(userId)
            print(queryString)
            self.cursor.execute(queryString)
            self.conn.commit()
            data = "Password Updated Sucessfully"
        else:
            data = "Password do not match"

        self.conn.close()

        return data

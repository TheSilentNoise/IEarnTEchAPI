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
        queryString = "select * from user order by id DESC limit 10"
        '''queryString = "select u.id,u.user_fname,u.user_lname,enrl.course_name," \
                      "u.user_phoneno,u.user_email,enrl.date_created from " \
                      "(select uc.user_id,c.id,uc.date_created,course_name from " \
                      "courses c join user__course uc on c.id=uc.course_id)enrl " \
                      "join user u ON u.id=enrl.user_id order by u.id"
                      '''
        self.cursor.execute(queryString)
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        for row in rows:
            row = dict(zip(columns,row))
            data.append(row)
        self.conn.close()

        #print(data[0]['user_password'])
        #select u.id,u.user_fname,u.user_lname,enrl.course_name from (select uc.user_id,c.id,course_name from courses c join user__course uc on c.id=uc.course_id)enrl join user u ON u.id=enrl.user_id
        #print(data)

        return data

    def userEnroll(self):
        data = []
        self.cursor = self.conn.cursor()
        queryString = "select u.id,u.user_fname,u.user_lname,enrl.course_name," \
                      "u.user_phoneno,u.user_email,enrl.date_created from " \
                      "(select uc.user_id,c.id,uc.date_created,course_name from " \
                      "courses c join user__course uc on c.id=uc.course_id)enrl " \
                      "join user u ON u.id=enrl.user_id order by u.id"
        self.cursor.execute(queryString)
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        for row in rows:
            row = dict(zip(columns,row))
            data.append(row)
        self.conn.close()

        #print(data)

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

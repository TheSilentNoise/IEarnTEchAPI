from flask_restful import Resource
from commons.queries import Queries
from flask_restful_swagger import swagger
from flask import jsonify
import pymysql

class UserEnrollment(Resource):
    """
       This class calls methods to retrieve the cartridge type
       """

    @swagger.operation(
        notes='This method is used to retrieve the '
              'data from target table',
        nickname='GET'

    )
    def get(self):
        """
        Fetches data from target table
        :return: Success or failure message based on data fetched
        """
        try:
            queries = Queries()
        except pymysql.InternalError as e:
            return jsonify(
                {'Error': {
                    'Message': e.args[0]}})
        except pymysql.OperationalError  as e:
            return jsonify({'Error': {
                'Message': [e.args[0]]}})
        except Exception as e:
            return jsonify({'Error': {
                'Message': [e.args[0]]}})
        try:
            data = queries.userEnroll()
            return jsonify({'data': data})
        except pymysql.ProgrammingError  as e:
            return jsonify({'Error': {
                'Message': [e.args[0]]}})
        except pymysql.OperationalError  as e:
            return jsonify({'Error': {
                'Message': [e.args[0]]}})
        except pymysql.DataError as e:
            return jsonify({'Error': {
                'Message': [e.args[0]]}})
        except Exception as e:
            return jsonify({'Error': {
                'Message': [e.args[0]]}})
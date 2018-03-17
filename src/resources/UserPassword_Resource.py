from flask_restful import Resource
from commons.queries import Queries
from flask_restful_swagger import swagger
from flask import jsonify
import pymysql

class ChangePassword(Resource):
    """
    This class calls methods to change the password for a user
    """
    @swagger.operation(
        notes='This method is used to retrieve the '
              'data from target table',
        nickname='PUT',
        parameters=[
            {
                "name": "userId",
                "description": "The User Id is a unique "
                               "identifier of each User",
                "required": True,
                "allowMultiple": False,
                "dataType": "Int",
                "paramType": "path"
            },
            {
                "name": "body",
                "description": "{ oldPassword : '', newPassword : '' }",
                "required": True,
                "type": "application/json",
                "paramType": "body"
            }
        ]
    )

    def put(self,userId):
        """
                Updates password for a given user, if given the correct old password
                :return: Data updated, if successful
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
            data = queries.changeUserPassword(userId)
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
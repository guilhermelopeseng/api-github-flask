import requests
from flask import request, abort, jsonify
from flask_restful import Resource

class UserInfoResource(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        try:
            username = json_data['username']
            if username is None or username == '':
                return abort(404, '[ERROR] username not find')
            res = requests.get(f"https://api.github.com/users/{username}").json()

            dic = {
                'Username': res['login'],
                'Name': res['name'],
                'Bio': res['bio'],
            }

            return dic
        except:
            return abort(404, '[ERROR] Failed in processing username in Github')
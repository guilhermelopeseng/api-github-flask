import requests
from flask import render_template, request, abort


def index():
    return render_template('index.html')


def user():
    try:
        username = request.form["username"]
        if username is None or username == '':
            return abort(404, '[ERROR] username not find')
        res = requests.get(f"https://api.github.com/users/{username}")
        data = res.json()

        return render_template(
            'user.html',
            login=data['login'],
            name=data['name'],
            bio=data['bio'],
        )
    except:
        return abort(404, '[ERROR] username not find')

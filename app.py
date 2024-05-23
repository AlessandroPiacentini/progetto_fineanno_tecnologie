from flask import Flask, render_template, request, make_response
from DataBase_controller import Database
import hashlib
import json
from login_controller import LoginController

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")


@app.route("/home")
def home():
    if get_cookie("id") is None:
        return render_template("login.html")
    return render_template("home.html")

@app.route("/registrazione")
def registrazione():
    return render_template("registrazione.html")

@app.route('/checklogin', methods=['POST'])
def checklogin():
    data = request.get_json()  
    data['password'] = converti_in_md5(data['password'])
    lg = LoginController()
    result = lg.checklogin(data)
    if result != None:
        response = make_response(result)
        response = set_cookie("id", result, response)
    return response

@app.route('/checkregistrazione', methods=['POST'])
def checkregistrazione():
    data = request.get_json()  
    data['password'] = converti_in_md5(data['password'])
    lg = LoginController()
    result = lg.checkregistrazione(data)
    return result

def converti_in_md5(stringa):
    m = hashlib.md5()
    m.update(stringa.encode('utf-8'))
    return m.hexdigest()

def get_cookie(key):
    return request.cookies.get(key)

def set_cookie(key, value, response):
    response.set_cookie(key, value, max_age=5*60, secure=True, httponly=True, samesite='Lax')
    return response




if __name__ == '__main__':  
    app.run()

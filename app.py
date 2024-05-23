from flask import Flask, render_template, request
from DataBase_controller import Database
import hashlib
import json
from login_controller import LoginController

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/registrazione")
def registrazione():
    return render_template("registrazione.html")

@app.route('/checklogin', methods=['POST'])
def checklogin():
    data = request.get_json()  
    
    data['password'] = converti_in_md5(data['password'])
    
    
    lg=LoginController()
    result=lg.checklogin(data)
    return result
    
    
@app.route('/checkregistrazione', methods=['POST'])
def checkregistrazione():
    data = request.get_json()  
    
    data['password'] = converti_in_md5(data['password'])
    
    
    lg=LoginController()
    result=lg.checkregistrazione(data)
    return result
    
    
    
    

def converti_in_md5(stringa):
    m = hashlib.md5()
    m.update(stringa.encode('utf-8'))
    return m.hexdigest()

if __name__ == '__main__':  
    app.run()

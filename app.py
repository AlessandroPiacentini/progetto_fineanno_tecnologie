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



@app.route('/checklogin', methods=['POST'])
def checklogin():
    lg=LoginController()
    
    data = request.get_json()  
    
    print(data)
    
    data['password']=converti_in_md5(data['password'])
    
    
    db=Database.getInstance()
        
    result=db.read_table('users',where=data)
    if len(result)==0:
        return json.dump(False)
    else:
        return json.dump("home")
            
        
    
    # response=lg.checklogin(data)
    # print(response)
    # return response
    
    
    
    
def converti_in_md5(stringa):
        m = hashlib.md5()
        m.update(stringa.encode('utf-8'))
        return m.hexdigest()


if __name__ == '__main__':  
    app.run()

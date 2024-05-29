import hashlib
from flask import Flask, redirect, request, jsonify, session
from DataBase_controller import Database

class LoginController:
    db = None
    def __init__(self, app):
        self.db = Database.getInstance() 
        self.app = app
        self.register_routes()
        
    def register_routes(self):
        @self.app.route('/checklogin', methods=['POST'])
        def checklogin():
            data = request.get_json()
            data['password'] = self.converti_in_md5(data['password'])
            return self.check_login(data['username'], data['password'])

        @self.app.route('/checkregistrazione', methods=['POST'])
        def checkregistrazione():
            data = request.get_json()
            data['password'] = self.converti_in_md5(data['password'])
            return self.check_registrazione(data['username'], data['password'])
        
        @self.app.route('/logout')
        def logout():
            session.pop('id', None)
            return redirect('/login')
    
    def check_login(self, username, password):
        result = self.db.check_user( username, password)
        if len(result) == 0:
            return jsonify(False)
        else:
            session['id'] = result[0][0]
            return jsonify("home")
        
    def check_registrazione(self, username, password):
        result = self.db.check_user( username, password)
        if len(result) == 0:
            self.db.inserisci_user( username, password)
            return jsonify("login")
        else:
            return jsonify(False)
        
    def converti_in_md5(self, stringa):
        m = hashlib.md5()
        m.update(stringa.encode('utf-8'))
        return m.hexdigest()


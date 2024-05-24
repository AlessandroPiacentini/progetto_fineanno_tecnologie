import hashlib
from flask import Flask, request, jsonify, session
from DataBase_controller import Database

class LoginController:
    db = None
    def __init__(self, app):
        self.db = Database.getInstance()  # Initialize the database instance
        self.app = app
        self.register_routes()
        
    def register_routes(self):
        @self.app.route('/checklogin', methods=['POST'])
        def checklogin():
            data = request.get_json()
            data['password'] = self.converti_in_md5(data['password'])
            return self.check_login(data)

        @self.app.route('/checkregistrazione', methods=['POST'])
        def checkregistrazione():
            data = request.get_json()
            data['password'] = self.converti_in_md5(data['password'])
            return self.check_registrazione(data)
        
        @self.app.route('/logout')
        def logout():
            session.pop('id', None)
            return jsonify("login")
    
    def check_login(self, data):
        result = self.db.read_table('users', where=data)
        if len(result) == 0:
            return jsonify(False)
        else:
            session['id'] = result[0][0]
            return jsonify("home")
        
    def check_registrazione(self, data):
        result = self.db.read_table('users', where=data)
        if len(result) == 0:
            self.db.insert('users', data)
            return jsonify("login")
        else:
            return jsonify(False)
        
    def converti_in_md5(self, stringa):
        m = hashlib.md5()
        m.update(stringa.encode('utf-8'))
        return m.hexdigest()

# Inizia l'app Flask e registra il controller
app = Flask(__name__)
lg = LoginController(app)

if __name__ == '__main__':
    app.run(debug=True)

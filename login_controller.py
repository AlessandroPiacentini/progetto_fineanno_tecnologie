import json
from flask import make_response, Flask, request
from DataBase_controller import Database
from cookie_controller import CookieController

class LoginController:
    
    def __init__(self) -> None:
        self.db = Database.getInstance()  # Initialize the database instance
    
    def checklogin(self, data):
        result = self.db.read_table('users', where=data)
        
        if len(result) == 0:
            return json.dumps(False)
        else:
            return json.dumps("home")
        
    def checkregistrazione(self, data):
        result = self.db.read_table('users', where=data)
        
        if len(result) == 0:
            self.db.insert('users', data)
            return json.dumps("home")
        else:
            return json.dumps(False)

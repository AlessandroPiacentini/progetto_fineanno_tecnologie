from DataBase_controller import Database
import json


class LoginController:
    
    def __init__(self) -> None:
        pass
    
    def checklogin(self, data):
        db = Database.getInstance()
        result = db.read_table('users', where=data)
        
        if len(result) == 0:
            return json.dumps(False)
        else:
            return json.dumps("home")
        
    def checkregistrazione(self, data):
        db = Database.getInstance()
        result = db.read_table('users', where=data)
        
        if len(result) == 0:
            db.insert('users', data)
            return json.dumps("home")
        else:
            return json.dumps(False)
        



    
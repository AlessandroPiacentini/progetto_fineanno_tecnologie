from DataBase_controller import Database
import json


class LoginController:
    
    def __init__(self) -> None:
        pass
    
    def checklogin(self, data):
        db=Database.getInstance()
        
        result=db.read_table('users',where=data)
        if len(result)==0:
            return json.dump(False)
        else:
            return json.dump("home")
            
        
        




    
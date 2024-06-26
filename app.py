from flask import Flask
from login_controller import LoginController
from page_controller import PageController
from spese_controller import SpeseController
from DataBase_controller import Database

app = Flask(__name__)
app.secret_key = 'gestione_spese_tecnologie'


lg = LoginController(app) 
pc = PageController(app)
sc = SpeseController(app)


if __name__ == '__main__':
    app.run() 

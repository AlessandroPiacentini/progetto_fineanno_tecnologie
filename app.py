from flask import Flask, render_template, request, make_response
from DataBase_controller import Database
import hashlib
import json
from login_controller import LoginController
from page_controller import PageController

app = Flask(__name__)
app.secret_key = 'gestione_spese_tecnologie'

lg = LoginController(app) 
pc = PageController(app)

if __name__ == '__main__':
    app.run(debug=True)  # Consiglio di attivare il debug durante lo sviluppo

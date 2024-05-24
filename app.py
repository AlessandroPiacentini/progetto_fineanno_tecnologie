from flask import Flask
from login_controller import LoginController
from page_controller import PageController
from spese_controller import SpeseController

app = Flask(__name__)
app.secret_key = 'gestione_spese_tecnologie'

lg = LoginController(app) 
pc = PageController(app)
sc = SpeseController(app)

if __name__ == '__main__':
    app.run(debug=True)  # Consiglio di attivare il debug durante lo sviluppo

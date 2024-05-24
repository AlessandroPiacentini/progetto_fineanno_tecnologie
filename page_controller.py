from flask import Flask, request, make_response, render_template

class PageController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route("/login")
        def login():
            return render_template("login.html")

        @self.app.route("/")
        def hello_world():
            return render_template("index.html", title="Hello")

        @self.app.route("/home")
        def home():
            return render_template("home.html")

        @self.app.route("/registrazione")
        def registrazione():
            return render_template("registrazione.html")

# Inizializza l'app Flask e registra il controller
app = Flask(__name__)
pc = PageController(app)

if __name__ == '__main__':
    app.run(debug=True)

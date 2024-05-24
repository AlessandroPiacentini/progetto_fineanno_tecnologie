from flask import Flask, session, render_template

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
            if 'id' in session and session['id'] is not None:
                return render_template("home.html")
            else:
                return render_template("login.html")
        @self.app.route("/spese")
        def spese():
            if 'id' in session and session['id'] is not None:
                return render_template("spese.html")
            else:
                return render_template("login.html")
        @self.app.route("/addSpesa")
        def addSpesa():
            if 'id' in session and session['id'] is not None:
                return render_template("add_spese.html")
            else:
                return render_template("login.html")

        @self.app.route("/registrazione")
        def registrazione():
            return render_template("registrazione.html")


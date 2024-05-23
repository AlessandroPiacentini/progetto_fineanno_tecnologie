from flask import flask, request, make_response, render_template

class Page_controller:
    app = None
    def __call__(self, app):
        self.app = app
    
    @self.app.route("/login")
    def login(self):
        return render_template("login.html")
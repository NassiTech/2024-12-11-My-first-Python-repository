from flask import Flask

app = Flask(__name__)


# Begrüßungsroute
@app.route("/")
def home():
    return "Willkommen bei meiner Flask-App!"


# Info-Route
@app.route("/info")
def info():
    return "Dies ist eine einfache API mit Flask."


# Team-Route
@app.route("/team")
def team():
    return "Unser Team besteht aus IT-Experten und Entwicklern."


# Hilfe-Route
@app.route("/hilfe")
def hilfe():
    return "Hier findest du Unterstützung zu unserer API."


# Kontakt-Route
@app.route("/kontakt")
def kontakt():
    return "Schreibe uns eine E-Mail an kontakt@example.com."


# about-Route
@app.route("/about")
def about():
    return "Mein Name ist Max Muster, und ich interessiere mich für Webentwicklung."


# project-Route
@app.route("/project")
def project():
    return "Mein aktuelles Projekt ist eine Flask-API für Anfänger."


# news-Route
@app.route("/news")
def news():
    return "Heute lernen wir, wie man APIs mit Flask erstellt!"


# feedback-Route
@app.route("/feedback")
def feedback():
    return "Wir freuen uns über dein Feedback unter feedback@example.com."


# fsupport-Route
@app.route("/support")
def support():
    return "Besuche unsere Support-Seite unter support.example.com."


# greet-Route  using parameters


@app.route("/greet/<name>")
def greet(name):
    return f"Hallo {name}, willkommen auf meiner Flask-API!"


if __name__ == "__main__":
    app.run(port=5000)

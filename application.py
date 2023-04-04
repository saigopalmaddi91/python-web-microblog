from flask import Flask, render_template

app = Flask(__name__)


class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/fancy")
def hello_world_fancy():
    return """
    <html>
    <body>

    <h1> Hello World! </h1>
    <p> Greetings!!! </p>

    """


@app.route("/jinja")
def jinja_func():
    return render_template("jinja_intro.html", name="Saigopal Maddi", template_name='Jinja2')


@app.route("/datastructures/")
def data_structures():
    movies = ["Game of Thrones", "Breaking Bad", "You"]
    information = {'first_name': 'Saigopal', 'last_name': 'Maddi', 'age': 27, 'job': 'software'}
    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")
    kwargs = {
        "movies": movies,
        "information": information,
        "moons": moons
    }
    return render_template("data_structures.html", **kwargs)


@app.route("/conditionals/")
def render_conditionals():
    company = "OnePlus"
    return render_template("conditionals_basics.html", company=company)


@app.route("/for-loop/")
def render_for_loop():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    return render_template("for_loop.html", planets=planets)
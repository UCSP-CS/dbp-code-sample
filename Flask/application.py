from flask import Flask # Import the class `Flask` from the `flask` module, written by someone else.

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file


@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
    return "Hello, world!"

@app.route("/maria")
def maria():
    return "Hello, Maria"

@app.route("/jose")
def jose():
    return "Hello, Jose"

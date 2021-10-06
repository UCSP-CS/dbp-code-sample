import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():

    # Query for currency exchange rate
    currency = request.form.get("currency")
    res = requests.get(
        "http://data.fixer.io/api/latest",
        params={"access_key": "b42cc38fe4cd5b869888c5a9902aeb3c", "symbols": currency}
    )

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})

    # Make sure currency is in response
    data = res.json()
    if currency not in data.get("rates", []):
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})

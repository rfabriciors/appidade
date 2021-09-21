import flask
import os
from flask import Flask, render_template, jsonify

health = True
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/health')
def healthcheck():
    if health:
        return render_template("health.html")
    else:
        return 'bad request!', 400

@app.route('/sethealth')
def sethealth():
    global health
    health = False
    chopstick = {
        'health': health
    }
    return jsonify(chopstick)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")
#!/usr/bin/env python3

from flask import Flask, render_template

from get_props import making_data_json

Real_Tech = Flask(__name__)

@Real_Tech.route("/")
def hello_world():
    return """
    <p>Hello Real Tech!</p>
    <a href="/propiedades">propiedades</a>
    """

@Real_Tech.route("/propiedades")
def propiedades():
    prop = making_data_json()
    return render_template("propiedades.html", prop=prop)


if __name__ == "__main__":
    Real_Tech.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3

from flask import Flask, render_template

from get_props import making_json
Real_Tech = Flask(__name__)

@Real_Tech.route("/")
def hello_world():
    return "<p>Hello Real Tech!</p>"

@Real_Tech.route("/apartamentos")
def apartamentos():
    prop = making_json().filtered_props
    return "<p>Hello, World!</p>", render_template("apartamentos.html", prop=prop)


if __name__ == "__main__":
    Real_Tech.run(host='0.0.0.0', port=5000, debug=True)

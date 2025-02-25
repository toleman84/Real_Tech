#!/usr/bin/env python3

from flask import Flask, render_template, request
import json

from get_props import making_data_json, get_data_prop

Real_Tech = Flask(__name__)

# Opciones predefinidas para el menú desplegable
PROPIEDADES = [
    {"id": "MLA1472", "name": "Departamentos"},
    {"id": "MLA1473", "name": "Casas"},
    {"id": "MLA1474", "name": "Locales Comerciales"},
    {"id": "MLA1475", "name": "Terrenos"}
]

def cargar_propiedades():
    with open("url_backup.json", "r", encoding="utf-8") as file:
        return json.load(file)

@Real_Tech.route("/")
def hello_world():
    return """
    <p>Hello Real Tech!</p>
    <a href="/propiedades">propiedades</a>
    """

@Real_Tech.route("/propiedades", methods=["GET", "POST"])
def propiedades():
    category = request.form.get("category", "MLU1459")
    prop_id = request.form.get("prop_id", "MLA1472")
    prop_name = next((p["name"] for p in PROPIEDADES if p["id"] == prop_id), "Departamentos")

    # Llamar a la función existente con los parámetros proporcionados
    prop = get_data_prop(category=category, prop_id=prop_id, prop_name=prop_name)
    return render_template("props.html", prop=prop, category=category, prop_name=prop_name, PROPIEDADES=PROPIEDADES)


if __name__ == "__main__":
    Real_Tech.run(host='0.0.0.0', port=5000, debug=True)

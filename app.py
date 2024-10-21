import time
import random
from dataclasses import dataclass
from datetime import datetime
from flask import Flask, render_template
from flask.json import dumps

app = Flask(__name__) #main

list1 = ["Вчора", "пооосле завтра"]
list2 = ["на вас", "ви", "на вас"]
list3 = ["упаде андроеднийколайдер", "побачете як риба буде танцювать гопака на пальмі", "повинні поставити все імущество на красний"]

# @app.route("/home/")

@app.get("/list")
def choice():
    return f"{random.choice(list1)} {random.choice(list2)} {random.choice(list3)} "

@app.get("/")
def index():
    return f"{render_template("index.html")}"
# @app.route("/")



@app.get("/menu")
def menu():
    return f"{render_template("index.html")}"


# @app.get @app.post @app.delete @app.put


if __name__ == "__main__":
    app.run(port=8010, debug=True)

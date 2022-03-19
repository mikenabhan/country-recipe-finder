#!/usr/bin/env python3
import json
import random
from flask import Flask

app = Flask(__name__)

all_countries = []

@app.route('/')

def get_county():
    with open('./all_countries.json', "r") as country_file:
        all_countries = json.load(country_file)
        random_country = random.choice(all_countries)
    return random_country


#!/usr/bin/env python3
import json
# import sqlite3
import os
import random

all_countries = []

def get_county():
    with open('./all_countries.json', "r") as country_file:
        all_countries = json.load(country_file)
        random_country = random.choice(all_countries)
    return random_country['Name']
print(get_county())
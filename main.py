#!/usr/bin/env python3
import json
# import sqlite3
import os
import random

all_countries = []
remaining_countries = []

def first_run():
    with open('./all_countries.json', "r") as country_file:
        all_countries = json.load(country_file)

    for i in all_countries:
        country = i['Name']
        # print(country)
        remaining_countries.append(country)

    # print(remaining_countries)

    with open('remaining_countries.json', "w") as outfile:
        json.dump(remaining_countries, outfile)


if not os.path.exists('./remaining_countries.json'):
    first_run()

def get_country():
    with open('./remaining_countries.json', "r") as country_list_file:
        countries_to_choose = json.load(country_list_file)
    this_week = random.choice(countries_to_choose)
    countries_to_choose.remove(this_week)
    print(this_week)
    with open('remaining_countries.json', "w") as outfile:
        json.dump(countries_to_choose, outfile)
    # print(len(countries_to_choose))
get_country()
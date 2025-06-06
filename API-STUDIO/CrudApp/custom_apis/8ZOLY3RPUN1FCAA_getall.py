from urllib.parse import quote_plus

import requests
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import declarative_base, Session


def custom_api(db, models, data):
    countries = db.query(models.Country).all()

    countries_list = []

    for country in countries:
        countries_list.append({
            "state": country.state,
            "language": country.language
        })

    return countries_list
   


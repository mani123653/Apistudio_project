from urllib.parse import quote_plus

import requests
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import declarative_base, Session


def custom_api(db, models, data):

    language = data.get('language')
    state = data.get('state')

    countries = db.query(models.Country).filter(models.Country.language == language, models.Country.state == state).all()
    return countries


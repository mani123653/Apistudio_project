from urllib.parse import quote_plus

import requests
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import declarative_base, Session


def custom_api(db, models, data):

    psk_id = data.get('psk_id')

    obj = db.query(models.Country).filter(models.Country.psk_id == psk_id).first()

    db.delete(obj)

    db.commit()

    return "User deleted successfully"

"""SQLAlchemy models (schema) for twitoff"""
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import numpy as np
import json

DB = SQLAlchemy()

class Record(DB.Model):
    """Campaign  data"""
    # id, backers_count, category, pledged, state, blurb_length, goal_in_usd, campaign_duration, sub_category
    id = DB.Column(DB.BigInteger, primary_key=True)
    backers_count = DB.Column(DB.Integer)
    category = DB.Column(DB.UnicodeText())
    pledged = DB.Column(DB.Integer)
    state = DB.Column(DB.Integer)
    blurb_length = DB.Column(DB.Integer)
    goal_in_usd = DB.Column(DB.Integer)
    campaign_duration = DB.Column(DB.Integer)
    sub_category = DB.Column(DB.UnicodeText())
    
    def __repr__(self):
        return f"<User: {self.text}>"





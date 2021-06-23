"""
Main app/routing file for Twitoff.
The file that holds the function `create_app`
to collect our modules and organize the flask app.
"""
from os import getenv
from flask import Flask, render_template, request
from .models import DB, Record, list_tuple

def create_app():
    # initilizes our application
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    @app.route("/")
    def root():
        """This will be presented when we visit '<BASE_URL>/ '"""
        users = Record.query.all()  # SQL equivalent: `SELECT * FROM user;
        return render_template("base.html", title='Home', users=users)
    @app.route("/compare", methods=["POST"])
    @app.route("/user", methods=["POST"])
    @app.route("/user/<name>", methods=["GET"])
    def prediction(name=None, message=''):
        """This will be presented when we visit '<BASE_URL>/user '"""
    # return render_template("prediction.html", title="prediction", message=message)
    @app.route("/reset")
    def reset():
        """This will be presented when we visit '<BASE_URL>/reset '"""
        DB.drop_all()
        DB.create_all()
        for list_item in list_tuple:
        # id,  backers_count, category, goal, pledged, spotlight, state, blurb_length, goal_in_usd, campaign_duration, sub_category
            db_record = Record(id=list_item[0], backers_count=list_item[1], category = list_item[2],                 
                        pledged = list_item[3], state = list_item[4],
                        blurb_length = list_item[5], goal_in_usd = list_item[6], 
                        campaign_duration = list_item[7], sub_category = list_item[8]) 
            DB.session.add(db_record)
        DB.session.commit()
        users = Record.query.all()  # SQL equivalent: `SELECT * FROM user;`
        return render_template("base.html", title='Home', users=users)
    # @app.route("/say_something")
    # def say_something():
    #     """This will be presented when we visit '<BASE_URL>/say_something '"""
    #     return "I am saying something"
    return app

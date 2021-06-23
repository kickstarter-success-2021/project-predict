"""Retrieve and requests tweets from the DS API"""
""" Remember, use flask shell to test components"""
""" If Necessary, pipenv install python-dotenv"""
#Make sure you have installed sklearn and google-api-python-client
import requests
import spacy
from .models import DB, Tweet, User

# See the commands in the doc string below
""" Install with command python -m spacy download en_core_web_sm, then 
Load with command nlp = spacy.load("en_core_web_sm"), then
nlp.to_disk("my_model")"""
nlp = spacy.load("my_model")

def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector


# Add and updates tweets
def add_or_update_user(username):
    """
    Adds and updates the user with twitter handle 'username'
    to our database
    """
    try:
        r = requests.get(
            f"https://lambda-ds-twit-assist.herokuapp.com/user/{username}")
        user = r.json()
        user_id = user["twitter_handle"]["id"]
        # This either resepectively grabs or creates a user for our db
        db_user = User.query.get(user_id) or User(id=user_id, name=username)
        # This adds the db_user to our database
        DB.session.add(db_user)
        tweets = user["tweets"]
        for tweet in tweets:
            tweet_vector = vectorize_tweet(tweet["full_text"])
            db_tweet = Tweet.query.get(tweet["id"]) or Tweet(id=tweet["id"], text=tweet["full_text"], vect=tweet_vector)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        print("Error processing {}: {}".format(username, e))
    else:
        DB.session.commit()
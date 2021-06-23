"""Prediction of users based on tweet vectors"""
import numpy as np
# from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
import joblib

def predict_user(user0_name, user1_name, hypo_tweet_text):
    """
    Determines and returns which user is more likley to say a given tweet.
    Example Run: predict_user("elonmusk", "jackblack", "Tesla Cars are cool")
    Returns either a 0 (user0_name) or a 1 (user1_name)
    """
    
    # # Grabbing users form our DB - need to exist
    # user0 = User.query.filter(User.name == user0_name).one()
    # user1 = User.query.filter(User.name == user1_name).one()
    # # Grab vectors from the tweets attribute
    # user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    # user1_vects = np.array([tweet.vect for tweet in user1.tweets])
    # # Vertically stack tweet vectors on top of each other
    # vects = np.vstack([user0_vects, user1_vects])
    # # Creating a list of labels the same length as user0 tweets + user1 tweets
    # labels = np.concatenate(
    #     [np.zeros(len(user0.tweets)), np.ones(len(user1.tweets))])
    # # Creating instance and training model
    #         # log_reg = LogisticRegression().fit(vects, labels)
    grboost = joblib.load('assets/Pickle')
    model = grboost.fit(X_train, y_train)   
    # Creating vectors for hypothetical tweet parameter
    # hypo_tweet_vect = vectorize_tweet(hypo_tweet_text).reshape(1, -1)
    """.reshape(1, -1) If you have an array of shape (2,4) then reshaping it with (-1, 1), then the array will 
    get reshaped in such a way that the resulting array has only 1 column and this is only possible 
    by having 8 rows, hence, (8,1)."""
    return grboost.predict(X_val, y_val)
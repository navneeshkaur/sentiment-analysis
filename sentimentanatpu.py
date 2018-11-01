# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:38:42 2018

@author: NavneeshKaur
"""
import tweepy

from textblob import TextBlob
consumerkey='consumer_key'
consumersecret='consumer_secret '

accesstoken='access_token'
accesstokensecret='access_token_secret'
auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)
api=tweepy.API(auth)
public_tweets=api.search('Modi')
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

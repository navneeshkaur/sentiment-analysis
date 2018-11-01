# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:38:42 2018

@author: NavneeshKaur
"""
import tweepy

from textblob import TextBlob
consumerkey='buS3ogq0ju3gz2M4cQIFvwtfh'
consumersecret='jrA9NjY8lgeVj6Tai2LEfrKMWAuWPneVH5SOiY7BiQA2bVBxAX '

accesstoken='1057859228533121024-CYHH7EK3R6Bnzel4AHafjNl6ZSgXZb'
accesstokensecret='nNQLMYQpRBafYKfnntScsFXWQl3v5r8RpRCOPg2v9qmWr'
auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)
api=tweepy.API(auth)
public_tweets=api.search('Modi')
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

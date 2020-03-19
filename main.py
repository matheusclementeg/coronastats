# coding: utf-8

import requests
import tweepy
import time
from datetime import datetime, timezone, timedelta
from os import environ

# Keys for the authentication process
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


# Authentication process using the keys
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Creation of the actual interface using authentication
api = tweepy.API(auth)

# Infinite loop, tweets once every 24 hours
try:
    # Retrievel of API
    response = requests.get("https://coronavirus-19-api.herokuapp.com/countries")

    # Fetches JSON
    data = response.json()

    my_gen = (item for item in data if item['country'] == 'Brazil')
    for item in my_gen:
        print(item)

    # Current Time
    difference = timedelta(hours=-3)
    time_zone = timezone(difference)
    CurrentTime = datetime.today()
    CurrentTimeBR = CurrentTime.astimezone(time_zone)
    CurrentTimeFormat = '{} / {} / {}'.format(CurrentTimeBR.day,CurrentTimeBR.month,CurrentTimeBR.year)

    # Sub nodes from the 'latest' node are fetched along with the current date/time and used in the tweet
    tweet = "Dados do Coronavírus (COVID-19) no Brasil 🇧🇷 \n" +  "\n 🗓️ Data: " + CurrentTimeFormat + "" +  "\n 🤒 Casos Confirmados: " + str(
        item['cases']) + "" + "\n 😷 Casos Críticos: " + str(
        item['critical']) + "" + "\n 😢 Mortes: " + str(item['deaths']) + "" + "\n 🥳 Recuperados: " + str(
        item['recovered']) + "\n" + "\n #COVID19 #Coronavirus"
    print(tweet)
    api.update_status(tweet)
except tweepy.TweepError as error:
    print('\nError. Retweet not successful. Reason: ')
    print(error.reason)
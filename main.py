# coding: utf-8

import requests
import tweepy
import time
import time
from datetime import date
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
while True:
    try:
        # Retrievel of API
        response = requests.get("https://coronavirus-19-api.herokuapp.com/countries")

        # Fetches JSON
        data = response.json()
        # Fetches the 'latest' node from the API
        LatestData = data[29]

        # Current Time
        CurrentTime = date.today()
        CurrentTimeFormat = '{} / {} / {}'.format(CurrentTime.day, CurrentTime.month, CurrentTime.year)


        # Sub nodes from the 'latest' node are fetched along with the current date/time and used in the tweet
        tweet = "Dados do Coronavírus (COVID-19) - 🇧🇷 \n" +  "\n Data: " + CurrentTimeFormat + "" +  "\n Casos Confirmados: " + str(
            LatestData['cases']) + "" + "\n Casos Críticos: " + str(
            LatestData['critical']) + "" + "\n Mortes: " + str(LatestData['deaths']) + "" + "\n Recuperados: " + str(
            LatestData['recovered']) + "\n" + "\n #COVID19 #Coronavirus"
        print(tweet)
        api.update_status(tweet)
        time.sleep(86400)
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
# coding: utf-8

import requests
import tweepy
import time
import time
from datetime import date
from datetime import datetime


# Keys for the authentication process
ConsumerKey = 'pxQNZ8GHWKBs5ZU1aTtNs4sHj'
ConsumerSecret = 'ViFUkvoErZwrMw8NUGKGCl2YGdYmbOQQx0FWUHQ2YTL3rozLnc'
AccessToken = '1239600700369309697-aWDF7ms9nGxyKQ2MYx842KKO3z7qyN'
AccessTokenSecret = 'xNXszgpBqBcYa3kayMhmBtgWgqNPfmaL7p2KZLk6ZGvSN'

# Authentication process using the keys
auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

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
        LatestData = data[31]

        # Current Time
        CurrentTime = date.today()
        CurrentTimeFormat = '{} / {} / {}'.format(CurrentTime.day, CurrentTime.month, CurrentTime.year)


        # Sub nodes from the 'latest' node are fetched along with the current date/time and used in the tweet
        tweet = "Dados do Coronavírugit as (COVID-19) - 🇧🇷 \n" +  "\n Data: " + CurrentTimeFormat + "" +  "\n Casos Confirmados: " + str(
            LatestData['cases'])+  "\n Casos Confirmados (Hoje): " + str(
            LatestData['todayCases']) + "" + "\n Casos Críticos: " + str(
            LatestData['critical']) + "" + "\n Mortes: " + str(LatestData['deaths']) + "" + "\n Mortes (hoje): " + str(LatestData['todayDeaths']) + "" + "\n Recuperados: " + str(
            LatestData['recovered']) + "\n" + "\n #COVID19 #Coronavirus"
        print(tweet)
        api.update_status(tweet)
        time.sleep(86400)
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
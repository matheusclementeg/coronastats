# coding: utf-8

import requests
import tweepy
import time
import datetime
import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        #Keys for the authentication process
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
                CurrentTime = datetime.datetime.now().time()

                # Sub nodes from the 'latest' node are fetched along with the current date/time and used in the tweet
                tweet = "Dados do Coronavírus (COVID-19) 🇧🇷 \n" +  "\n Casos Confirmados: " + str(
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
    return jsonify({"message": "Não entre em pânico!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='https://coronaupdate.herokuapp.com/', port=port)

from flask import Flask, render_template, jsonify
import twitter
import tweepy

app = Flask(__name__)

@app.route('/')
def MainScreen():

    return render_template('index.html')

@app.route('/<int:id>/<int:size>/<int:needFollow>', methods = ['POST'])
def DoRetweets(id, size, needFollow):

    errors = []

    #Connect to Twitter API
    consumer_key = ''
    consumer_key_secret = ''

    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    #Get Raffle Winners
    
    winners = ['name1', 'name2', 'name3']

    return jsonify({'data': render_template('response.html', list = winners, errors = errors)})

if __name__ == "__main__":

    app.run(debug = True)
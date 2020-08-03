from flask import Flask, render_template, jsonify
import twitter
import tweepy

app = Flask(__name__)

@app.route('/')
def MainScreen():

    return render_template('index.html')

@app.route('/<int:id>', methods = ['POST'])
def DoRetweets(id):

    #Put Python Code Here

    winners = ['name1', 'name2', 'name3']
    return jsonify({'data': render_template('response.html', list = winners)})

if __name__ == "__main__":

    app.run(debug = True)
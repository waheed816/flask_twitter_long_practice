# !!START
from flask import Flask, render_template
from .config import Config
from .tweets import tweets
import random

app = Flask(__name__)
app.config.from_object(Config)
# !!END


@app.route('/')
def index():
    tweet_index = random.randint(0, len(tweets) - 1)
    """renders landing page"""
    return render_template("index.html", tweet=tweets[tweet_index])

@app.route('/feed')
def feed():
    return render_template("feed.html", tweets=tweets)

# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from datetime import date
from .form.form import PostForm
from random import randint

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

@app.route('/new', methods=["GET", "POST"])
def post():
    print("ENTER NEW ROW")
    form = PostForm()
    if form.validate_on_submit():
        print("IM HERE")
        new_post = {
            "id": len(tweets) + 1,
            "author": form.data["author"],
            "tweet": form.data["tweet"],
            "date": date.today(),
            "likes": randint(1000,1000000)}
        tweets.append(new_post)
        return redirect('/feed')
    if form.errors:
        return render_template("post_form.html", form=form, errors=form.errors)

    return render_template("new_tweet.html", form=form, errors=None)

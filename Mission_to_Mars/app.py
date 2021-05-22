from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info_DB")

@app.route("/")
def home():

    mars_info = mongo.db.mars_info.find_one()

    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():

    new_mars_info = scrape_mars.scrape()

    mongo.db.mars.update({}, new_mars_info, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
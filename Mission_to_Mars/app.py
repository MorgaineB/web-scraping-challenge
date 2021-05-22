from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info_DB")
db = mongo.db

@app.route("/")
def home():

    mars_info = db.mars_info.find_one()
    app.logger.info(mars_info)
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def mars():
    mars_info = scrape_mars.scrape()
    app.logger.info(mars_info)
    db.mars_info.update({}, mars_info, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
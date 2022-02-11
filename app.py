# use Flask to render a template, redirecting to another url, and creating a URL.
from flask import Flask, render_template, redirect, url_for
# use PyMongo to interact with our Mongo database.
from flask_pymongo import PyMongo
# use the scraping code, we will convert from Jupyter notebook to Python.
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
  # update the database 
   mars.update({}, mars_data, upsert=True)
  # redirect after successfully scraping the data
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()
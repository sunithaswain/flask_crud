from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__,static_url_path="/static",
static_folder="static",
template_folder="templates")
#from app import routes
app.run(debug=True)
mongo =PyMongo()
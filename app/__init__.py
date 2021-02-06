import os
from flask import Flask
from dotenv import load_dotenv

from app.classes.db import DB

app = Flask(__name__)

load_dotenv()

db = DB(os.environ["MONGO_CONNECTION_STRING"])

app.config['SECRET_KEY'] = "1d0522a7bd75b8e7"

from app import routes
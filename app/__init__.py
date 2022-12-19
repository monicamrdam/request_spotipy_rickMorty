from flask import Flask
from config import Config
from app.favourites.favourites_controller import favourite_page
from app.artist.artist_controller import artist_page

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(favourite_page)
app.register_blueprint(artist_page)

from app import routes


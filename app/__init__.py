from flask import Flask
from config import Config
from app.artist.artist_controller import artist_page
from app.character.character_controller import character_page
from app.favourites.favourites_controller import favourite_page
from app.all_character.all_character_controller import all_character_page

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(artist_page)
app.register_blueprint(character_page)
app.register_blueprint(favourite_page)
app.register_blueprint(all_character_page)

from app import routes

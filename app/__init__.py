from flask import Flask
from app.RickAndMortySpotify.artist.artist_controller import artist_page
from app.RickAndMortyPopulator.character.character_controller import character_page
from app.RickAndMortySpotify.favourites.favourites_controller import favourite_page
from app.RickAndMortyPopulator.all_character.all_character_controller import all_character_page

app = Flask(__name__)

app.register_blueprint(artist_page)
app.register_blueprint(character_page)
app.register_blueprint(favourite_page)
app.register_blueprint(all_character_page)

from app import routes

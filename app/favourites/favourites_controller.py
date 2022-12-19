from flask import Blueprint
from app.favourites.favourites_service import FavoriteSong

favourite_page = Blueprint('favourite_page', __name__)


@favourite_page.route('/favourites')
def favourites():
    return FavoriteSong.get_favorite_song()


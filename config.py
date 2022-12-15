import os
from dotenv import load_dotenv

#Carga las variables de entorno en memoria
load_dotenv() #Cargar todo el contenido de .env en variables de entorno

class Config:
    SERVER_NAME ='127.0.0.1:5000'
    DEBUG= True

    URL_Search = 'https://api.spotify.com/v1/search'
    URL_Artist= 'https://api.spotify.com/v1/artists'

    CLIENT_ID = os.environ.get('CLIENT_ID', "") # O devuelve la variable de entorno o la cadena vacia
    CLIENTE_SECRET = os.environ.get('CLIENTE_SECRET', "")  # O devuelve la variable de entorno o la cadena vacia
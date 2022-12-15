from app import app
from flask import jsonify

#Creamos una ruta de prueba home para tester que el servitor funciona
@app.route('/')
def home():
    message={
        "Home":'http://127.0.0.1:5000/',
    }
    return jsonify(message)
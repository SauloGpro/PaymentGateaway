from flask import Flask, render_template, request, jsonify
from models import db, Transaction
import os

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Aquí iría la lógica para manejar la carga de archivos y actualizar la base de datos
    return jsonify({'status': 'success'})

@app.route('/convert', methods=['POST'])
def convert_currency():
    # Lógica para interactuar con la API de UNIRAMP
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)

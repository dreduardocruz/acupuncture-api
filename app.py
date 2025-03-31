import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from routes.points_routes import points_routes
from controllers.points_controller import PointsController
from controllers.western_diseases_controller import WesternDiseasesController
from fuzzywuzzy import fuzz

# Configuração dos caminhos dos arquivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
DATA_DIR = os.path.join(BASE_DIR, 'data')
POINTS_CSV = os.path.join(DATA_DIR, 'acupuncture_points.csv')
MERIDIANS_CSV = os.path.join(DATA_DIR, 'meridians.csv')
SYNDROMES_CSV = os.path.join(DATA_DIR, 'syndromes.csv')
WESTERN_DISEASES_CSV = os.path.join(DATA_DIR, 'western_diseases_acupuncture.csv')

app = Flask(__name__)

# Configuração dos caminhos como variáveis de configuração do Flask
app.config['POINTS_CSV'] = POINTS_CSV
app.config['MERIDIANS_CSV'] = MERIDIANS_CSV
app.config['SYNDROMES_CSV'] = SYNDROMES_CSV
app.config['WESTERN_DISEASES_CSV'] = WESTERN_DISEASES_CSV

# Registra o blueprint com as configurações
points_routes.config = app.config
app.register_blueprint(points_routes)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
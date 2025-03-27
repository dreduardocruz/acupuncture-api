import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, Blueprint
from routes.points_routes import points_routes
from controllers.points_controller import PointsController
from fuzzywuzzy import fuzz  # Adicione este import

# Configuração dos caminhos dos arquivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')  # Caminho para a pasta css
DATA_DIR = os.path.join(BASE_DIR, 'data')
POINTS_CSV = os.path.join(DATA_DIR, 'acupuncture_points.csv')
MERIDIANS_CSV = os.path.join(DATA_DIR, 'meridians.csv')
SYNDROMES_CSV = os.path.join(DATA_DIR, 'syndromes.csv')  # Novo arquivo

app = Flask(__name__)  # O Flask já vai usar a pasta 'static' por padrão

# Configuração dos caminhos como variáveis de configuração do Flask
app.config['POINTS_CSV'] = POINTS_CSV
app.config['MERIDIANS_CSV'] = MERIDIANS_CSV
app.config['SYNDROMES_CSV'] = SYNDROMES_CSV  # Nova configuração

points_routes = Blueprint('points_routes', __name__)

@points_routes.route('/points', methods=['GET'])
def get_points_html():
    return PointsController.get_points_html(app.config['POINTS_CSV'])

@points_routes.route('/meridians', methods=['GET'])
def get_meridians_html():
    return PointsController.get_meridians_html(app.config['MERIDIANS_CSV'])

@points_routes.route('/search', methods=['GET'])
def search_points_html():
    query = request.args.get('query', '')
    return PointsController.search_points_html(query, app.config['POINTS_CSV'])

@points_routes.route('/syndromes', methods=['GET'])
def get_syndromes_html():
    return PointsController.get_syndromes_html(app.config['SYNDROMES_CSV'])

@points_routes.route('/syndromes/search', methods=['GET'])
def search_syndromes_html():
    query = request.args.get('query', '')
    return PointsController.search_syndromes_html(query, app.config['SYNDROMES_CSV'])

# Configuração de rotas
app.register_blueprint(points_routes)

@app.route('/')
def home():
    return render_template('home.html')

# Para debug
print(f"Pasta static configurada em: {STATIC_DIR}")
if os.path.exists(STATIC_DIR):
    print(f"Arquivos na pasta static: {os.listdir(STATIC_DIR)}")
else:
    print("Pasta static não encontrada!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
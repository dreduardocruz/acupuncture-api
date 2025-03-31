import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, request
from controllers.points_controller import PointsController
from controllers.western_diseases_controller import WesternDiseasesController

points_routes = Blueprint('points_routes', __name__)

@points_routes.route('/api/points', methods=['GET'])
def get_points():
    return PointsController.get_points()

@points_routes.route('/points', methods=['GET'])
def get_points_html():
    return PointsController.get_points_html(points_routes.config['POINTS_CSV'])

@points_routes.route('/api/points/search', methods=['GET'])
def search_points():
    query = request.args.get('query', '')
    return PointsController.search_points(query)

@points_routes.route('/search', methods=['GET'])
def search_points_html():
    query = request.args.get('query', '')
    return PointsController.search_points_html(query, points_routes.config['POINTS_CSV'])

@points_routes.route('/api/points/<int:point_id>', methods=['DELETE'])
def delete_point(point_id):
    return PointsController.delete_point(point_id)

@points_routes.route('/meridians', methods=['GET'])
def get_meridians_html():
    return PointsController.get_meridians_html(points_routes.config['MERIDIANS_CSV'])

@points_routes.route('/syndromes', methods=['GET'])
def get_syndromes_html():
    return PointsController.get_syndromes_html(points_routes.config['SYNDROMES_CSV'])

@points_routes.route('/syndromes/search', methods=['GET'])
def search_syndromes_html():
    query = request.args.get('query', '')
    return PointsController.search_syndromes_html(query, points_routes.config['SYNDROMES_CSV'])

@points_routes.route('/western-diseases', methods=['GET'])
def get_western_diseases_html():
    return WesternDiseasesController.get_western_diseases_html(points_routes.config['WESTERN_DISEASES_CSV'])

@points_routes.route('/western-diseases/search', methods=['GET'])
def search_western_diseases_html():
    query = request.args.get('query', '')
    return WesternDiseasesController.search_western_diseases_html(query, points_routes.config['WESTERN_DISEASES_CSV'])
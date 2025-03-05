import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, request
from controllers.points_controller import PointsController

points_routes = Blueprint('points_routes', __name__)

@points_routes.route('/api/points', methods=['GET'])
def get_points():
    return PointsController.get_points()

@points_routes.route('/points', methods=['GET'])
def get_points_html():
    return PointsController.get_points_html()

@points_routes.route('/api/points/search', methods=['GET'])
def search_points():
    query = request.args.get('query', '')
    return PointsController.search_points(query)

@points_routes.route('/search', methods=['GET'])
def search_points_html():
    query = request.args.get('query', '')
    return PointsController.search_points_html(query)

@points_routes.route('/api/points/<int:point_id>', methods=['DELETE'])
def delete_point(point_id):
    return PointsController.delete_point(point_id)
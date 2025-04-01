from flask import jsonify, render_template, render_template_string
from models.point import AcupuncturePoint
from fuzzywuzzy import fuzz, process
import csv
import os

class PointsController:
    @staticmethod
    def get_points(file_path):
        # Retorne uma lista de dicionários com os pontos de acupuntura
        try:
            points = PointsController.load_acupuncture_points(file_path)
            return jsonify([point.to_dict() for point in points])
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_points_html(file_path):
        try:
            print(f"Tentando carregar arquivo: {file_path}")
            points = PointsController.load_acupuncture_points(file_path)
            print(f"Pontos carregados: {len(points)}")
            return render_template('points.html', 
                                 points=[point.to_dict() for point in points],
                                 search_query='')
        except Exception as e:
            print(f"Erro ao carregar pontos: {str(e)}")
            return f"<h1>Erro ao carregar pontos</h1><p>{str(e)}</p>", 500

    @staticmethod
    def search_points(query):
        points = PointsController.load_acupuncture_points('data/acupuncture_points.csv')
        results = []
        query = query.lower()
        
        for point in points:
            point_dict = point.to_dict()
            if any(query in str(value).lower() for value in point_dict.values()):
                results.append(point_dict)
        
        return jsonify(results)

    @staticmethod
    def search_points_html(query, file_path):
        try:
            points = PointsController.load_acupuncture_points(file_path)
            results = []
            for point in points:
                point_dict = point.to_dict()
                if any(query.lower() in str(value).lower() for value in point_dict.values()):
                    results.append(point_dict)
            return render_template('points.html', 
                                 points=results,
                                 search_query=query)
        except Exception as e:
            return f"<h1>Erro</h1><p>{str(e)}</p>", 500

    @staticmethod
    def delete_point(point_id):
        # Implemente a lógica para deletar um ponto de acupuntura
        pass

    @staticmethod
    def load_acupuncture_points(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo CSV não encontrado: {file_path}")
            
        points = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    point = AcupuncturePoint(
                        name=row.get('Nome OMS', ''),
                        chinese_name=row.get('Nome Chinês', ''),
                        location=row.get('Localização', ''),
                        energy_level=row.get('Nível Energético', ''),
                        meridian=row.get('Meridiano Regular', ''),
                        opens_channels=row.get('Canal Maravilhoso', ''),
                        closes_channels=row.get('Função CM', ''),
                        function=row.get('Função CM', ''),
                        particularity=row.get('Particularidade', '')
                    )
                    points.append(point)
        except Exception as e:
            raise Exception(f"Erro ao ler arquivo CSV: {str(e)}")
            
        return points

    @staticmethod
    def get_meridians(file_path):
        meridians = PointsController.load_meridians(file_path)
        return jsonify([meridian for meridian in meridians])

    @staticmethod
    def get_meridians_html(file_path):
        meridians = PointsController.load_meridians(file_path)
        return render_template('meridians.html', meridians=meridians)

    @staticmethod
    def search_meridians(query, file_path):
        meridians = PointsController.load_meridians(file_path)
        results = []
        for meridian in meridians:
            if any(query.lower() in str(value).lower() for value in meridian.values()):
                results.append(meridian)
        return jsonify(results)

    @staticmethod
    def load_meridians(file_path):
        meridians = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                meridians = [row for row in csv_reader]
            return meridians
        except Exception as e:
            raise Exception(f"Erro ao ler arquivo de meridianos: {str(e)}")

    @staticmethod
    def get_syndromes_html(file_path):
        try:
            syndromes = PointsController.load_syndromes(file_path)
            return render_template('syndromes.html', syndromes=syndromes)
        except Exception as e:
            return f"<h1>Erro ao carregar síndromes</h1><p>{str(e)}</p>", 500

    @staticmethod
    def search_syndromes_html(query, file_path):
        try:
            syndromes = PointsController.load_syndromes(file_path)
            results = []
            
            # Se a query estiver vazia, mostra todas as síndromes
            if not query:
                return render_template('syndromes.html', 
                                     syndromes=syndromes,
                                     search_query='')
            
            # Se houver query, faz a busca fuzzy
            for syndrome in syndromes:
                max_ratio = max(
                    fuzz.partial_ratio(query.lower(), str(value).lower())
                    for value in syndrome.values()
                )
                
                if max_ratio > 60:
                    results.append(syndrome)
            
            return render_template('syndromes.html', 
                                 syndromes=results, 
                                 search_query=query)
        except Exception as e:
            return f"<h1>Erro na pesquisa</h1><p>{str(e)}</p>", 500

    @staticmethod
    def load_syndromes(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo CSV não encontrado: {file_path}")
            
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                syndromes = list(csv_reader)
                if not syndromes:
                    return []  # Retorna lista vazia se não houver dados
                return syndromes
        except Exception as e:
            raise Exception(f"Erro ao ler arquivo CSV: {str(e)}")
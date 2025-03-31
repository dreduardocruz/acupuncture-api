import pandas as pd
from flask import render_template
from fuzzywuzzy import fuzz

class WesternDiseasesController:
    @staticmethod
    def get_western_diseases_html(csv_path):
        try:
            df = pd.read_csv(csv_path)
            return render_template('western_diseases.html', diseases=df.to_dict('records'))
        except Exception as e:
            return f"Erro ao carregar dados: {str(e)}"

    @staticmethod
    def search_western_diseases_html(query, csv_path):
        try:
            df = pd.read_csv(csv_path)
            
            # Busca por correspondência parcial no nome da doença
            matches = df[df['Doença'].str.contains(query, case=False, na=False)]
            
            # Se não encontrar correspondência exata, usa fuzzy matching
            if len(matches) == 0:
                matches = df[df['Doença'].apply(lambda x: fuzz.partial_ratio(query.lower(), str(x).lower()) > 80)]
            
            return render_template('western_diseases.html', 
                                diseases=matches.to_dict('records'),
                                search_query=query)
        except Exception as e:
            return f"Erro na busca: {str(e)}" 
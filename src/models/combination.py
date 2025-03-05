class Combination:
    def __init__(self, name, points, description):
        self.name = name  # Nome da combinação
        self.points = points  # Lista de pontos de acupuntura
        self.description = description  # Descrição da combinação e suas indicações

    def add_point(self, point):
        """Adiciona um ponto à combinação."""
        self.points.append(point)

    def remove_point(self, point):
        """Remove um ponto da combinação."""
        if point in self.points:
            self.points.remove(point)

    def get_points(self):
        """Retorna a lista de pontos da combinação."""
        return self.points

    def __str__(self):
        """Retorna uma representação em string da combinação."""
        return f"Combinação: {self.name}, Pontos: {', '.join(self.points)}, Descrição: {self.description}"
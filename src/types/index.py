from typing import List, Dict, Any

class Point:
    def __init__(self, chinese_name: str, anatomical_location: str, description: str):
        self.chinese_name = chinese_name
        self.anatomical_location = anatomical_location
        self.description = description

class Meridian:
    def __init__(self, name: str, energy_levels: List[str], description: str):
        self.name = name
        self.energy_levels = energy_levels
        self.description = description

class Combination:
    def __init__(self, points: List[Point], description: str):
        self.points = points
        self.description = description

class RequestType:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

class ResponseType:
    def __init__(self, status: str, message: str, data: Any = None):
        self.status = status
        self.message = message
        self.data = data
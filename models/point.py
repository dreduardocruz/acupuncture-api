class AcupuncturePoint:
    def __init__(self, name, chinese_name, location, energy_level, meridian, opens_channels, closes_channels, function, particularity):
        self.name = name
        self.chinese_name = chinese_name
        self.location = location
        self.energy_level = energy_level
        self.meridian = meridian
        self.opens_channels = opens_channels
        self.closes_channels = closes_channels
        self.function = function
        self.particularity = particularity

    def to_dict(self):
        return {
            "name": self.name,
            "chinese_name": self.chinese_name,
            "location": self.location,
            "energy_level": self.energy_level,
            "meridian": self.meridian,
            "opens_channels": self.opens_channels,
            "closes_channels": self.closes_channels,
            "function": self.function,
            "particularity": self.particularity
        }
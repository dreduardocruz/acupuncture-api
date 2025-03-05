import csv

class Meridian:
    def __init__(self, name, anatomical_location, description, energy_level):
        self.name = name  # Nome do meridiano
        self.anatomical_location = anatomical_location  # Localização anatômica
        self.description = description  # Descrição do meridiano
        self.energy_level = energy_level  # Níveis energéticos do meridiano

    def save_to_csv(self):
        with open('data/meridians.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.anatomical_location, self.description, self.energy_level])

    @staticmethod
    def get_all_from_csv():
        meridians = []
        with open('data/meridians.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                meridians.append(row)
        return meridians

    @staticmethod
    def delete_from_csv(name):
        meridians = Meridian.get_all_from_csv()
        meridians = [m for m in meridians if m['name'] != name]
        with open('data/meridians.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'anatomical_location', 'description', 'energy_level'])
            writer.writeheader()
            writer.writerows(meridians)

    def get_info(self):
        return {
            "name": self.name,
            "anatomical_location": self.anatomical_location,
            "description": self.description,
            "energy_level": self.energy_level
        }
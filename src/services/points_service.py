class PointsService:
    def __init__(self, point_repository, meridian_repository, combination_repository):
        self.point_repository = point_repository
        self.meridian_repository = meridian_repository
        self.combination_repository = combination_repository

    def get_all_points(self):
        return self.point_repository.get_all()

    def get_point_by_id(self, point_id):
        return self.point_repository.get_by_id(point_id)

    def get_all_meridians(self):
        return self.meridian_repository.get_all()

    def get_meridian_by_id(self, meridian_id):
        return self.meridian_repository.get_by_id(meridian_id)

    def get_all_combinations(self):
        return self.combination_repository.get_all()

    def get_combination_by_id(self, combination_id):
        return self.combination_repository.get_by_id(combination_id)

    def find_combinations_for_syndrome(self, syndrome):
        return self.combination_repository.find_by_syndrome(syndrome)
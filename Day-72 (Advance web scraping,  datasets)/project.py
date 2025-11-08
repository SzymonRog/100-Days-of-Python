
class Project:
    def __init__(self, project_id, project_name, project_type, total_value, cofinancing_value, regions=[], beneficiary_name=''):
        self.project_id = project_id
        self.project_name = project_name
        self.project_type = project_type
        self.total_value = total_value
        self.cofinancing_value = cofinancing_value
        self.country = 'Poland'
        self.regions = regions
        self.beneficiary_name = beneficiary_name
        self.currency = 'PLN'
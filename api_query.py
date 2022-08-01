class Results:

    def __init__(self, response_json=None):
        self.response_json = response_json['data']['axies']['results']


    def get_results(self) -> list:
        return self.response_json


class AxieQuery(Results):

    def __init__(self, response_json=None):
        super().__init__(response_json)
        self.response_json = response_json
    

    def get_data(self) -> dict:
        return self.response_json['data']
    

    def get_axies(self) -> dict:
        return self.response_json['data']['axies']
    
    
    def get_total(self) -> int:
        return self.response_json['data']['axies']['total']


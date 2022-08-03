
# Recusive
def hashmap_key_searcher(dictionary, target):

    """ Takes a dictionary/hashmap and searches a key. """

    try:

        # checks each item on the dictionary
        for key, value in dictionary.items():


            if key == target:

                return value


            if type(value).__name__ == dict.__name__:

                return hashmap_key_searcher(value, target)
    
        return

    except:

        return None


class Query:

    """
        Disects the response from the GraphQL for an object.
    """

    def __init__(self, response_json=None):
        self.response_json = response_json
        if(type(response_json).__name__ != dict.__name__):
            self.response_json = None

    def get_data(self) -> dict:
        return hashmap_key_searcher(self.response_json, "data")

    def get_axies(self) -> dict:
        return hashmap_key_searcher(self.response_json, "axies")
    
    
    def get_total(self) -> int:
        return hashmap_key_searcher(self.response_json, "total")
    

    def get_results(self) -> list:
        return hashmap_key_searcher(self.response_json, "results")

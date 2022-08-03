
# recursive function.
# searches the hashmap, to know if the given key is available.
def hashmap_key_searcher(dictionary, target):
    try:
        """ Takes a dictionary/hashmap and searches a key. """

        # checks each item on the dictionary
        for key, value in dictionary.items():

            # checks if the key is equals to the target.
            if key == target:

                # returns value
                return value

            # checks if the value is another dictionary.
            if type(value).__name__ == dict.__name__:

                # runs the function again.
                return hashmap_key_searcher(value, target)
        
        # ends
        return
    except:

        return None


class AxieQuery:

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

class Axie:

    """
    
        Takes the dictionary and turns it into an object.

    """

    def __init__(self, dictionary=None):
        self.dictionary = dictionary
        self.id = self.dictionary['id']
        self.name = self.dictionary['name']
        self.stage = self.dictionary['stage']
        self.axie_class = self.dictionary['class']
        self.breed_count = self.dictionary['breedCount']
        self.image = self.dictionary['image']
        self.title = self.dictionary['title']
        self.auction = self.dictionary['auction']
        self.usd = self.dictionary['auction']['currentPriceUSD']
        self.battleinfo = self.dictionary['battleInfo']
        self.parts = self.dictionary["parts"]
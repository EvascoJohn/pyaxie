from api_model import BasicInfo
from api_model import Auction
from api_model import Parts
from api_model import GetAxieLatest



class Axie(BasicInfo, Auction, Parts):

    def __init__(self, response):

        super().__init__(response)
    

    async def if_price_usd(self, price):

        if float(self.get_price_usd()) <= price:
            return self

        return False
    

    async def if_eyes(self, eye):
        
        if(eye == self.get_parts()[0]):
            return self

        return False
    
    async def if_parts(self, parts):

        for part in self.get_parts():
            if(parts == part):
                return self

        return False



def get_lastest_axie(dictionary):

    return GetAxieLatest(dictionary)


def axie(response):

    return Axie(response)

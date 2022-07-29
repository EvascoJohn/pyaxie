import json


class ApiJSON(object):

	def __init__(self):
		self._json_body = {
				"operationName": None,
				"variables": None,
				"query": None
				}



class GetBaseClass(ApiJSON):

	_query = None

	_operation_name = None

	def __init__(self, dictionary: dict):

		super().__init__()

		self.json_body = self._json_body
		
		self.json_body["operationName"] = self._operation_name
		
		self.json_body["variables"] = dictionary
		
		self.json_body["query"] = self._query


	def get_json(self) -> str:

		return self.json_body



class BaseQuery(object):

	def __init__(self, response: dict):

		self.response = response
		self._index = 0

	def _common_query(self, response: dict):

		return response["data"]["axies"]["results"]
	

	def set_index(self, index=0):
		print("INDEX", index)
		self._index = index

	
	def get_response(self):
		return self._common_query(self.response)



class GetAxieBriefList(GetBaseClass):


	_query = """

				query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String)

				{\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) 

				{\n    total\n    results {\n      ...AxieBrief\n      __typename\n    }\n    __typename\n  }\n}\n\n

				fragment AxieBrief on Axie {\n  id\n  name\n  stage\n  class\n  breedCount\n  image\n  title\n  

				battleInfo {\n    banned\n    __typename\n  }\n  

				auction {\n    currentPrice\n    currentPriceUSD\n    __typename\n  }\n  

				parts {\n    id\n    name\n    class\n    type\n    specialGenes\n    __typename\n  }\n  __typename\n}\n

					"""


	_operation_name = "GetAxieBriefList"

	def __init__(self, dictionary:dict):

		super().__init__(dictionary)



class GetAxieLatest(GetBaseClass):


	_query = """

				query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String)

				{\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) 

				{\n    total\n    results {\n      ...AxieBrief\n      __typename\n    }\n    __typename\n  }\n}\n\n

				fragment AxieBrief on Axie {\n  id\n  name\n  stage\n  class\n  breedCount\n  image\n  title\n  

				battleInfo {\n    banned\n    __typename\n  }\n  

				auction {\n    currentPrice\n    currentPriceUSD\n    __typename\n  }\n  

				parts {\n    id\n    name\n    class\n    type\n    specialGenes\n    __typename\n  }\n  __typename\n}\n

					"""


	_operation_name = "GetAxieLatest"

	def __init__(self, dictionary:dict):
		super().__init__(dictionary)
		self.size = dictionary["size"]


class BasicInfo(BaseQuery):

	def __init__(self, response: dict):

		super().__init__(response)

		self.basic_info = super()._common_query(response)


	def get_name(self) -> str:
		return self.basic_info["name"]


	def get_id(self) -> str:
		return self.basic_info["id"]


	def get_stage(self) -> str:
		return self.basic_info["stage"]


	def get_class(self) -> str:
		return self.basic_info["class"]



class Auction(BaseQuery):


	def __init__(self, response: dict):

		super().__init__(response)

		self.auction = super()._common_query(response)["auction"]


	def get_price_usd(self) -> str:

		return str(self.auction["currentPriceUSD"])


	def get_price(self) -> str:

		return str(self.auction["currentPrice"])



class Parts(BaseQuery):


	def __init__(self, response: dict):

		super().__init__(response)

		self.parts = self._common_query(response)


	def get_parts(self) -> dict:

		return self.parts["parts"]


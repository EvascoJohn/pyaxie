import json


class ApiJSON(object):

	"""
		The GraphQL takes a specific format of JSON that it understands in order to give back data.
		this object holds the base format of what the GraphQL takes.
	"""

	def __init__(self):

		"""
			Initializes _json_body.   
		"""

		self._json_body = {

				"operationName": None,

				"variables": None,

				"query": None

				}



class GetBaseClass(ApiJSON):


	"""
		This class is inherited for all post queries. This class Holds all the similarities of the post queries.
	"""

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



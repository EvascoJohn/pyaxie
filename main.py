import requests
import time
from presenter import axie, get_lastest_axie


api_url = "https://graphql-gateway.axieinfinity.com/graphql"


latest = get_lastest_axie(
  {
    "from":0,
    "size":1,
    "sort":"Latest",
    "auctionType":"Sale",
    "class":"Plant",
    "parts":{},
    "stage":4
  }
)


if __name__ == '__main__':

  response = requests.post(api_url, json=latest.get_json())


  fetch = axie(response.json())

  if(fetch.if_price_usd(20.0)):

    if(fetch.if_parts({"name":"Papi", "body-part": "Eyes"})):

      print(fetch.get_id())
      print(fetch.get_name())
      print(fetch.get_class())
      print(fetch.get_price_usd())
      print(fetch.get_parts())

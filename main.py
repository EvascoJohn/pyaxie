import requests
import time

from api_model import GetAxieLatest


api_url = "https://graphql-gateway.axieinfinity.com/graphql"


latest = GetAxieLatest(
  {
    "from":0,
    "size":3,
    "sort":"Latest",
    "auctionType":"Sale",
    "class":"Plant",
    "stage":4
  }
)


if __name__ == '__main__':

  response = requests.post(api_url, json=latest.get_json())
  
import requests
import threading
import asyncio
import time
import os
from rich import print
from rich.columns import Columns
from presenter import axie, get_lastest_axie


api_url = "https://graphql-gateway.axieinfinity.com/graphql"


latest = get_lastest_axie(
  {
    "size":1,
    "sort":"Latest",
    "auctionType":"Sale",
    "class":"Plant",
    "stage":4
  }
)

async def main():

    buffer = 0


    while True:
        try:

            response = requests.post(api_url, json=latest.get_json())

            fetch = axie(response.json())

            if(await fetch.if_price_usd(10.0)):

                id = fetch.get_id()

                if id != buffer:

                    price = fetch.get_price_usd()
                    name = fetch.get_name()
                    axie_class = fetch.get_class()
                    price.center(40)
                    string = f"""ID: {id}CLASS: {axie_class}\nNAME: {name}PRICE: {price}\n"""
                    string.center(40)
                    print("-"*60)
                    print(string)
    
                buffer = id
        

        except KeyboardInterrupt:
            print("Program Stopped.")
            break

if __name__ == '__main__':
    asyncio.run(main())
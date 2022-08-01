import random
import time

import axie_model
import api_model
import api_query
import requests

from rich.live import Live
from rich.table import Table

def retrieve(results, Axie, table):
     for data in results():
        axie = Axie(data)
        table.add_row(axie.id, axie.name, f"[red]{axie.usd}" if float(axie.usd) > 10.0 else f"[green]{axie.usd}")


def generate_table() -> Table:
    table = Table(title="MARKET PLACE TRACKER BY: EVASCO", width=150, style="Yellow")
    table.add_column("ID", style="Yellow")
    table.add_column("NAME", style="Blue")
    table.add_column("PRICE USD", style="Green")

    api_url = "https://graphql-gateway.axieinfinity.com/graphql"

    size = 20

    latest_axie = api_model.GetAxieLatest({"size":size, "stage":4, "class":"Plant", "auctionType":"Sale", "sort":"Latest"})
    response = requests.post(api_url, json=latest_axie.get_json())
    rjson = response.json()
    results = api_query.Results(rjson)

    retrieve(results.get_results, axie_model.Axie, table)

    return table


with Live(generate_table(), refresh_per_second=4) as live:
    while True:
        try:
            live.update(generate_table())
        except KeyboardInterrupt:
            print("Program Ended.")
            break
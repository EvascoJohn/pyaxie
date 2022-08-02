import api_model
import requests
import api_query
import axie_model


api_url = "https://graphql-gateway.axieinfinity.com/graphql"


if __name__ == "__main__":
    latest_axie = api_model.GetAxieLatest({"size":1, "stage":4, "class":"Plant", "auctionType":"Sale", "sort":"Latest"})
    response = requests.post(api_url, json=latest_axie.get_json())
    rjson = response.json()
    query = api_query.Results(rjson)
    print(query.get_results())
import requests
import json

def getPrices():
    #dictionary containing: ore:[type_id, average market price]
    ores = {
        "Veldspar": [1230, 0],
        "Scordite": [1228, 0],
        "Kernite": [20, 0]
    }
    #url of eve api that returns market prices
    URL = "https://esi.evetech.net/latest/markets/prices/"

    getPrice = requests.get(url = URL)

    prices = getPrice.json()

    #finds each ore in the ore dictionary and updates the price
    for key, value in ores.items():
        for x in range(0, len(prices)):
            if prices[x]["type_id"] == value[0]:
                value[1] = prices[x]["average_price"]
                break

    return ores

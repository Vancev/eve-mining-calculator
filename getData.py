# Copyright (c) 2018 VanceV
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

import requests
import json

def getPrices(securityRating):
    #dictionary containing: ore:[type_id, average market price]
    ores = {}

    #Ore security ratings from eveuniversity.org
    if securityRating == 1:
        ores = {
            "Veldspar": [1230, 0],
            "Scordite": [1228, 0],
        }
    elif securityRating == .9 or securityRating == .8:
        ores = {
            "Veldspar": [1230, 0],
            "Scordite": [1228, 0],
            "Pyroxeres": [1224, 0],
            "Plagioclase": [18, 0]
        }
    elif securityRating == .6 or securityRating == .6 or securityRating == .5:
        ores = {
            "Veldspar": [1230, 0],
            "Scordite": [1228, 0],
            "Pyroxeres": [1224, 0],
            "Plagioclase": [18, 0],
            "Kernite": [20, 0],
            "Omber": [1227, 0]
        }
    elif securityRating == .4 or securityRating == .3:
        ores = {
            "Veldspar": [1230, 0],
            "Scordite": [1228, 0],
            "Pyroxeres": [1224, 0],
            "Plagioclase": [18, 0],
            "Kernite": [20, 0],
            "Omber": [1227, 0],
            "Jaspet": [1226, 0]
        }
    elif securityRating == .2 or securityRating == .1:
        ores = {
            "Veldspar": [1230, 0],
            "Scordite": [1228, 0],
            "Pyroxeres": [1224, 0],
            "Plagioclase": [18, 0],
            "Kernite": [20, 0],
            "Omber": [1227, 0],
            "Jaspet": [1226, 0],
            "Hemorphite": [1231, 0],
            "Hedbergite": [21, 0]
        }       
    elif securityRating == 0:
        ores = {
            "Veldspar": [1230, 0],
            "Scordite": [1228, 0],
            "Pyroxeres": [1224, 0],
            "Plagioclase": [18, 0],
            "Kernite": [20, 0],
            "Omber": [1227, 0],
            "Jaspet": [1226, 0],
            "Hemorphite": [1231, 0],
            "Hedbergite": [21, 0],
            "Spodumain": [19, 0],
            "Gneiss": [1229, 0],
            "Crokite": [1225, 0],
            "Arkonor": [22, 0],
            "Bistot": [1223, 0],
            "Mercoxit": [11396, 0],
            "Dark Ochre": [1232, 0],
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

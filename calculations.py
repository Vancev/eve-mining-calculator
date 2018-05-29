# Copyright (c) 2018 VanceV
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

from getData import *
from prettytable import PrettyTable

#returns the ammount of time until the cargo hold is full
#cargoSize, miningAmount, duration, lazerAmount
def fullHold(cs, ma, d, la):
    amountPerMine = float(ma) * float(la)
    minesPerCargo = float(cs) / float(amountPerMine)
    timeToFull = float(d) * float(minesPerCargo)
    return round(float(timeToFull)/60, 2)

#returns the isk per hold as well as isk per hour per each ore
#cargoSize, miningAmount, duration, lazerAmount, securityRating, travelTime
def iskPerHoldAndHour(cs, ma, d, la, sc):
    ores = getPrices(sc)
    amountPerMine = float(ma) * float(la)
    #isk per hour
    time = float(3600/d)
    orePerHour = float(amountPerMine*time)
    #value of a full cargo hold
    minesPerCargo = float(cs) / float(amountPerMine)
    totalMined = amountPerMine * minesPerCargo
    ore = PrettyTable(['Ore', 'Average Price', 'Value of Full Hold(ISK)', 'ISK per Hour'])
    #creates a string containing the ore name, value of full cargo hold, and isk per hour
    for key, value in ores.items():
        ore.add_row([str(key), str(value[1]), str(value[1] * totalMined), str(value[1] * orePerHour)])
    return ore

    #returns the isk per hold as well as isk per hour per each ore
#cargoSize, miningAmount, duration, lazerAmount, securityRating, travelTime
def iskPerHoldAndHourTimeGiven(cs, ma, d, la, sc, tt):
    ores = getPrices(sc)
    amountPerMine = float(ma) * float(la)
    #isk per hour
    time = float(3600/d)
    orePerHour = float(amountPerMine*time)
    #value of a full cargo hold
    hourDelay = float(float(tt)/60)
    oreLostPerHour = float(orePerHour*hourDelay)
    minesPerCargo = float(cs) / float(amountPerMine)
    totalMined = amountPerMine * minesPerCargo
    ore = PrettyTable(['Ore', 'Average Price', 'Value of Full Hold(ISK)', 'ISK per Hour of Mining', 'ISK per Hour Including Travel'])
    #creates a string containing the ore name, value of full cargo hold, and isk per hour
    for key, value in ores.items():
        ore.add_row([str(key), str(value[1]), str(value[1] * totalMined), str(value[1] * orePerHour), str(value[1] * (orePerHour-oreLostPerHour))])
    return ore
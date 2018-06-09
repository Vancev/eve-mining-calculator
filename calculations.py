# Copyright (c) 2018 VanceV
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.
from getData import *
from prettytable import PrettyTable
from helpers import commaFormat, hoursAndMinutes

#returns the ammount of time until the cargo hold is full
#cargoSize, miningAmount, duration, lazerAmount
def fullHold(cs, ma, d, la):
    amountPerMine = float(ma) * float(la)
    orePerSec = float(amountPerMine) / float(d)
    timeToFull = float(cs) / float(orePerSec)
    return round(float(timeToFull)/60, 2)

#returns the isk per hold as well as isk per hour per each ore
#cargoSize, miningAmount, duration, lazerAmount, securityRating, breakEven
def iskPerHoldAndHour(cs, ma, d, la, sc, be):
    ores = getPrices(sc)
    amountPerMine = float(ma) * float(la)
    #isk per hour
    time = float(3600/d)
    orePerHour = float(amountPerMine*time)
    #value of a full cargo hold
    minesPerCargo = float(cs) / float(amountPerMine)
    totalMined = amountPerMine * minesPerCargo
    #if break even ammount has not been entered
    if be == "":
        #creates a table containing the ore name, ore price, value of full cargo hold, and isk per hour
        ore = PrettyTable(['Ore', 'Average Price', 'Value of Full Hold(ISK)', 'ISK per Hour'])
        for key, value in ores.items():
            ore.add_row([str(key), commaFormat(value[2]), commaFormat((1.0/value[1]) * value[2] * totalMined), 
                        commaFormat((1.0/value[1]) * value[2] * orePerHour)])
    #if break even ammount has been entered
    else: 
        #creates a table containing the ore name, ore price, value of full cargo hold, isk per hour, and time to break even 
        ore = PrettyTable(['Ore', 'Average Price', 'Value of Full Hold(ISK)', 'ISK per Hour', 'Time to Break Even (HH:MM:SS)'])
        for key, value in ores.items():
            ore.add_row([str(key), commaFormat(value[2]), commaFormat((1.0/value[1]) * value[2] * totalMined), 
                        commaFormat((1.0/value[1]) * value[2] * orePerHour), hoursAndMinutes(float(be/((1.0/value[1]) * value[2] * orePerHour)))])
    return ore

#returns the isk per hold, isk per hour per each ore, and isk per hour with travel time
#cargoSize, miningAmount, duration, lazerAmount, securityRating, travelTime, breakEven
def iskPerHoldAndHourTimeGiven(cs, ma, d, la, sc, tt, be):
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
    #if break even ammount has not been entered
    if be == "":
        #creates a string containing the ore name, ore price, value of full cargo hold, isk per hour of mining, and isk per hour including travel
        ore = PrettyTable(['Ore', 'Average Price', 'Value of Full Hold(ISK)', 'ISK per Hour of Mining', 'ISK per Hour Including Travel'])
        for key, value in ores.items():
            ore.add_row([str(key), commaFormat(value[2]), commaFormat((1.0/value[1]) * value[2] * totalMined), 
                        commaFormat((1.0/value[1]) * value[2] * orePerHour), commaFormat((1.0/value[1]) * value[2] * (orePerHour-oreLostPerHour))])
    #break even amount has been entered
    else:
        #creates a string containing the ore name, ore price, value of full cargo hold, isk per hour, isk per hour including travel, and time to break even (based on isk/hr including travel)
        ore = PrettyTable(['Ore', 'Average Price', 'Value of Full Hold(ISK)', 'ISK per Hour of Mining', 'ISK per Hour Including Travel', 'Time to Break Even (HH:MM:SS)'])
        for key, value in ores.items():
            ore.add_row([str(key), commaFormat(value[2]), commaFormat((1.0/value[1]) * value[2] * totalMined), 
                        commaFormat((1.0/value[1]) * value[2] * orePerHour), commaFormat((1.0/value[1]) * value[2] * (orePerHour-oreLostPerHour)), 
                        hoursAndMinutes(float(be/((1.0/value[1]) * value[2] * (orePerHour - oreLostPerHour))))])
    return ore
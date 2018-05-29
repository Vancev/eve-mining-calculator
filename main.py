# Copyright (c) 2018 VanceV
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

from getData import *
from calculations import *
from helpers import *
import sys

#TODO user input error hanling, allowing to enter travel time, showing time to break even 
securityRating = ""
travelTime = ""
correctSC = False
try:
    #make sure securityRating input is a float between 0 and 1
    while securityRating > 1 or securityRating <0:
        while correctSC == False:
            securityRating = raw_input("Enter the lowest security rating to mine in (0-1): ")
            if isFloat(securityRating) == True:
                correctSC = True
                securityRating = float(securityRating)
            else:
                correctSC = False

    cargoSize = raw_input("Enter your cargo size: ")
    miningAmount = raw_input("Enter the mining lazers mining amount(per lazer): ")
    duration = raw_input("Enter the lazers duration in seconds: ")
    lazerAmount = raw_input("Enter the number of lazers: ")
    travelTime = raw_input("Enter your travel time. (Optional, press enter to skip: ")
    cargoSize = int(cargoSize)
    miningAmount = int(miningAmount)
    duration = int(duration)
    lazerAmount = int(lazerAmount)
    if travelTime:
        travelTime = int(travelTime)
except:
    print "A number must be entered for all inputs"
    sys.exit()

print "\nMining time to a full hold: ", fullHold(cargoSize, miningAmount, duration, lazerAmount), " minutes\n"
#calculates the isk for a full hold with each ore
ore = iskPerHoldAndHour(cargoSize, miningAmount, duration, lazerAmount, round(float(securityRating), 1))
print ore
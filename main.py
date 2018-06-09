# Copyright (c) 2018 VanceV
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

from getData import *
from calculations import *
from helpers import *

#TODO: make travel time calculations more accurate
securityRating = ""
correctInput = False
#make sure securityRating input is a float between 0 and 1
while correctInput == False:
    securityRating = raw_input("Enter the lowest security rating to mine in (0-1): ")
    if isFloat(securityRating) == True:
        securityRating = float(securityRating)
        if securityRating > 1 or securityRating <0:
            correctInput = False
        else:
            correctInput = True
    else:
        correctInput = False

correctInput = False
while correctInput == False:
    cargoSize = raw_input("Enter your cargo size: ")
    if isFloat(cargoSize) == True:
        correctInput = True
        cargoSize = float(cargoSize)
    else: 
        correctInput = False

correctInput = False
while correctInput == False:
    miningAmount = raw_input("Enter the mining lasers mining amount(per laser): ")
    if isFloat(miningAmount) == True:
        correctInput = True
        miningAmount = float(miningAmount)
    else:
        correctInput = False

correctInput = False
while correctInput == False:
    duration = raw_input("Enter the lasers duration in seconds: ")
    if isFloat(duration) == True:
        correctInput = True
        duration = float(duration)
    else:
        correctInput = False

correctInput = False
while correctInput == False:
    lazerAmount = raw_input("Enter the number of lasers: ")
    if isInt(lazerAmount) == True:
        correctInput = True
        lazerAmount = int(lazerAmount)
    else:
        correctInput = False

correctInput = False
travelTime = ""
while correctInput == False:
    travelTime = raw_input("Enter your round trip travel time in minutes. (Optional, press enter to skip): ")
    if isInt(travelTime) == True:
        correctInput = True
        lazerAmount = int(lazerAmount)
    elif travelTime == "":
        correctInput = True
    else:
        correctInput = False

correctInput = False
breakEven = ""
while correctInput == False:
    breakEven = raw_input("Enter the ammount of ISK needed to break even. (Optional, press enter to skip): ")
    if isInt(breakEven) == True:
        correctInput = True
        breakEven = int(breakEven)
    elif breakEven == "":
        correctInput = True
    else:
        correctInput = False

print "\nMining time to a full hold: ", fullHold(cargoSize, miningAmount, duration, lazerAmount), " minutes\n"
#calculates the isk for a full hold with each ore depending if travel time has been entered
if travelTime == "":
    ore = iskPerHoldAndHour(cargoSize, miningAmount, duration, lazerAmount, round(float(securityRating), 1), breakEven)
else:
    ore = iskPerHoldAndHourTimeGiven(cargoSize, miningAmount, duration, lazerAmount, round(float(securityRating), 1), travelTime, breakEven)
print ore
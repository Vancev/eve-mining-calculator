from getData import *
from calculations import *

cargoSize = input("Enter your cargo size: ")
miningAmount = input("Enter the mining lazers mining amount(per lazer): ")
duration = input("Enter the lazers duration in seconds: ")
lazerAmount = input("Enter the number of lazers: ")

print "Time to a full hold: ", fullHold(cargoSize, miningAmount, duration, lazerAmount), " minutes"
ore = "Ore \t\tValue of Full Hold(ISK)    ISK per Hour\n"
#calculates the isk for a full hold with each ore
ore += iskPerHold(cargoSize, miningAmount, duration, lazerAmount)
print ore
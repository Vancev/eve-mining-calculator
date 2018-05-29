from getData import *

#returns the ammount of time until the cargo hold is full
#cargoSize, miningAmount, duration, lazerAmount
def fullHold(cs, ma, d, la):
    amountPerMine = float(ma) * float(la)
    minesPerCargo = float(cs) / float(amountPerMine)
    timeToFull = float(d) * float(minesPerCargo)
    return round(float(timeToFull)/60, 2)

#returns the isk per hold as well as isk per hour per each ore
#cargoSize, miningAmount, duration, lazerAmount, securityRating
def iskPerHold(cs, ma, d, la, sc):
    ores = getPrices(sc)
    amountPerMine = float(ma) * float(la)
    #isk per hour
    time = float(3600/d)
    orePerHour = float(amountPerMine*time)
    #value of a full cargo hold
    minesPerCargo = float(cs) / float(amountPerMine)
    totalMined = amountPerMine * minesPerCargo
    ore = ""
    #creates a string containing the ore name, value of full cargo hold, and isk per hour
    for key, value in ores.items():
        ore+=str(key) + " \t" + str(value[1] * totalMined) + "     \t\t" + str(value[1] * orePerHour) + "\n"
    return ore
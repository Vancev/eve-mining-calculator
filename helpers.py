# Copyright (c) 2018 VanceV
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

#returns true if item passed in is a float. Returns false otherwise
def isFloat(number):
    try:
        float(number)
        return True
    except:
        return False

#returns true if item passed in is an int. Returns false otherwise
def isInt(number):
    try:
        int(number)
        return True
    except:
        return False

#formats number with commas
def commaFormat(number):
    return '{:,.2f}'.format(float(number))

def hoursAndMinutes(number):
    hours = int(number)
    minutes = int((number*60) % 60)
    seconds = int((number*3600) % 60)
    return str(hours) + ':' + str(minutes) + ':' + str(seconds)

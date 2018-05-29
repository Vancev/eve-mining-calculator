# Copyright (c) 2018 VanceV
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

def isFloat(number):
    try:
        float(number)
        return True
    except:
        return False

def isInt(number):
    try:
        int(number)
        return True
    except:
        return False

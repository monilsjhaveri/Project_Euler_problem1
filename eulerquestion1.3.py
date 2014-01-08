#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Monil Jhaveri
#
# Created:     07/01/2014
# Copyright:   (c) MonilRushi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def euler1(x):
    total = 0
    for i in range(0, x):
        if (i%3 == 0) or (i%5 == 0) :
            total += i
    return total

print euler1(1000)


#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      MonilRushi
#
# Created:     06/01/2014
# Copyright:   (c) MonilRushi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def euler1(x):
    ans = []
    sub = []
    t = 0
    if ((x%3) or (x%5)):
        ans.append(x)
    if (x%3) and (x%5):
        sub.append(x)
    ans.remove(sub)
    for i in ans:
        t += i
    return t

print euler1(1000)


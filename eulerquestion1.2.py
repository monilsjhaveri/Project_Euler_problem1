#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MonilRushi
#
# Created:     07/01/2014
# Copyright:   (c) MonilRushi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
def euler1(x):
    total = 0
    sub = 0
    for i in range(1, x):
        if (i%3 == 0):
            total += i
    for i in range(1, x):
        if (i%5 == 0):
            total += i
    for i in range(1, x):
        if (i%15 == 0):
            sub += i
    ans = total - sub
    return ans

print euler1(1000)

from decimal import *
getcontext().prec = 6

PSI = input()
PSI = float(PSI)

kc2 = 0.07030690061*PSI

def isint(num = None):
    if int(num*100000) == int(num)*100000:
        return True
    return False

kc2 = Decimal(kc2) / Decimal(1)
kc2 = float(kc2)

if isint(kc2):
    print(int(kc2))
else:
    print(kc2)
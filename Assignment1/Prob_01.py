from decimal import*
getcontext().prec = 6

F = input()
F = float(F)

C = 5/9*(F - 32)
K = (F - 32)/1.8 + 273.15

C = Decimal(C) / Decimal(1)
K = Decimal(K) / Decimal(1)

C = float(C)
K = float(K)

def isint(num = None):
    if int(num*100000) == int(num)*100000:
        return True
    return False
if isint(C) and isint(K):
    print(int(C),int(K))
elif isint(C) and not isint(K):
    print(int(C),float(K))
elif not isint(C) and not isint(K):
    print(float(C),float(K))
else:
    print(float(C),int(K))
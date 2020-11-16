from math import *

a = input()
b = input()
c = input()

a = float(a)
b = float(b)
c = float(c)

S = sqrt((a**2 + b**2 + c**2)**2 - 2*(a**4 + b**4 + c**4))/4
S = round(S,2)

if int(S * 100) == int(S)*100:
    S = int(S)

if a + b <= c or a + c <= b or b + c <= a:
    print("Khong phai tam giac")
else:
    if a == b or a == c or b == c:
        if a == b == c:
            print("Tam giac deu, dien tich =", S)
        else:
            print("Tam giac can, dien tich =", S)
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giac vuong, dien tich =", S)
    else:
        print("Tam giac thuong, dien tich =", S)
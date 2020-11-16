x = input()
x = int(x)

def Fibonaci(num = None):
    if num == 1 or num == 2:
        return 1
    return Fibonaci(num - 1) + Fibonaci(num - 2)
if (x < 1) or (x > 30) :
    print("So",x,"khong nam trong khoang [1,30].")
else:
    print(Fibonaci(x))
n = input()
k = input()
p = input()
q = input()

n = int(n)
k = int(k)
p = int(p)
q = int(q)

Alice = 0
if q == 1:
    Alice = p*2 - 1
else:
    Alice = p*2
Bob = Alice - k
if Bob <= 0:
    Bob = Alice + k
if Bob > n:
    print(-1)
else:
    temp = Bob % 2
    if temp == 0:
        u = Bob / 2
        v = 2
    else:
        u = (Bob + 1)/2
        v = 1
    print(int(u),v)
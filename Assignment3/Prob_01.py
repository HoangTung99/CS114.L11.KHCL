(a, b) = input().split()
m = int(a)
n = int(b)
def X(a,b,t):
  if b == 1:
      return a 
  else:
    x = pow(a, b//2,t)
    if b % 2 == 1:
      return ((x**2) * a) % t
    else:
      return (x**2)%t

print(X(m, n, 10**9 + 7))
n = input()
i=0
t = 0
while i < len(n):
  if n[i]=='4' or n[i]=='7':
    t = t+1
  i = i +1
if t == 4 or t == 7:
  print('YES')
else:
  print('NO')

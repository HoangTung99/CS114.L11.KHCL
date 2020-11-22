arr = input().split(' ')
arrA = input().split(' ')
arrB = input().split(' ')

nA = int(arr[0])
nB = int(arr[1])
cA = 0
cB = 0
re = []

while(cA < nA or cB < nB):
  if cA < nA and cB < nB:
    if int(arrA[cA]) > int(arrB[cB]):
      re.append(arrB[cB])
      cB += 1
    else:
      re.append(arrA[cA])
      cA += 1
  elif cA >= nA and cB < nB:
    re.append(arrB[cB])
    cB += 1
  elif cA < nA and cB >= nB:
    re.append(arrA[cA])
    cA += 1
  else:
    break


print(" ".join(re))
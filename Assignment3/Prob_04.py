
def isInclude(target, array):
  for e in array:
    if target == e:
      return True
  return False

n = int(input())
array = input().split()
sizeOfArray = len(array)
for i in range(0, sizeOfArray):
  array[i] = int(array[i])

min = array[0]
max = array[0]

for e in array:
  if e < min:
    min = e
  if e > max:
    max = e

print(max - min - (sizeOfArray - 1))
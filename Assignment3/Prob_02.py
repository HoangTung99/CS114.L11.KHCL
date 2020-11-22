n = int(input())
(x, y) = (int(x) for x in input().split())

whiteX = 1
whiteY = 1
blackX = n
blackY = n

whiteSteps = 0
blackSteps = 0

#-- Calculate white's steps:
# 1. On the same row
if whiteX == x:
  whiteSteps = abs(y -  whiteY)

# 2. On the same column
elif whiteY == y:
  whiteSteps = abs(x - whiteX)

# 3. Not both
elif whiteX != x and whiteY != y:
  # a. Buoc cheo
  if x >= y:
    whiteSteps = abs(y - whiteY)
    whiteX += whiteSteps
    whiteY += whiteSteps
  else:
    whiteSteps = abs(x - whiteX)
    whiteX += whiteSteps
    whiteY += whiteSteps

  # b. Sau do, buoc ngang hoac doc
  if whiteX != x:
    whiteSteps += abs(x - whiteX)
    whiteX += abs(x - whiteX)
  
  elif whiteY != y:
    whiteSteps += abs(y - whiteY)
    whiteY += abs(y - whiteY)
  


#-- Calculate black's steps:
# 1. On the same row
if blackX == x:
  blackSteps = abs(y -  blackY)

# 2. On the same column
elif blackY == y:
  blackSteps = abs(x - blackX)

# 3. Not both
elif blackX != x and blackY != y:
  # a. Buoc cheo
  if x <= y:
    blackSteps = abs(y - blackY)
    blackX -= blackSteps
    blackY -= blackSteps
  else:
    blackSteps = abs(x - blackX)
    blackX -= blackSteps
    blackY -= blackSteps

  # b. Sau do, buoc ngang hoac doc
  if blackX != x:
    blackSteps += abs(x - blackX)
    blackX -= abs(x - blackX)
  
  elif blackY != y:
    blackSteps += abs(y - blackY)
    blackY -= abs(y - blackY)
  


if whiteSteps <= blackSteps:
  print("White")

else:
  print("Black")
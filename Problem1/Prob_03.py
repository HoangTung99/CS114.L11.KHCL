from decimal import *

inp = input()
loc = inp.find(" ")

xxx = int(inp[0:loc])
yy = int(inp[loc + 1:len(inp)])

ga = int(2*xxx - yy/2)
cho = int(yy/2 - xxx)

print(ga,cho)
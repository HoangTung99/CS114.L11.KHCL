inp = input()
lo = inp.rfind(" ")

k = inp[0:lo]
t = inp[lo+1:]

k = int(k)
t = int(t)

du = t % k
thuong = t // k
ga = 0
if thuong % 2 == 0:
    ga = du
else:
    ga = k - du
print(ga)
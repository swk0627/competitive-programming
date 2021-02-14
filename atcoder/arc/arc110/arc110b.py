import math
n = int(input())
t = input()
s = '110' * (n // 3 + 1)
if t == '0': print(int(1e10))
elif t == '1': print(2 * int(1e10))
elif t in '110' * math.ceil(n / 3):
    print(int(1e10) - (math.ceil(n / 3) - 1))
elif t in '110' * (math.ceil(n / 3) + 1):
    print(int(1e10) - (math.ceil(n / 3)))
else: print(0)
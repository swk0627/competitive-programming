import itertools
import math
n = int(input())
x = list(map(int, input().split()))
ans = 100 ** 14
pnums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for k in range(1, len(pnums)+1):
    for c in itertools.combinations(pnums, k):
        mul = 1
        flg = True
        for num in c: mul *= num
        for num in x:
            if math.gcd(mul, num) == 1:
                flg = False
        if flg:
            ans = min(ans, mul)
print(ans)
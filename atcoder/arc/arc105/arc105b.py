import math
n = int(input())
a = list(map(int, input().split()))
M = max(a)
m = min(a)
while(M != m):
    for i in range(n):
        if a[i] != m:
            a[i] -= m * (math.ceil(a[i] / m) - 1)
    M = max(a)
    m = min(a)
print(m)
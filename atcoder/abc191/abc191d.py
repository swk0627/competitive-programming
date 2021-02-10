import math
X, Y, R = map(float, input().split())
times = 10000

def isqrt(n):
  k1 = 0
  k2 = n
  mid = 0
  while True:
    mid = (k1 + k2) // 2
    if mid * mid <= n and (mid+1) * (mid+1) > n:
      return mid
    if mid * mid <= n:
      k1 = mid + 1
    else:
      k2 = mid - 1

ans = 0
low = int(round(math.ceil(X - R) * times))
high = int(round(math.floor(X + R) * times))
X = int(round(times * X))
Y = int(round(times * Y))
R = int(round(times * R))

for i in range(low, high + times, times):
    dy = isqrt(R ** 2 - (X - i) ** 2)
    e = math.floor((Y + dy)/times)
    s = math.ceil((Y - dy)/times)
    ans += e - s + 1
print(ans)
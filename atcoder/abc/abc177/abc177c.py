n = int(input())
a = list(map(int, input().split()))
ans = 0
s = sum(a[1:])
for i in range(n-1):
    ans += a[i] * s
    ans %= (10 ** 9 + 7)
    s -= a[i+1]
print(ans)
n = int(input())
a = list(map(int, input().split()))
ans = 0
s = sum(a)
for num in a:
    s -= num
    ans += (n - 1) * (num ** 2)
    ans -= 2 * (num * s)
print(ans)
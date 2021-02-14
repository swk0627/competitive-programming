b, c = map(int, input().split())
ans = 1
if b > 0:
    ans += (c - 1) // 2
    ans += ans
    if c - 1 >= 2 and (c - 1) % 2 == 0:
        ans -= 1
    ans += min(abs(b) * 2 - 1, c // 2 * 2)
    if abs(b) * 2 - 1 > c // 2 * 2 and c % 2 == 0:
        ans -= 1
if b == 0:
    ans += c // 2
    ans += c // 2
    if c % 2 == 0:
        ans -= 1
if b < 0:
    ans += c // 2
    ans += ans
    if c % 2 == 0:
        ans -= 1
    ans += min(abs(b) * 2 - 1, (c - 1) // 2 * 2)
    if abs(b) * 2 - 1 > (c - 1) // 2 * 2 and (c - 1) % 2 == 0:
        ans -= 1
print(ans)
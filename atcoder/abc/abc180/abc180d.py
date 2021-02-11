x, y, a, b = map(int, input().split())
cnt = 0
while a * x < y and a * x < b:
    cnt += 1
    x *= a
if y - x > 0:
    cnt += (y - x) // b
if (y - x) % b == 0:
    cnt -= 1
print(cnt)
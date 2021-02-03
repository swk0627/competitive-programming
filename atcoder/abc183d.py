n, w = map(int, input().split())
event = []
for _ in range(n):
    s, t, p = map(int, input().split())
    event.append((t, -p))
    event.append((s, p))
event.sort()
t = 0
water = 0
for x, y in event:
    water += y
    if w < water:
        print('No')
        exit()
print('Yes')
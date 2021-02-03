n = int(input())
flg = True
t_t, t_x, t_y = 0, 0, 0
for _ in range(n):
    t, x, y = map(int, input().split())
    dt = t - t_t
    dist = abs(x - t_x) + abs(y - t_y)
    flg = (dt >= dist) & (dt % 2 == dist % 2) & flg
    t_t, t_x, t_y = t, x, y
if flg: print('Yes')
else: print('No')
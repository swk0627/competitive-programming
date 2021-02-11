N = int(input())
tmp = 0
Ps = []
for _ in range(N):
	x, y = map(int, input().split())
	Ps.append([x, y])
for i in range(N):
	x1, y1 = Ps[i][0], Ps[i][1]
	for j in range(i+1, N):
		x2, y2 = Ps[j][0], Ps[j][1]
		if(-1 <= (y2-y1)/(x1-x2) <= 1):	tmp += 1
print(tmp)
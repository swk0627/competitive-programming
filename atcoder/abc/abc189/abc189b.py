N, X = map(int, input().split())
tmp = 0
X *= 100
for i in range(N):
	V, P = map(int, input().split())
	tmp += V * P
	if(tmp > X):
		print(i+1)
		break
else: print(-1)
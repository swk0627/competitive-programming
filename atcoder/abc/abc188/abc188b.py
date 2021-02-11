N = int(input())
tmp = 0
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
for i in range(N):
	tmp += As[i] * Bs[i]
if(tmp == 0): print('Yes')
else: print('No')
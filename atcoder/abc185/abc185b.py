N, M, T = map(int, input().split())
N0 = N
tmp = 0
for _ in range(M):
	A, B = map(int, input().split())
	N -= A - tmp
	if(N <= 0):
		print('No')
		exit()
	N += B - A
	if(N > N0): N = N0
	tmp = B
N -= T - tmp
if(N <= 0): print('No')
else: print('Yes')
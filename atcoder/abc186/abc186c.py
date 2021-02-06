N = int(input())
cnt = 0
for num in range(N):
	S = str(num+1)
	O = oct(num+1)
	OS = str(num+1)
	S = set(list(S))
	OS = set(list(O))
	if '7' in S or '7' in OS:
		cnt += 1
print(N - cnt)
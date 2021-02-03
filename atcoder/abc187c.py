N = int(input())
S = set()
for _ in range(N):
	S.add(input())
for T in S:
	if '!' + T in S:
		print(T)
		exit()
print('satisfiable')
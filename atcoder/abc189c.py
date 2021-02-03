N = int(input())
A = list(map(int, input().split()))
INF = float('inf')
ans = 0
for i in range(N):
    m = INF
    for j in range(i, N):
        m = min(m, A[j])
        ans = max(ans, m * (i - j + 1))
print(ans)
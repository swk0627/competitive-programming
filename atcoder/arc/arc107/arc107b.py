n, k = map(int, input().split())
k = abs(k)
ans = 0
for i in range(k+2, 2*n+1):
    j = i - k
    ans += min(i-1, 2*n-i+1) * min(j-1, 2*n-j+1)
print(ans)
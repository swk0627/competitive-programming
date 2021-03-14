n = int(input())
s = list(map(int, input()))
x = input()
dp = [ [] for _ in range(200001)]
dp[n].append(0)
for i in range(1, n+1)[::-1]:
    if x[i-1] == 'T':
        for r in range(7):
            dp[i-1].append(r) if (10 * r) % 7 in dp[i] or (10 * r + s[i-1]) % 7 in dp[i] else None
    if x[i-1] == 'A':
        for r in range(7):
            dp[i-1].append(r) if (10 * r) % 7 in dp[i] and (10 * r + s[i-1]) % 7 in dp[i] else None
print(dp[:n+1])
print('Takahashi' if 0 in dp[0] else 'Aoki')
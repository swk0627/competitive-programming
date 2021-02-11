h, w = map(int, input().split())
s = [ 0 for j in range(h)]
for i in range(h): s[i] = list(input())
ans = 0
for i in range(1, h):
    for j in range(1, w):
        cnt = 0
        if s[i][j] == '#': cnt += 1
        if s[i-1][j] == '#': cnt += 1
        if s[i][j-1] == '#': cnt += 1
        if s[i-1][j-1] == '#': cnt += 1
        if cnt == 1 or cnt == 3: ans += 1
print(ans)
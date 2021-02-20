n, m = map(int, input().split())
p = [ [] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    p[a-1].append(b-1)
    p[b-1].append(a-1)
visited = [ 0 for _ in range(n)]
ans = 0
for i in range(n):
    if not visited[i]:
        cnt = 0
        visited[i] = 1
        stack = []
        stack.append(i)
        while stack:
            node = stack.pop()
            cnt += 1
            for j in p[node]:
                if not visited[j]:
                    visited[j] = 1
                    stack.append(j)
    ans = max(ans, cnt)
print(ans)
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
graph = [ [] for _ in range(n)]
for _ in range(m):
    c, d = map(int, input().split())
    graph[c-1].append(d-1)
    graph[d-1].append(c-1)
visited = [ 0 for _ in range(n)]
for i in range(n):
    if not visited[i]:
        stack = [i]
        curr = 0
        visited[i] = 1
        while stack:
            node = stack.pop()
            curr += a[node] - b[node]
            for j in graph[node]:
                if not visited[j]:
                    visited[j] = 1
                    stack.append(j)
        if curr:
            print('No')
            exit()
print('Yes')
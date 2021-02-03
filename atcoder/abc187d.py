n = int(input())
a, b = [], []
cnt = 0
for _ in range(n):
    x = list(map(int, input().split()))
    a.append(x[0])
    b.append(x[1])
x = -1 * sum(a)
l = [ 2 * i + j for i, j in zip(a, b)]
l.sort(reverse=True)
for i in l:
    x += i
    cnt += 1
    if x > 0: break
print(cnt)
import itertools

n, m = map(int, input().split())
cond = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
choice = [tuple(map(int, input().split())) for _ in range(k)]
ans = 0
for balls in itertools.product(*choice):
    cnt = sum(A in balls and B in balls for A, B in cond)
    if ans < cnt:
        ans = cnt
print(ans)
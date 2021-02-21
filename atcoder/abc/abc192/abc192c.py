n, k = tuple(input().split())
k = int(k)
ans = int(n)
for i in range(k):
    li = list(n)
    li.sort()
    l = int(''.join(li))
    h = int(''.join(li[::-1]))
    ans = h - l
    n = str(ans)
print(ans)
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
length = len(a) - 1
tmp = 0
ans = 0
for i in a:
    ans += i * (length - tmp) - i * tmp
    tmp += 1
print(ans)
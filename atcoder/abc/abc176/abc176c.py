n = int(input())
a = list(map(int, input().split()))
max_num = 0
ans = 0
for num in a:
    if max_num < num: max_num = num
    else: ans += max_num - num
print(ans)
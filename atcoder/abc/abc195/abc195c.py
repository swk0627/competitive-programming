n = int(input())
ans = 0
nines = 999
while(n - nines > 0):
    ans += n - nines
    nines *= 1000
    nines += 999
print(ans)
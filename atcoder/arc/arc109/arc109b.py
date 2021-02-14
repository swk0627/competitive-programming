n = int(input())
left = 0
right = n + 1
while(right - left > 1):
    x = (left + right) // 2
    if x*(x+1) <= 2*(n+1): left = x
    else: right = x
k = left
print(n - k + 1)
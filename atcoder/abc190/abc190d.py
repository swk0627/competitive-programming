n = 2 * int(input())
cnt = 0
for i in range(1, int(n**0.5)+1):
    if i % 2 != n // i % 2 and n % i == 0: cnt += 2
print(cnt)
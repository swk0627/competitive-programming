n = int(input())
a = list(map(int, input().split()))
print(sum(sorted(a, reverse=True)[::2]) - sum(sorted(a, reverse=True)[1::2]))
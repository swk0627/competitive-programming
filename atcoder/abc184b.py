x = int(input().split()[1])
s = input()
for c in s:
    if c == 'o': x += 1
    elif x > 0: x -= 1
print(x)

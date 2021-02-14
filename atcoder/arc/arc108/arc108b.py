n = int(input())
s = input()
a = []
for c in s:
    a.append(c)
    if c == 'x' and a[-3:] == ['f', 'o', 'x']:
        a.pop()
        a.pop()
        a.pop()
print(len(a))
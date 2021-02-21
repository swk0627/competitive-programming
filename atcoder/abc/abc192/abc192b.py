s = input()
for i, c in enumerate(s):
    if i % 2 == 0:
        if not c.islower():
            print('No')
            exit()
    if i % 2 == 1:
        if not c.isupper():
            print('No')
            exit()
print('Yes')
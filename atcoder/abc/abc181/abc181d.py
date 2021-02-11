from collections import Counter
s = input()
if len(s) <= 2:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0: print('Yes')
    else: print('No')
    exit()
for i in range(104, 1000, 8):
    if not Counter('000') - Counter(s):
        print('Yes')
        exit()
    if not Counter(str(i)) - Counter(s):
        print('Yes')
        exit()
print('No')
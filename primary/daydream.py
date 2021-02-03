s = input()
flg = True
while(flg):
    flg = False
    if s.endswith('dream'):
        s = s[:-5]
        flg = True
    if s.endswith('dreamer'):
        s = s[:-7]
        flg = True
    if s.endswith('erase'):
        s = s[:-5]
        flg = True
    if s.endswith('eraser'):
        s = s[:-6]
        flg = True
if s == '': print('YES')
else: print('NO')
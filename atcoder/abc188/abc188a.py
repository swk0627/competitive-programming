s = input().split()
s[0] = int(s[0])
s[1] = int(s[1])
if(s[0] < s[1]): 
	if(s[0]+3 > s[1]): print('Yes')
	else: print('No')
else:
	if(s[1]+3 > s[0]): print('Yes')
	else: print('No')
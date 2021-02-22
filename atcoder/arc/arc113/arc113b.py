mod = lambda x: int(x) % 40 if int(x) % 40 != 0 else 40
nums = list(map(mod, input().split()))
tmp = nums[1] ** nums[2]
tmp = mod(tmp)
tmp = nums[0] ** tmp
tmp = tmp % 10
print(tmp)
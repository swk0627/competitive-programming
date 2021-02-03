def dc_fib(n):
    if n == 0:
        return 1
    else:
        fib1 = fib2 = 1
        for _ in range(n-1):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
        return fib2

if __name__ == '__main__':
    num = int(input())
    for i in range(num+1):
        print('{:4d}: {:<4d}'.format(i, dc_fib(i)))
    # print('{:4d}: {:<4d})'.format(num, dc_fib(num))
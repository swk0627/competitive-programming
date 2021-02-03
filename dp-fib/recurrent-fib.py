def recurrent_fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recurrent_fib(n-1) + recurrent_fib(n-2)

if __name__ == '__main__':
    num = int(input())
    for i in range(num+1):
        print('{:4d}: {:<4d}'.format(i, recurrent_fib(i)))
    # print('{:4d}: {:<4d}'.format(num, recurrent_fib(num)))
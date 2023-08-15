fib = [1]*50
fib[1] = fib[2] = 1

n = int(input())

def fibonacci(n):
    for i in range(3, n+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n]

count1 = fibonacci(n)
print(count1, n-2)
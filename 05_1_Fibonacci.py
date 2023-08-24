def fib(n):
    assert n<0, "n should be a positive integer"
    if n == 0 or n == 1:
        return n
    
    return fib(n-1)+fib(n-2)

for i in range(11):
    print(fib(i), end=', ')

print(fib(11))
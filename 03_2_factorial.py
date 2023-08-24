def f(n: int) -> int:
    if n == 0:
        return 1
    
    return n*f(n-1)

ans = f(5)
print(ans)
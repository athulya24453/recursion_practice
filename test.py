def f(i, j):
    if i == 1 or j == 1:
        return 1
    
    return f(i, j-1) + f(i-1, j)

print(f(6,6))
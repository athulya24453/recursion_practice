sum = 0

def solution(i,n):
    global sum

    if i < 1:
        return
    
    solution(i-1, n)
    sum += i

    return sum

def sol2(i, s = 0):
    if i < 1:
        print(s)
        return
    
    sol2(i-1, s+i)

def sol3(n):
    if n == 0:
        return 0
    
    return (n + sol3(n-1))

print(solution(10,10))
sol2(10)
print(sol3(3))
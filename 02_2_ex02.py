count = 0

def solution(n):
    global count
    print(n-count)
    count += 1

    if count == (n):
        return
    
    solution(n)

def solution2(i, n = 1):
    print(i)

    if i == n:
        return
    
    solution2(i-1)

solution2(5)
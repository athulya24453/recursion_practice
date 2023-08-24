count = 0

def solution(n):
    global count
    print(count)
    count += 1
    

    if count == n:
        return
    
    solution(n)

def solution2(i,n):
    print(i)

    if i == n:
        return
    
    solution2((i+1),n)
    
solution2(1,5)
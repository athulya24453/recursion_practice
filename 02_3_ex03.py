def solution(i,n):
    if i<1:
        return
    
    solution(i-1,n)
    print(i)
    
solution(5,5)
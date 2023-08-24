def solution(n:int, i=1):
    if i>n:
        return
    
    solution(n,i+1)
    print(i)

solution(10)


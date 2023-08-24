def f(i: int, sarr):
    global n
    global arr
    if i >= n:
        print(sarr)
        return
    
    sarr.append(arr[i])
    f(i+1, sarr)
    sarr.pop()
    f(i+1,sarr)
    
arr = [3,1,2,5]
sarr = []
n = len(arr)
f(0,sarr)
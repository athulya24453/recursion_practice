def f(i, s, sarr):
    global n
    global arr
    global k

    if i >= n:
        if s == k:
            print(sarr)
        return
    
    sarr.append(arr[i])
    s += arr[i]
    f(i+1, s, sarr)

    sarr.pop()
    s -= arr[i]
    f(i+1, s, sarr)

arr = [1,2,1,3,1,2]
n = len(arr)
k = 4
f(0, 0, [])
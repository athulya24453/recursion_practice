def f(k, i, sarr):
    global n
    global arr

    if i >= n:
        sum = 0
        l = len(sarr)
        for i in range(l):
            sum += sarr[i]

        if sum == k:
            print(sarr)
        return
    
    sarr.append(arr[i])
    f(k,i+1, sarr)
    sarr.pop()
    f(k,i+1, sarr)

arr = [2,4,3,5]
n = len(arr)
sarr = []
f(6,0,sarr)

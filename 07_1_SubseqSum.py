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

def g(i, s, sarr):
    global n
    global arr
    global k

    if i >= n:
        if s == k:
          print(sarr)
        return
    
    s += arr[i]
    sarr.append(arr[i])
    g(i+1, s, sarr)
    s -= arr[i]
    sarr.pop()
    g(i+1, s, sarr)

arr = [2,4,3,5,1]
n = len(arr)
sarr = []
k = 6
f(6,0,sarr)
print("--------------------------------------")
g(0, 0, sarr)

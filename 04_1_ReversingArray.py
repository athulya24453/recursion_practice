def reverseArr(arr, i):
    l = len(arr)

    if i == l//2:
        return

    temp = arr[i]
    arr[i] = arr[l-1-i]
    arr[l-1-i] = temp

    reverseArr(arr, i+1)

exarr = "ABCD"
reverseArr(exarr,0)
print(exarr)
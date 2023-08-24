count = 0

def pal(s, i):
    global count
    global l

    if i == l//2:
        return
    
    if s[i] == s[l-1-i]:
        count += 1

    pal(s, i+1)

def pal2(S, i):
    global l

    if i == l//2:
        return True
    
    if s[i] != s[l-i-1]:
        return False
    
    return pal2(s, i+1)

s = "madma"
l = len(s)

# pal(s, 0)

# # print(count)

# if count == l//2 and l != 0:
#     print("Yes")

# else:
#     print("No")

if pal2(s, 0):
    print("Yes")

else:
    print("No")


    
    
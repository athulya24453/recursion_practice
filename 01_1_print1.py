# This is an infinite loop (ctrl+c) to stop

count = 0

def print1():
    global count
    print(1)
    count += 1
    if count == 10:
        return

print1()
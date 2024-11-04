import time
h = 0
m = 0
t = input("Enter time limit: ")
while m < 60:
    print(h, ":", m)
    time.sleep(1)
    if m == 59:
        h += 1
        m = -1
    if h == int(t):
        break
    m += 1

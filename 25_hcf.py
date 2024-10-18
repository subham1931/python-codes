import time
def hcf (a,b):
    t1 = time.time()
    while b != 0:
        a,b = b, a %  b
    t2 = time.time()
    t = t2-t1
    print(t)
    return a

def hcff(a,b):
    t1 = time.time()
    sm = b if a>b else a
    for i in range(1,sm+1):
        if ((a % i == 0) and (b % i == 0)):
            hcf = i
    t2 = time.time()
    t = t2-t1
    print(t)
    return hcf
print(hcf(24,54))
print(hcff(24,54))
# print(hcff(54,24))
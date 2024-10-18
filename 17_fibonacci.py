num = int(input("Enter the number of fibonaccie sequence you want : "))
a =0
b =1

fibonaci = []
if num == 1:
    fibonaci.append(a)
    print(a)
elif num == 2:
    fibonaci.extend([a,b])
    print(a,b)
elif num > 2:
    fibonaci.extend([a,b])
    print(a,b,end=' ')
    for i in range(num-2):
        c = a + b
        a = b
        b = c
        print(c,end=' ')
        fibonaci.append(c)

print(fibonaci)
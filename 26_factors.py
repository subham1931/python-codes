num =  12

for i in range(1,num+1):
    if num % i == 0:
        print(i)

def factor(num):
    return [i for i in range(1,num+1) if num % i == 0 ]

print(factor(12))
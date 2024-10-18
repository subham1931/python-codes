res=[]
for num in range(1,1000):
    if num == sum(int(i)**len(str(num)) for i in str(num)):
        res.append(num)
print(f'{res} -> {len(res)}')
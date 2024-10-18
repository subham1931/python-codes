num = 12
res = [i for i in range(1, 100) if i % num == 0]
res2 = list(filter(lambda a: a % num ==0,range(1,100)))
print(res)
print(res2)

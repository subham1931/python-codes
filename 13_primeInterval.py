def primes(num):
    primes_list = []

    if num > 1:
        for i in range(1,num+1):
            for j in range(2,num):
                if i % j == 0:
                    break
                else:
                    primes_list.append(i)
                    break
    return primes_list


print(primes(5))
def isPrime(num):
    if num <= 1 :
        return 'not prime'
    for i in range(2,num):
        if num % 2 == 0 :
            return 'Not Prime'
    return "Prime"

print(isPrime(10))
print(isPrime(11))
n1,n2,n3 = input("Enter three nulmer for check th greates : ").split(' ')

if n1 > n2 and n1 > n3:
    print(f"greatest is {n1}")
elif n2 > n1 and n2 > n3:
    print(f"greatest is {n2}")
else:
    print(f"greatest is {n3}")


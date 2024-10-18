num = int(input("Enter a number to check odd or even: "))

if num >= 0:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is negetive")
num = int(input("Enter anumer for find sum of natutral number till thaat : "))
if num > 1:
    ans = (lambda i: sum(range(1,i +1)))(num)
    print(ans)
else:
    print("Please enter a number greater than 1")
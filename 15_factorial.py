# def factorial(num):
#     if num < 1 :
#         return print("please enter an positive nonzero number")
    
#     else:
#         fact = 1
#         for i in range(1,num+1):
#             fact *= i
#     return fact

# num = int(input("Enter a nuber for find factorial"))
# print(factorial(num))


###using recursion

def fact(num):
    if num == 0 :
        return 1
    else:
        return num * fact(num - 1)

print(fact(5))


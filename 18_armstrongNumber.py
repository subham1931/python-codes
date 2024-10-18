num = input("Enter a number for check amstrong number : ")

# sum= 0
# for i in num:
#     sum += int(i)**3

# if int(num) == sum:
#     print(f"{num} was an armstrong number ")
# else:
#     print(f'{num} was not an armstrong number')

print(f"{num} is armstrong " if int(num) == sum(int(i)**3 for i in num) else f"{num} is not armstrong")
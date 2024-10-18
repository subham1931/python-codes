import random

s,e = map(int,input("enter a starting and ending number to generate an random number  : ").split(','))
print(random.randint(s,e))
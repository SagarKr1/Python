# 1. Write a Python program that checks if a number is prime using a for loop.

n = int(input("Enter a number: "))
count=0
for i in range(2,n):
    if(n%i==0):
        count +=1
        break

if count!=0:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
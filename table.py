# 4. Write a Python function called multiplication_table that takes an integer n as input and 
# prints the multiplication table for n up to 10 using a for loop.


num = int(input("Enter a number: "))

def Table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
        
Table(num)
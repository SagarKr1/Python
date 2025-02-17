# Write a Python program that checks the value of a variable score and prints the
# corresponding grade:
# If score >= 90, print "A".
# If score >= 80, print "B".
# If score >= 70, print "C".
# Otherwise, print "Fail".
print("Question 1")
print("************************************************************************")
math = float(input("Enter you math marks: "))
science = float(input("Enter you science marks: "))
sst = float(input("Enter you sst marks: "))
computer = float(input("Enter you computer marks: "))

per = (math + science + sst + computer) / 4

print("\n Your Percentage: ", per)

if per >= 90:
    print("Your Grade is A")
elif per >= 80 and per < 90:
    print("Your Grade is B")
elif per >= 70 and per < 80:
    print("Your Grade is C")
elif per >= 60 and per < 70:
    print("Your Grade is D")
else:
    print("Fail")


# Write a Python program that prints numbers from 1 to 100.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For numbers that are multiples of both 3 and 5, print "FizzBuzz".
print("Question 2")
print("************************************************************************")

for num in range(1, 101):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

# 1. Write a Python program that checks if a number is prime using a for loop.

# 2. Write a Python program that checks if a string is a palindrome using a for loop.

# 3. Write a Python function called fibonacci that takes an integer n .
# as input and returns the first n numbers in the Fibonacci sequence using a while loop.

# 4. Write a Python function called multiplication_table that takes an integer n as input and 
# prints the multiplication table for n up to 10 using a for loop.

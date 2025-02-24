# 1. What will be the output of the following code?
# def func(x, y=[]):

#     y.append(x)

#     return y

# print(func(1))

# print(func(2))

# Ans [1],[1, 2]

# 2. What will be the output of this recursive function?
# def recur(n):

#     if n == 0:

#         return 1

#     return n * recur(n - 1)


# print(recur(4))

# numbers = [10, 20, 30, 90,40]
# numbers.remove(90)
# print(numbers)  # Output: [10, 30, 40]


# 9. What will be the output of the following code?

# def scope_test():

#     a = 5


# scope_test()

# print(a)

# 11. What will be the output?

# x = 10

# def my_func():

#     global x

#     x = 20

# my_func()

# print(x)

# 13. What is the output of the following function?


# def outer():

#     x = "local"

#     def inner():

#         nonlocal x

#         x = "nonlocal"

#         print(x)

#     inner()

#     print(x)


# outer()

#15. What will be the output of the following code?


# def add(x, y=5):  

#     return x + y  

# print(add(3))


#16 What will be the output of the following code? 
# def outer():

#     x = "Hello"


#     def inner():

#         print(x)


#     return inner  


# my_func = outer()  

# my_func()

#19 What will be the output of the following code? 
# x = 5 
# if x == 5: 
#     print("Yes") 
# elif x > 2: 
#     print("No")

# my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# keys = my_dict.keys()  
# print(keys)  # Output: dict_keys(['name', 'age', 'city'])

# What will be the output of the following code? 
# x = 0 
# if not x: 
#     print("Hello")

# What will be the output of the following code? 

my_dict = {"a": 1, "b": 2}  

print(my_dict.get("c"))
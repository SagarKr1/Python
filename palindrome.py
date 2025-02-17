# 2. Write a Python program that checks if a string is a palindrome using a for loop.

str = input("Enter a string: ")

lstr = str.lower()

count = 0

for i in range(len(lstr) // 2):
    num = -(i + 1)
    if lstr[i] != lstr[num]:
        count += 1
        break

# Print result
if count == 0:
    print(f"{str} is a palindrome string")
else:
    print(f"{str} is not a palindrome string")

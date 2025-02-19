# 1. Count the Number of Vowels in a String #
# vowels are (aeiou)
print("1. Vowels ")
print()
def vowels(string):
    count = 0
    print("String are ",string)
    for char in string:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            count += 1
    
    return count

# Example usage:
string = input("Enter a string: ")
lstring = string.lower()
count = vowels(lstring)
print(f"Number of vowels in '{lstring}': {count}")



# 2. Find the Second Largest Number in a List
print()
print()

print("2. Second Largest Number")
def s_largest(ls):
    print(ls)
    ls.sort()
    print(ls)
    return ls[-2]


ls=[20,26,12,33,66]
num=s_largest(ls)
print("Second largest number is ",num)

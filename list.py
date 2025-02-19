#list - ordered,mutable,duplicates allowed. 

#set- unordered,not allow duplicate values,mutable

#tuple-ordered,immutable, 

#dictionary- key-value,keys need to be unique , values can repeat, mutable

a=[12,23,45,67,100]

# l1=

# a1=list()

b={12,23,45,67,100}

print(b)

c=(12,23,45,67,100)

print(type(b))

d={'name':'shakul','age':30,'salary':1000000}

print(a[-1])#12

#searching-indexing and dslicing

#accessing

for i in a:

    print(i)

a[3]=2000

print(a)

a.append([10000,80000])

print(a)

a.pop()

print(a)
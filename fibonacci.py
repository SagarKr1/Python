# 3. Write a Python function called fibonacci that takes an integer n .

n1=0
n2=1
num = int(input("Enter n term: "))
print(f"{n1} {n2}",end=" ")
while num >0 :
    sum = n1+n2
    print(sum,end=" ")
    n1 = n2
    n2 = sum
    num-=1

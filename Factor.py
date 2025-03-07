num=int(input("Enter a number: "))

factor=[]
print(f"Factorization of {num}: ",end=" ")
for i in range(1,num+1):
    # print(i)
    if num%i==0:
        print(i,end=" ")
        factor.append(i)
print()
print(factor)

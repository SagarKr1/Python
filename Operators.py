n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

print("\n" + "="*30)
# print(f"Logical AND (both positive)")
print(" Summary of Calculations")

print("="*30)

sum = n1+n2
print("Addition ",n1,"+",n2 ," = ",sum)
sub = n1-n2
print("subtraction ",n1,"-",n2 ," = ",sub)
mul = n1*n2
print("multiplication ",n1,"*",n2 ," = ",mul)
pow = n1**n2
print("Power ",n1,"**",n2 ," = ",pow)
div = n1/n2
print("division(/) ",n1,"/",n2 ," = ",div)
d = n1//n2
print("division(//)  ",n1,"//",n2 ," = ",d)
mod = n1%n2
print("Modulor ",n1,"%",n2 ," = ",mod)


print("== ",n1,"==",n2," = ",n1==n2)
print("> ",n1,">",n2," = ",n1>n2)
print(">= ",n1,">=",n2," = ",n1>=n2)
print("< ",n1,"<",n2," = ",n1<n2)
print("<= ",n1,"<=",n2," = ",n1<=n2)
print("!= ",n1,"!=",n2," = ",n1!=n2)

print("and (n1<n2) and (n1!=n2) = ",(n1<n2) and (n1!=n2) )
print("or (n1<n2) or (n1!=n2) = ",(n1<n2) or (n1!=n2))
print("not  not(n1==n2) = ",not(n1==n2))
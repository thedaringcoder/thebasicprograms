a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a<b:
    s=a
else:
    s=b
gcd=1
for i in range(1,s+1):
    if a%i==0 and b%i==0:
        gcd=i
print("greatest common divisor is: ",gcd)
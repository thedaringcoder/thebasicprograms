sum=0
n=int(input("enter number: "))
for i in range(1,n):
    if n%i==0:
        sum += i
if n==sum:
    print("Armstrong Number")
else:
    print("Not an Armstron Number")
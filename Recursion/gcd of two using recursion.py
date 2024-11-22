def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

x=int(input("enter number"))
y=int(input("enter number"))
print(gcd(x,y))
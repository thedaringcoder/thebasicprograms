def multi(a,b):
    if b==1:
        return a
    else:
        return multi(a,b-1) + a

x=int(input("enter a number: "))
y=int(input("enter a number"))
print(multi(x,y))
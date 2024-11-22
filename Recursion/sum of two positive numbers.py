def sum2p(a,b):
    if b==0:
        return a
    else:
        return sum2p(a,b-1) + 1

x=int(input("enter first number: "))
y=int(input("enter second number: "))
print(sum2p(x,y))
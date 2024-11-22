n=int(input("enter the maximum limit: "))
k=0
for i in range(n,0,-1):
    print(" "*k,end="")
    for j in range(i):
        print("*",end=" ")
    print()
    k+=1
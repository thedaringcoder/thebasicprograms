def checkrighttriangle():
    a=int(input("enter first side"))
    b=int(input("enter second side"))
    c=int(input("enter third side"))
    if a<b:
        hyp=b
        l,k=a,c
    else:
        hyp=a
        l,k=b,c
    if hyp<c:
        hyp=c
        l,k=a,b
    if hyp**2==l**2+k**2:
        print("Triangle is a right angle triangle")
    else:
        print("Triangle is NOT a right angle triangle")
checkrighttriangle()